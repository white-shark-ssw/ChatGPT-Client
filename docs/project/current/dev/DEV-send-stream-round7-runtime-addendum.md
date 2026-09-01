# DEV-send-stream round 7 Runtime addendum

- Visible official iOS left on conversation A did not automatically refresh when ChatGPTClient sent a new turn to A.
- This is Runtime Negative for passive official iOS UI refresh as an acquisition mechanism.
- b80 already proved that once explicit Sync/re-arm succeeds, the adopted-response path can expose accumulated reasoning/tool snapshots; another conversation failed to expose reasoning until that acquisition/re-arm happened.
- Therefore the current unresolved problem is automatic acquisition timing: knowing early enough that a remote turn started so the existing authoritative acquisition path can run.
- The native realtime investigation is only testing whether such an early target-conversation event exists below the visible UI. It is not intended to make official iOS refresh, and it does not by itself provide token-by-token reasoning streaming.
- Decision gate: early event -> candidate acquisition trigger; completion-only event -> completion hint only; no useful event -> reject this branch and design bounded selected-conversation monitoring.
- b83 remains unallocated.
