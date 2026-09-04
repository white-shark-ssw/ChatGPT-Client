# DEV-send-stream round 7 Runtime addendum

## Probe v0.7 package / Human Runtime gate — 2026-09-04

- User-uploaded `ChatGPTRealtimeProbe(6).jsonl` is byte-identical to the already analyzed Probe v0.6 Runtime file: `sha256:1cb6eb096c5748e7f781afbd761906bda39d55227a115a4e2dcea8c240de7a43`, 78,828 bytes / 207 valid events / zero parse errors / all `probeVersion=0.6`. It is not a v0.7 sample and adds no new Runtime evidence.
- The duplicate file still reconfirms the prior v0.6 result only: target `0df178903e95` authoritative Conversation Detail GET polling is Runtime Positive and `probe.detail_task_callback_surface` exposes `_task_onqueue_didReceiveDispatchData:completionHandler:` plus dispatch-data storage/callback surface. `http.conversation_detail.async_status` remains absent because v0.6 did not hook this path.
- Probe v0.7 research source/head is `718accba952bea2cb59005d17b8bf44317624f1c`. Dedicated research `build-probe` `33844386493 / 100933029519` passed; canonical Artifact `9925975675`; Artifact digest / downloaded ZIP SHA `sha256:26aff9c1c911dd74f88f587df248fdf5552d636fc9f5f549d5afd76e5bff1835`; Probe dylib `sha256:398d21e114f76b16e590b769878e3fb2a00899b2d95dccda5db69b84d1771101` matching sidecar.
- Against pristine official source ZIP `sha256:bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, independently repacked `ChatGPT-Official-RealtimeProbe-v07-TrollStore-20260904.ipa` is `sha256:c4b2e81b60d34a4e9926585881b87cf8ebf4527b9890f15497cc95acd96fab94`; outer ZIP is `sha256:5bd576c42fced0812fdfc775f88482668316b0aaf8ce1db12fc02c6bac18fcf9`. Package preserves `com.openai.chat / 1.2026.202 / 30140022279`, passes ZIP integrity, preserves dylib mode `0755`, and differs from pristine source in exactly three intended paths: original enhancer backup added, enhancer load entry replaced by Probe v0.7, research marker added.
- Probe v0.7 remains research-only. It observes only the Runtime-evidenced dispatch-data callback and scans authoritative Detail data for exact `conversation_async_status`; it adds no request, polling cadence, timer, retry, `/resume`, duplicate Send, response store or product authority.
- Evidence ladder: **v0.6 Human Runtime already analyzed / duplicate v0.6 re-upload identified / v0.7 research code + dedicated CI + Artifact + package verified / v0.7 Human Runtime pending / product remains b95 / b96 unallocated / Stable-Frozen Send No.**
- **Next exact action:** install exact Probe v0.7, fully relaunch official ChatGPT, press `清空`, run one deliberately long cross-platform response, export JSONL, and first require `probeVersion=0.7`. Decisive evidence is same-target `http.conversation_detail.async_status`, ideally an actually observed active-to-terminal transition such as `is_streaming -> complete`. Do not allocate b96 before that result.

## Earlier round 7 acquisition conclusion

- Visible official iOS left on conversation A did not automatically refresh when ChatGPTClient sent a new turn to A.
- This is Runtime Negative for passive official iOS UI refresh as an acquisition mechanism.
- b80 already proved that once explicit Sync/re-arm succeeds, the adopted-response path can expose accumulated reasoning/tool snapshots; another conversation failed to expose reasoning until that acquisition/re-arm happened.
- Therefore the current unresolved problem is automatic acquisition timing: knowing early enough that a remote turn started so the existing authoritative acquisition path can run.
- The native realtime investigation is only testing whether such an early target-conversation event exists below the visible UI. It is not intended to make official iOS refresh, and it does not by itself provide token-by-token reasoning streaming.
- Decision gate: early event -> candidate acquisition trigger; completion-only event -> completion hint only; no useful event -> reject this branch and design bounded selected-conversation monitoring.
- b83 remains unallocated.
