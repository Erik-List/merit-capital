export type TrackRecordTier = "1b" | "10b" | "100b";

// The filter is a single optional tier: null shows every investor, a tier
// keeps investors with at least one company currently worth that tier.
export type TrackRecordState = {
  tier: TrackRecordTier | null;
};

export const TRACK_RECORD_QUERY_KEY = "track-record";

export const TRACK_RECORD_TIERS: readonly TrackRecordTier[] = ["1b", "10b", "100b"];

export const TRACK_RECORD_TIER_LABELS: Record<TrackRecordTier, string> = {
  "1b": "$1B",
  "10b": "$10B",
  "100b": "$100B",
};

export const defaultTrackRecord: TrackRecordState = {
  tier: null,
};

export function parseTrackRecordParam(value: string | null): TrackRecordState {
  const normalized = (value ?? "").trim().toLowerCase();
  if (normalized === "1b" || normalized === "10b" || normalized === "100b") {
    return { tier: normalized };
  }
  return { ...defaultTrackRecord };
}

export function buildTrackRecordParam(state: TrackRecordState): string | null {
  return state.tier ?? null;
}

type TrackRecordBuckets = {
  one_b_companies?: { amount?: number | string | null } | null;
  ten_b_companies?: { amount?: number | string | null } | null;
  hundred_b_companies?: { amount?: number | string | null } | null;
  total_companies_invested?: number | string | null;
};

const TIER_KEY: Record<TrackRecordTier, keyof TrackRecordBuckets> = {
  "1b": "one_b_companies",
  "10b": "ten_b_companies",
  "100b": "hundred_b_companies",
};

export function computeTrackRecordHitRate(record: unknown, tier: TrackRecordTier) {
  const data = (record ?? {}) as TrackRecordBuckets;
  const bucketKey = TIER_KEY[tier];
  const bucket = data[bucketKey] ?? null;
  const totalRaw = data.total_companies_invested;

  const amountRaw = bucket && typeof bucket === "object" ? bucket.amount : null;
  const amount = normalizeCount(amountRaw);
  const total = normalizeCount(totalRaw);
  const safeAmount = Number.isFinite(amount) ? amount : 0;
  const safeTotal = Number.isFinite(total) ? total : 0;
  const percent = safeTotal > 0 ? (safeAmount / safeTotal) * 100 : 0;

  return {
    amount: safeAmount,
    total: safeTotal,
    percent,
  };
}

// "1 in 7" rounds, so the hover breakdown must carry the exact numbers.
export function oneInX(amount: number, total: number): number | null {
  if (amount <= 0 || total <= 0) return null;
  return Math.max(1, Math.round(total / amount));
}

function normalizeCount(value: unknown): number {
  if (typeof value === "number") {
    return Number.isFinite(value) ? value : 0;
  }
  if (typeof value === "string") {
    const parsed = Number.parseFloat(value);
    return Number.isFinite(parsed) ? parsed : 0;
  }
  return 0;
}
