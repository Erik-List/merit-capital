import Foundation
import Vision
import AppKit
let args = CommandLine.arguments
for path in args.dropFirst() {
    guard let img = NSImage(contentsOfFile: path), let tiff = img.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiff), let cg = rep.cgImage else { print("##FAIL \(path)"); continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = false
    let h = VNImageRequestHandler(cgImage: cg, options: [:])
    do { try h.perform([req]) } catch { print("##FAIL \(path)"); continue }
    print("##PAGE \(path)")
    for o in (req.results ?? []) { if let c = o.topCandidates(1).first { print(c.string) } }
}
