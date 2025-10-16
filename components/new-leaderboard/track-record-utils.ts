export type TrackRecordTier = "1b" | "10b" | "100b";
export type TrackRecordSelection = "all" | "preset" | "custom";

export type TrackRecordState = {
  selection: TrackRecordSelection;
  tier: TrackRecordTier;
  percent: number;
};

export const TRACK_RECORD_QUERY_KEY = "track-record";

export const TRACK_RECORD_TIER_LABELS: Record<TrackRecordTier, string> = {
  "1b": "1B",
  "10b": "10B",
  "100b": "100B",
};

export const TRACK_RECORD_TIER_LONG_LABELS: Record<TrackRecordTier, string> = {
  "1b": "one billion dollar",
  "10b": "ten billion dollar",
  "100b": "hundred billion dollar",
};

export const TRACK_RECORD_TIER_NEGATIVE_LABELS: Record<TrackRecordTier, string> = {
  "1b": "No 1B company investment",
  "10b": "No 10B company investment",
  "100b": "No 100B company investment",
};

export const defaultTrackRecord: TrackRecordState = {
  selection: "all",
  tier: "1b",
  percent: 10,
};

export function clampTrackRecordPercent(value: number): number {
  if (!Number.isFinite(value)) return 10;
  return Math.min(100, Math.max(1, Math.round(value)));
}

export function parseTrackRecordParam(value: string | null): TrackRecordState {
  if (!value || value.toLowerCase() === "all") {
    return { ...defaultTrackRecord };
  }

  const match = value.toLowerCase().match(/^(1b|10b|100b)-(\d{1,3})percent$/);
  if (!match) {
    return { ...defaultTrackRecord };
  }

  const [, tierToken, percentToken] = match;
  const tier = tierToken as TrackRecordTier;
  const percent = clampTrackRecordPercent(Number.parseInt(percentToken, 10));
  const selection: TrackRecordSelection = tier === "1b" && percent === 10 ? "preset" : "custom";

  return {
    selection,
    tier,
    percent,
  };
}

export function buildTrackRecordParam(state: TrackRecordState): string | null {
  if (state.selection === "all") {
    return null;
  }
  const tier = state.tier ?? "1b";
  const percent = clampTrackRecordPercent(state.percent ?? 10);
  return `${tier}-${percent}percent`;
}

export function sanitizeTrackRecordState(value: TrackRecordState): TrackRecordState {
  const tier: TrackRecordTier = value.tier ?? "1b";
  const percent = clampTrackRecordPercent(value.percent ?? 10);

  if (value.selection === "all") {
    return {
      selection: "all",
      tier,
      percent,
    };
  }

  const selection: TrackRecordSelection = tier === "1b" && percent === 10 && value.selection !== "custom"
    ? "preset"
    : value.selection;

  return {
    selection,
    tier,
    percent,
  };
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

