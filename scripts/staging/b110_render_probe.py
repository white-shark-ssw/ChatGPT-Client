from pathlib import Path

PROJECT = Path("ChatGPTClient.xcodeproj/project.pbxproj")
FEATURE = Path("ChatGPTClient/Conversation/ConversationFeature.swift")


def replace_exact(path: Path, old: str, new: str, expected_count: int = 1) -> None:
    text = path.read_text()
    actual = text.count(old)
    if actual != expected_count:
        raise SystemExit(f"{path}: expected {expected_count} occurrences, found {actual}: {old!r}")
    path.write_text(text.replace(old, new, expected_count))


replace_exact(PROJECT, "CURRENT_PROJECT_VERSION = 109;", "CURRENT_PROJECT_VERSION = 110;", 2)
replace_exact(PROJECT, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b109";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b110";', 2)

method_marker = """        return resolved.description
    }

    override func layoutSubviews() {
"""
method_replacement = """        return resolved.description
    }

    func bodyRenderedColorDiagnostics() -> [String: String] {
        var fields: [String: String] = [
            "labelAlpha": String(format: "%.3f", messageLabel.alpha),
            "bubbleAlpha": String(format: "%.3f", bubbleView.alpha),
            "contentAlpha": String(format: "%.3f", contentView.alpha),
            "labelLayerOpacity": String(format: "%.3f", messageLabel.layer.opacity),
            "labelPresentationOpacity": messageLabel.layer.presentation().map { String(format: "%.3f", $0.opacity) } ?? "none"
        ]
        renderedInkDiagnostics(image: renderedLabelImage(), prefix: "labelRender").forEach { fields[$0.key] = $0.value }
        renderedInkDiagnostics(image: renderedHierarchyCropImage(), prefix: "hierarchyCrop").forEach { fields[$0.key] = $0.value }
        return fields
    }

    private func renderedLabelImage() -> UIImage? {
        let size = messageLabel.bounds.size
        guard size.width >= 1, size.height >= 1 else { return nil }
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        format.opaque = false
        return UIGraphicsImageRenderer(size: size, format: format).image { _ in
            messageLabel.drawHierarchy(in: messageLabel.bounds, afterScreenUpdates: true)
        }
    }

    private func renderedHierarchyCropImage() -> UIImage? {
        let frame = messageLabel.convert(messageLabel.bounds, to: contentView)
        guard frame.width >= 1, frame.height >= 1 else { return nil }
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        format.opaque = false
        return UIGraphicsImageRenderer(size: frame.size, format: format).image { context in
            context.cgContext.translateBy(x: -frame.minX, y: -frame.minY)
            contentView.drawHierarchy(in: contentView.bounds, afterScreenUpdates: true)
        }
    }

    private func renderedInkDiagnostics(image: UIImage?, prefix: String) -> [String: String] {
        guard let cgImage = image?.cgImage else { return ["\(prefix)Status": "image_unavailable"] }
        let width = cgImage.width
        let height = cgImage.height
        guard width > 0, height > 0 else { return ["\(prefix)Status": "empty"] }
        var pixels = [UInt8](repeating: 0, count: width * height * 4)
        let colorSpace = CGColorSpaceCreateDeviceRGB()
        let bitmapInfo = CGBitmapInfo.byteOrder32Big.rawValue | CGImageAlphaInfo.premultipliedLast.rawValue
        guard let context = CGContext(data: &pixels, width: width, height: height, bitsPerComponent: 8, bytesPerRow: width * 4, space: colorSpace, bitmapInfo: bitmapInfo) else { return ["\(prefix)Status": "context_unavailable"] }
        context.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
        var redSum = 0.0
        var greenSum = 0.0
        var blueSum = 0.0
        var sampleCount = 0
        var nearWhiteCount = 0
        var blueDominantCount = 0
        for offset in stride(from: 0, to: pixels.count, by: 4) {
            let alpha = Double(pixels[offset + 3]) / 255.0
            guard alpha > 0.06 else { continue }
            let red = min(1, (Double(pixels[offset]) / 255.0) / alpha)
            let green = min(1, (Double(pixels[offset + 1]) / 255.0) / alpha)
            let blue = min(1, (Double(pixels[offset + 2]) / 255.0) / alpha)
            guard max(red, green, blue) > 0.18 else { continue }
            sampleCount += 1
            redSum += red
            greenSum += green
            blueSum += blue
            if min(red, green, blue) > 0.75 && max(red, green, blue) - min(red, green, blue) < 0.08 { nearWhiteCount += 1 }
            if blue - red > 0.12 && blue - green > 0.08 { blueDominantCount += 1 }
        }
        guard sampleCount > 0 else { return ["\(prefix)Status": "no_ink_pixels", "\(prefix)PixelCount": "0"] }
        let count = Double(sampleCount)
        return [
            "\(prefix)Status": "ok",
            "\(prefix)PixelCount": String(sampleCount),
            "\(prefix)InkRGB": String(format: "%.3f,%.3f,%.3f", redSum / count, greenSum / count, blueSum / count),
            "\(prefix)NearWhiteFraction": String(format: "%.3f", Double(nearWhiteCount) / count),
            "\(prefix)BlueDominantFraction": String(format: "%.3f", Double(blueDominantCount) / count)
        ]
    }

    override func layoutSubviews() {
"""
replace_exact(FEATURE, method_marker, method_replacement)

authoritative_marker = """            diagnostics.info(category: "ui", name: "assistantChunkColor.willDisplay", fields: fields)
            return
"""
authoritative_replacement = """            diagnostics.info(category: "ui", name: "assistantChunkColor.willDisplay", fields: fields)
            scheduleAssistantChunkRenderDiagnostics(messageCell, tableView: tableView, indexPath: indexPath, surface: "authoritative", chunkIndex: row.chunkIndex, chunkCount: row.chunkCount)
            return
"""
replace_exact(FEATURE, authoritative_marker, authoritative_replacement)

live_marker = """        diagnostics.info(category: "ui", name: "assistantChunkColor.willDisplay", fields: fields)
    }

    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {
"""
live_replacement = """        diagnostics.info(category: "ui", name: "assistantChunkColor.willDisplay", fields: fields)
        scheduleAssistantChunkRenderDiagnostics(messageCell, tableView: tableView, indexPath: indexPath, surface: "live", chunkIndex: row.chunkIndex, chunkCount: row.chunkCount)
    }

    private func scheduleAssistantChunkRenderDiagnostics(_ messageCell: ConversationMessageCell, tableView: UITableView, indexPath: IndexPath, surface: String, chunkIndex: Int, chunkCount: Int) {
        DispatchQueue.main.async { [weak self, weak tableView, weak messageCell] in
            guard let self = self, let tableView = tableView, let messageCell = messageCell, tableView.indexPath(for: messageCell) == indexPath else { return }
            var fields = messageCell.bodyRenderedColorDiagnostics()
            fields["surface"] = surface
            fields["rowIndex"] = String(indexPath.row)
            fields["chunkIndex"] = String(chunkIndex)
            fields["chunkCount"] = String(chunkCount)
            self.diagnostics.info(category: "ui", name: "assistantChunkRender.afterDisplay", fields: fields)
        }
    }

    func tableView(_ tableView: UITableView, contextMenuConfigurationForRowAt indexPath: IndexPath, point: CGPoint) -> UIContextMenuConfiguration? {
"""
replace_exact(FEATURE, live_marker, live_replacement)
