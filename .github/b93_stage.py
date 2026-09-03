from pathlib import Path
import sys

ROOT = Path("ChatGPTClient/RootViewController.swift")
PBX = Path("ChatGPTClient.xcodeproj/project.pbxproj")
CHECKPOINT = Path("docs/project/current/dev/DEV-send-stream.md")


def allocate() -> None:
    root = ROOT.read_text()
    pbx = PBX.read_text()
    checkpoint = CHECKPOINT.read_text()
    assert "hostView.bringSubviewToFront(webView)" not in root
    assert "location.pathname.match(/^\\/(?:g\\/[^/?#]+\\/)?c\\/([^/?#]+)/)" in root
    assert pbx.count("CURRENT_PROJECT_VERSION = 92;") == 2
    assert pbx.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b92";') == 2
    assert "## b93 exact minimum A/B — not yet allocated" in checkpoint
    assert "DEV-send-stream-0.1.0-b93" not in checkpoint
    checkpoint = checkpoint.replace(
        "- b92 Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b92-covered-overlap-focus-handoff-20260903.md`\n",
        "- b92 Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b92-covered-overlap-focus-handoff-20260903.md`\n- b93 Candidate / Build: `DEV-send-stream-0.1.0-b93` / `0.1.0 (93)` permanently reserved; product/package pending at allocation checkpoint\n",
        1,
    )
    checkpoint = checkpoint.replace("## b93 exact minimum A/B — not yet allocated", "## b93 exact minimum A/B — allocated", 1)
    checkpoint = checkpoint.replace("b93 has not been allocated in this Runtime-recording checkpoint.", "b93 is allocated only for selection-time external focus reacquisition; product/package is pending.", 1)
    checkpoint = checkpoint.replace(
        "**Closed for b92 Runtime classification. Next exact action:** perform a fresh resume/conflict guard, then allocate b93 only for the selection-time external-focus reacquisition A/B above. Do not modify continuation protocol or add speculative recovery logic.",
        "**Open for b93 selection-focus A/B. Next exact action:** apply only selection-time focus reacquisition to the existing external-live executor, validate exact two-file product scope + Simulator, then package b93 and stop at Human Runtime. Do not modify continuation protocol or add speculative recovery logic.",
        1,
    )
    CHECKPOINT.write_text(checkpoint)


def product() -> None:
    root = ROOT.read_text()
    pbx = PBX.read_text()
    checkpoint = CHECKPOINT.read_text()
    assert "## b93 exact minimum A/B — allocated" in checkpoint
    assert "DEV-send-stream-0.1.0-b93" in checkpoint
    assert "selection_external_focus_rearm" not in root
    old = '''        diagnostics.info(category: "webSend", name: "coveredExecutor.observing", fields: ["target": "existing_conversation", "mode": forceReload ? "manual_sync_rearm" : "selection"])
    }

    func sendExistingConversation(text: String, conversationID: String, events: @escaping (CoveredWebSendEvent) -> Void) {'''
    new = '''        diagnostics.info(category: "webSend", name: "coveredExecutor.observing", fields: ["target": "existing_conversation", "mode": forceReload ? "manual_sync_rearm" : "selection"])
    }

    func reactivateExternalObservationFocus() {
        precondition(Thread.isMainThread)
        guard observingExternalResponse else { return }
        logWebViewActivationState(stage: "selection_external_focus_rearm")
        let nativeFirstResponder = webView.becomeFirstResponder()
        diagnostics.info(category: "webSend", name: "coveredExecutor.selectionFocusActivationAttempt", fields: ["nativeFirstResponder": nativeFirstResponder ? "true" : "false"])
        webView.evaluateJavaScript("document.hasFocus()") { [weak self] result, error in
            guard let self else { return }
            let documentHasFocus = (result as? Bool) == true
            self.diagnostics.info(category: "webSend", name: "coveredExecutor.selectionFocusActivationResult", fields: ["nativeFirstResponder": nativeFirstResponder ? "true" : "false", "documentHasFocus": documentHasFocus ? "true" : "false", "evaluation": error == nil ? "succeeded" : "failed"])
        }
    }

    func sendExistingConversation(text: String, conversationID: String, events: @escaping (CoveredWebSendEvent) -> Void) {'''
    assert root.count(old) == 1
    root = root.replace(old, new, 1)
    old2 = '''            default:
                guard let generation = externalGeneration else { return }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            }
        }
    }

    private func handleExternalAcquisitionHint'''
    new2 = '''            default:
                guard let generation = externalGeneration else { return }
                self.repository.consumeLiveResponseEvent(event, conversationID: conversationID, generation: generation)
            }
        }
        if existingSnapshot?.phase.isActive == true, existingSnapshot?.promptText.isEmpty == true { sendExecutor.reactivateExternalObservationFocus() }
    }

    private func handleExternalAcquisitionHint'''
    assert root.count(old2) == 1
    root = root.replace(old2, new2, 1)
    assert pbx.count("CURRENT_PROJECT_VERSION = 92;") == 2
    assert pbx.count('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b92";') == 2
    pbx = pbx.replace("CURRENT_PROJECT_VERSION = 92;", "CURRENT_PROJECT_VERSION = 93;")
    pbx = pbx.replace('DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b92";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b93";')
    ROOT.write_text(root)
    PBX.write_text(pbx)


if len(sys.argv) != 2 or sys.argv[1] not in {"allocate", "product"}:
    raise SystemExit("usage: b93_stage.py allocate|product")
if sys.argv[1] == "allocate": allocate()
else: product()
