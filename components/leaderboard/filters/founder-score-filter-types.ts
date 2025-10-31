export type FounderScoreCategory = "speed" | "processQuality" | "passiveSupport" | "activeSupport";

export type FounderScoreFilterState =
  | { mode: "all" }
  | { mode: "top10" }
  | { mode: "categories"; selected: FounderScoreCategory[] };

export const FOUNDER_SCORE_QUERY_KEY = "founder-score";

export const ALL_FOUNDER_SCORE_CATEGORIES: readonly FounderScoreCategory[] = [
  "speed",
  "processQuality",
  "passiveSupport",
  "activeSupport",
] as const;

export function isCategoriesFounderState(
  state: FounderScoreFilterState,
): state is Extract<FounderScoreFilterState, { mode: "categories"; selected: FounderScoreCategory[] }> {
  return state.mode === "categories";
}

export function normalizeFounderCategories(
  selected: readonly FounderScoreCategory[] | undefined,
): FounderScoreCategory[] {
  if (!Array.isArray(selected)) {
    return [ALL_FOUNDER_SCORE_CATEGORIES[0]];
  }
  const validSet = new Set<FounderScoreCategory>();
  selected.forEach((category) => {
    if ((ALL_FOUNDER_SCORE_CATEGORIES as readonly string[]).includes(category)) {
      validSet.add(category as FounderScoreCategory);
    }
  });
  const normalized = ALL_FOUNDER_SCORE_CATEGORIES.filter((category) => validSet.has(category));
  if (normalized.length === 0) {
    return [ALL_FOUNDER_SCORE_CATEGORIES[0]];
  }
  return [normalized[0]];
}

