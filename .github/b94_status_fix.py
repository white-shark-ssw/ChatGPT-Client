from pathlib import Path
p=Path('docs/project/current/dev/DEV-send-stream.md')
s=p.read_text()
old='**Active — new exact b92 single-executor Runtime proves background lifecycle can stop the official page-owned continuation loop, and exact b93 proves selection focus reacquisition succeeds but is not sufficient to restart a stopped loop. b93 focus-sufficient is Rejected. The next isolated evidence target is exact b94 official-page rebootstrap on foreground for one active external response; b94 is allocated only for that A/B. Stable/Frozen Send remains No.**'
new='**Active — exact b92 single-executor Runtime proves background lifecycle can stop the official page-owned continuation loop, and exact b93 proves selection focus reacquisition succeeds but is not sufficient to restart a stopped loop. b93 focus-sufficient is Rejected. Exact b94 foreground official-page rebootstrap is Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified; Human Runtime pending. Stable/Frozen Send remains No.**'
assert old in s
p.write_text(s.replace(old,new,1))
