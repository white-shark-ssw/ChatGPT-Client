#!/usr/bin/env python3
import argparse
import struct
from pathlib import Path

MH_MAGIC_64 = 0xFEEDFACF
LC_LOAD_WEAK_DYLIB = 0x80000018


def align8(value: int) -> int:
    return (value + 7) & ~7


def read_header(data: bytearray):
    if len(data) < 32:
        raise SystemExit("Mach-O too small")
    magic = struct.unpack_from("<I", data, 0)[0]
    if magic != MH_MAGIC_64:
        raise SystemExit(f"unsupported Mach-O magic: 0x{magic:08x}")
    ncmds = struct.unpack_from("<I", data, 16)[0]
    sizeofcmds = struct.unpack_from("<I", data, 20)[0]
    return ncmds, sizeofcmds


def load_dylib_names(data: bytearray):
    ncmds, _ = read_header(data)
    offset = 32
    names = []
    for _ in range(ncmds):
        cmd, cmdsize = struct.unpack_from("<II", data, offset)
        if cmdsize < 8 or offset + cmdsize > len(data):
            raise SystemExit("invalid Mach-O load command")
        if cmd in {0xC, 0xD, 0x80000018, 0x8000001F, 0x80000023}:
            name_offset = struct.unpack_from("<I", data, offset + 8)[0]
            start = offset + name_offset
            end = data.find(b"\0", start, offset + cmdsize)
            if end < 0:
                raise SystemExit("unterminated dylib load command")
            names.append(data[start:end].decode("utf-8", "replace"))
        offset += cmdsize
    return names


def inject(path: Path, install_name: str):
    data = bytearray(path.read_bytes())
    ncmds, sizeofcmds = read_header(data)
    if install_name in load_dylib_names(data):
        raise SystemExit(f"load command already exists: {install_name}")

    encoded = install_name.encode("utf-8") + b"\0"
    cmdsize = align8(24 + len(encoded))
    insertion = 32 + sizeofcmds
    if insertion + cmdsize > len(data):
        raise SystemExit("no room for load command")
    if any(data[insertion:insertion + cmdsize]):
        raise SystemExit(f"non-zero Mach-O header padding at 0x{insertion:x}")

    command = bytearray(cmdsize)
    struct.pack_into("<IIIIII", command, 0, LC_LOAD_WEAK_DYLIB, cmdsize, 24, 0, 0, 0)
    command[24:24 + len(encoded)] = encoded
    data[insertion:insertion + cmdsize] = command
    struct.pack_into("<I", data, 16, ncmds + 1)
    struct.pack_into("<I", data, 20, sizeofcmds + cmdsize)
    path.write_bytes(data)

    updated = bytearray(path.read_bytes())
    names = load_dylib_names(updated)
    if install_name not in names:
        raise SystemExit("injected load command did not verify")
    print(f"injected {install_name}")
    print(f"ncmds {ncmds} -> {ncmds + 1}")
    print(f"sizeofcmds {sizeofcmds} -> {sizeofcmds + cmdsize}")
    print(f"command_offset=0x{insertion:x} command_size={cmdsize}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mach_o", type=Path)
    parser.add_argument("install_name")
    args = parser.parse_args()
    inject(args.mach_o, args.install_name)


if __name__ == "__main__":
    main()
