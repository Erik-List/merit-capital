// Build the two source defects MAX_RAMP exists to catch, from the Lux master:
//   soft.png     — a genuinely blurred source
//   upscaled.png — the Thrive trap: a 32px favicon enlarged 8x
// Both must still fail the ramp rule after the multi-ink change.
import sharp from "sharp";

const src = "/tmp/lux-full-fixed.png";

async function main() {
  await sharp(src).blur(2.5).toFile("/tmp/soft.png");
  // sharp applies only the LAST resize of a pipeline, so the shrink and the
  // enlargement must be two pipelines or the "upscaled" file is the original.
  await sharp(src).resize(32, 32, { kernel: "lanczos3" }).toFile("/tmp/tiny.png");
  await sharp("/tmp/tiny.png").resize(256, 256, { kernel: "lanczos3" })
    .toFile("/tmp/upscaled.png");
  console.log("wrote /tmp/soft.png and /tmp/upscaled.png");
}

main();
