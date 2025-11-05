import fs from "node:fs";
import path from "node:path";

const CACHE_DIR = path.resolve(process.cwd(), "scripts", "cache");

export function ensureCacheDir(category: string): string {
  const dir = path.join(CACHE_DIR, category);
  fs.mkdirSync(dir, { recursive: true });
  return dir;
}

export function getCachePath(category: string, slug: string): string {
  const dir = ensureCacheDir(category);
  return path.join(dir, `${slug}.json`);
}

export function readCache<T>(category: string, slug: string): T | null {
  try {
    const filePath = getCachePath(category, slug);
    if (!fs.existsSync(filePath)) return null;
    const content = fs.readFileSync(filePath, "utf-8");
    return JSON.parse(content) as T;
  } catch (error) {
    console.warn(`Failed to read cache for ${category}/${slug}:`, error);
    return null;
  }
}

export function writeCache<T>(category: string, slug: string, data: T): void {
  try {
    const filePath = getCachePath(category, slug);
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2) + "\n", "utf-8");
  } catch (error) {
    console.error(`Failed to write cache for ${category}/${slug}:`, error);
    throw error;
  }
}

export function cacheExists(category: string, slug: string): boolean {
  return fs.existsSync(getCachePath(category, slug));
}

export function readBatchCache<T>(
  category: string,
  slugs: string[]
): Map<string, T> {
  const results = new Map<string, T>();
  for (const slug of slugs) {
    const cached = readCache<T>(category, slug);
    if (cached) results.set(slug, cached);
  }
  return results;
}

export function writeBatchCache<T>(
  category: string,
  data: Map<string, T> | Record<string, T>
): void {
  const entries = data instanceof Map ? Array.from(data.entries()) : Object.entries(data);
  for (const [slug, value] of entries) {
    writeCache(category, slug, value);
  }
}

