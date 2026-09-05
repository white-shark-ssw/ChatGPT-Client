from pathlib import Path

PROJECT = Path("ChatGPTClient.xcodeproj/project.pbxproj")
FEATURE = Path("ChatGPTClient/Conversation/ConversationFeature.swift")


def replace_exact(path: Path, old: str, new: str, expected_count: int = 1) -> None:
    text = path.read_text()
    actual = text.count(old)
    if actual != expected_count:
        raise SystemExit(f"{path}: expected {expected_count} occurrences, found {actual}: {old!r}")
    path.write_text(text.replace(old, new, expected_count))


replace_exact(PROJECT, "CURRENT_PROJECT_VERSION = 110;", "CURRENT_PROJECT_VERSION = 111;", 2)
replace_exact(PROJECT, 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b110";', 'DIAGNOSTICS_CANDIDATE = "DEV-send-stream-0.1.0-b111";', 2)

reuse_marker = '    static let reuseIdentifier = "ConversationMessageCell"\n\n'
reuse_replacement = '    static let reuseIdentifier = "ConversationMessageCell"\n    private static var diagnosticCellOrdinalSeed = 0\n\n'
replace_exact(FEATURE, reuse_marker, reuse_replacement)

property_marker = """    private var onCopy: (() -> Void)?
    private var onToggleReasoning: (() -> Void)?
    private var onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?
    private var layoutMetrics = Metrics(rowHeight: 44, timestampFrame: .zero, bubbleFrame: .zero, reasoningButtonFrame: .zero, reasoningBodyFrame: .zero, reasoningDividerFrame: .zero, messageFrame: .zero, copyFrame: .zero)

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
"""
property_replacement = """    private var onCopy: (() -> Void)?
    private var onToggleReasoning: (() -> Void)?
    private var onToggleToolDetail: ((Int, ConversationToolDetailSection) -> Void)?
    private var layoutMetrics = Metrics(rowHeight: 44, timestampFrame: .zero, bubbleFrame: .zero, reasoningButtonFrame: .zero, reasoningBodyFrame: .zero, reasoningDividerFrame: .zero, messageFrame: .zero, copyFrame: .zero)
    private var diagnosticCellOrdinal = 0
    private var lastConfiguredRoleForDiagnostics = "none"
    private var reusedFromRoleForDiagnostics = "none"
    private var reusedFromLinkRunCountForDiagnostics = 0

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        Self.diagnosticCellOrdinalSeed += 1
        diagnosticCellOrdinal = Self.diagnosticCellOrdinalSeed
"""
replace_exact(FEATURE, property_marker, property_replacement)

prepare_marker = """    override func prepareForReuse() {
        super.prepareForReuse()
        onCopy = nil
        onToggleReasoning = nil
        onToggleToolDetail = nil
        messageLabel.text = nil
"""
prepare_replacement = """    override func prepareForReuse() {
        super.prepareForReuse()
        reusedFromRoleForDiagnostics = lastConfiguredRoleForDiagnostics
        reusedFromLinkRunCountForDiagnostics = attributedLinkRunCount(messageLabel.attributedText)
        onCopy = nil
        onToggleReasoning = nil
        onToggleToolDetail = nil
        messageLabel.text = nil
"""
replace_exact(FEATURE, prepare_marker, prepare_replacement)

render_marker = """    func bodyRenderedColorDiagnostics() -> [String: String] {
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
"""
render_replacement = """    func bodyRenderedColorDiagnostics() -> [String: String] {
        var fields: [String: String] = [
            "labelAlpha": String(format: "%.3f", messageLabel.alpha),
            "bubbleAlpha": String(format: "%.3f", bubbleView.alpha),
            "contentAlpha": String(format: "%.3f", contentView.alpha),
            "labelLayerOpacity": String(format: "%.3f", messageLabel.layer.opacity),
            "labelPresentationOpacity": messageLabel.layer.presentation().map { String(format: "%.3f", $0.opacity) } ?? "none",
            "cellOrdinal": String(diagnosticCellOrdinal),
            "reusedFromRole": reusedFromRoleForDiagnostics,
            "reusedFromLinkRunCount": String(reusedFromLinkRunCountForDiagnostics)
        ]
        attributedStructureDiagnostics().forEach { fields[$0.key] = $0.value }
        let hierarchyImage = renderedLabelImage()
        renderedInkDiagnostics(image: hierarchyImage, prefix: "labelRender").forEach { fields[$0.key] = $0.value }
        transparentInkDiagnostics(image: hierarchyImage, prefix: "labelHierarchyTransparent").forEach { fields[$0.key] = $0.value }
        transparentInkDiagnostics(image: renderedLabelLayerImage(), prefix: "labelLayerTransparent").forEach { fields[$0.key] = $0.value }
        transparentInkDiagnostics(image: directAttributedImage(), prefix: "directAttributedTransparent").forEach { fields[$0.key] = $0.value }
        renderedInkDiagnostics(image: renderedHierarchyCropImage(), prefix: "hierarchyCrop").forEach { fields[$0.key] = $0.value }
        return fields
    }

    private func attributedStructureDiagnostics() -> [String: String] {
        guard let attributedText = messageLabel.attributedText, attributedText.length > 0 else {
            return ["attributedLength": "0", "attributeRunCount": "0", "foregroundRunCount": "0", "foregroundDistinctColors": "none", "linkRunCount": "0", "attachmentRunCount": "0"]
        }
        let range = NSRange(location: 0, length: attributedText.length)
        var attributeRunCount = 0
        var foregroundRunCount = 0
        var foregroundColors = Set<String>()
        var linkRunCount = 0
        var attachmentRunCount = 0
        attributedText.enumerateAttributes(in: range, options: []) { attributes, _, _ in
            attributeRunCount += 1
            if let color = attributes[.foregroundColor] as? UIColor {
                foregroundRunCount += 1
                foregroundColors.insert(diagnosticsColor(color))
            }
            if attributes[.link] != nil { linkRunCount += 1 }
            if attributes[.attachment] != nil { attachmentRunCount += 1 }
        }
        return [
            "attributedLength": String(attributedText.length),
            "attributeRunCount": String(attributeRunCount),
            "foregroundRunCount": String(foregroundRunCount),
            "foregroundDistinctColors": foregroundColors.sorted().joined(separator: "|").nilIfEmpty ?? "none",
            "linkRunCount": String(linkRunCount),
            "attachmentRunCount": String(attachmentRunCount)
        ]
    }

    private func attributedLinkRunCount(_ attributedText: NSAttributedString?) -> Int {
        guard let attributedText = attributedText, attributedText.length > 0 else { return 0 }
        var count = 0
        attributedText.enumerateAttribute(.link, in: NSRange(location: 0, length: attributedText.length), options: []) { value, _, _ in
            if value != nil { count += 1 }
        }
        return count
    }

    private func renderedLabelImage() -> UIImage? {
"""
# Avoid adding a String extension just for diagnostics; use a local expression instead.
render_replacement = render_replacement.replace('foregroundColors.sorted().joined(separator: "|").nilIfEmpty ?? "none"', '(foregroundColors.isEmpty ? "none" : foregroundColors.sorted().joined(separator: "|"))')
replace_exact(FEATURE, render_marker, render_replacement)

label_image_marker = """    private func renderedHierarchyCropImage() -> UIImage? {
"""
label_image_replacement = """    private func renderedLabelLayerImage() -> UIImage? {
        let size = messageLabel.bounds.size
        guard size.width >= 1, size.height >= 1 else { return nil }
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        format.opaque = false
        return UIGraphicsImageRenderer(size: size, format: format).image { context in
            messageLabel.layer.render(in: context.cgContext)
        }
    }

    private func directAttributedImage() -> UIImage? {
        guard let attributedText = messageLabel.attributedText, attributedText.length > 0 else { return nil }
        let size = messageLabel.bounds.size
        guard size.width >= 1, size.height >= 1 else { return nil }
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        format.opaque = false
        return UIGraphicsImageRenderer(size: size, format: format).image { _ in
            attributedText.draw(with: messageLabel.bounds, options: [.usesLineFragmentOrigin, .usesFontLeading], context: nil)
        }
    }

    private func renderedHierarchyCropImage() -> UIImage? {
"""
replace_exact(FEATURE, label_image_marker, label_image_replacement)

transparent_marker = """    private func renderedInkDiagnostics(image: UIImage?, prefix: String) -> [String: String] {
"""
transparent_replacement = """    private func transparentInkDiagnostics(image: UIImage?, prefix: String) -> [String: String] {
        guard let cgImage = image?.cgImage else { return ["\\(prefix)Status": "image_unavailable"] }
        let width = cgImage.width
        let height = cgImage.height
        guard width > 0, height > 0 else { return ["\\(prefix)Status": "empty"] }
        var pixels = [UInt8](repeating: 0, count: width * height * 4)
        let colorSpace = CGColorSpaceCreateDeviceRGB()
        let bitmapInfo = CGBitmapInfo.byteOrder32Big.rawValue | CGImageAlphaInfo.premultipliedLast.rawValue
        guard let context = CGContext(data: &pixels, width: width, height: height, bitsPerComponent: 8, bytesPerRow: width * 4, space: colorSpace, bitmapInfo: bitmapInfo) else { return ["\\(prefix)Status": "context_unavailable"] }
        context.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
        var redSum = 0.0
        var greenSum = 0.0
        var blueSum = 0.0
        var sampleCount = 0
        var blueDominantCount = 0
        for offset in stride(from: 0, to: pixels.count, by: 4) {
            let alpha = Double(pixels[offset + 3]) / 255.0
            guard alpha > 0.06 else { continue }
            let red = min(1, (Double(pixels[offset]) / 255.0) / alpha)
            let green = min(1, (Double(pixels[offset + 1]) / 255.0) / alpha)
            let blue = min(1, (Double(pixels[offset + 2]) / 255.0) / alpha)
            sampleCount += 1
            redSum += red
            greenSum += green
            blueSum += blue
            if blue - red > 0.12 && blue - green > 0.08 { blueDominantCount += 1 }
        }
        guard sampleCount > 0 else { return ["\\(prefix)Status": "no_ink_pixels", "\\(prefix)PixelCount": "0"] }
        let count = Double(sampleCount)
        return [
            "\\(prefix)Status": "ok",
            "\\(prefix)PixelCount": String(sampleCount),
            "\\(prefix)InkRGB": String(format: "%.3f,%.3f,%.3f", redSum / count, greenSum / count, blueSum / count),
            "\\(prefix)BlueDominantFraction": String(format: "%.3f", Double(blueDominantCount) / count)
        ]
    }

    private func renderedInkDiagnostics(image: UIImage?, prefix: String) -> [String: String] {
"""
replace_exact(FEATURE, transparent_marker, transparent_replacement)

configure_marker = """    self.onToggleReasoning = onToggleReasoning
    self.onToggleToolDetail = onToggleToolDetail
    layoutMetrics = metrics
    messageLabel.isHighlighted = false
"""
configure_replacement = """    self.onToggleReasoning = onToggleReasoning
    self.onToggleToolDetail = onToggleToolDetail
    layoutMetrics = metrics
    lastConfiguredRoleForDiagnostics = message.role.rawValue
    messageLabel.isHighlighted = false
"""
replace_exact(FEATURE, configure_marker, configure_replacement)
