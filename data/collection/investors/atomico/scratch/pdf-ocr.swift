// OCR a scanned PDF with macOS's own Vision framework (no third-party installs).
//
// Companies House serves pre-2016 annual returns and most paper-filed share
// allotments (SH01) as page images with no text layer. This renders each page
// with PDFKit and runs VNRecognizeTextRequest over it, printing the text page by
// page. Built in the Atomico run (PRO-79) for the UK register layer.
//
// Usage: swift pdf-ocr.swift <file.pdf> [max-pages]
import Foundation
import PDFKit
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count >= 2, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    FileHandle.standardError.write("usage: swift pdf-ocr.swift <file.pdf> [max-pages]\n".data(using: .utf8)!)
    exit(2)
}
let maxPages = args.count >= 3 ? (Int(args[2]) ?? doc.pageCount) : doc.pageCount

for i in 0..<min(doc.pageCount, maxPages) {
    guard let page = doc.page(at: i) else { continue }
    let bounds = page.bounds(for: .mediaBox)
    let scale: CGFloat = 2.5
    let size = NSSize(width: bounds.width * scale, height: bounds.height * scale)
    let image = NSImage(size: size)
    image.lockFocus()
    if let ctx = NSGraphicsContext.current?.cgContext {
        ctx.setFillColor(NSColor.white.cgColor)
        ctx.fill(CGRect(origin: .zero, size: size))
        ctx.scaleBy(x: scale, y: scale)
        page.draw(with: .mediaBox, to: ctx)
    }
    image.unlockFocus()
    guard let tiff = image.tiffRepresentation, let rep = NSBitmapImageRep(data: tiff),
          let cg = rep.cgImage else { continue }
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false
    let handler = VNImageRequestHandler(cgImage: cg, options: [:])
    try? handler.perform([request])
    let lines = (request.results ?? []).compactMap { $0.topCandidates(1).first?.string }
    print("=== page \(i + 1)")
    print(lines.joined(separator: "\n"))
}
