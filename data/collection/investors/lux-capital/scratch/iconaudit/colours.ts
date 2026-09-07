// How flat is the artwork? For each test image, list the colour bins (4 bits
// per channel) over pixels that deviate from the plate, as a share of them.
// A flat-filled logo puts nearly all its mass in one or two bins; a blurred or
// upscaled source spreads it across many.
import sharp from "sharp";

async function report(file: string) {
  const { data, info } = await sharp(file).ensureAlpha().raw()
    .toBuffer({ resolveWithObject: true });
  const { width: w, height: h, channels: c } = info;
  const lum = (r: number, g: number, b: number) => 0.2126 * r + 0.7152 * g + 0.0722 * b;
  const plateLum = 252 * 0.2126 + 252 * 0.7152 + 252 * 0.0722;
  const bins = new Map<number, number>();
  let cand = 0;
  const devs: number[] = [];
  for (let i = 0; i < w * h; i++) {
    const a = data[i * c + 3] / 255;
    const r = data[i * c] * a + 252 * (1 - a);
    const g = data[i * c + 1] * a + 252 * (1 - a);
    const b = data[i * c + 2] * a + 252 * (1 - a);
    devs.push(Math.abs(lum(r, g, b) - plateLum));
  }
  const sorted = [...devs].sort((x, y) => x - y);
  const full = Math.max(1, sorted[Math.floor(0.995 * sorted.length)]);
  for (let i = 0; i < w * h; i++) {
    if (devs[i] / full <= 0.15) continue;
    cand++;
    const a = data[i * c + 3] / 255;
    const r = data[i * c] * a + 252 * (1 - a);
    const g = data[i * c + 1] * a + 252 * (1 - a);
    const b = data[i * c + 2] * a + 252 * (1 - a);
    const key = ((r >> 4) << 8) | ((g >> 4) << 4) | (b >> 4);
    bins.set(key, (bins.get(key) || 0) + 1);
  }
  const top = [...bins.entries()].sort((a, b) => b[1] - a[1]).slice(0, 6);
  const share = (n: number) => ((100 * n) / cand).toFixed(1) + "%";
  const over = (p: number) => [...bins.values()].filter(n => n >= p * cand).length;
  console.log(`${file}`);
  console.log(`   candidates ${cand}  bins ${bins.size}  top: ${top.map(t => share(t[1])).join(" ")}`);
  console.log(`   bins over 1%: ${over(0.01)}   over 5%: ${over(0.05)}   over 10%: ${over(0.10)}`);
  const mass = (p: number) => share([...bins.values()].filter(n => n >= p * cand).reduce((s, n) => s + n, 0));
  console.log(`   mass in bins over 5%: ${mass(0.05)}   over 10%: ${mass(0.10)}`);
}

async function main() {
  for (const f of ["/tmp/lux-full-fixed.png", "/tmp/soft.png", "/tmp/upscaled.png"]) await report(f);
}
main();
