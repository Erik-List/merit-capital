// The investor index's arithmetic: which companies are in the filtered set,
// what each investor's counts are per entry stage, and in which order the
// investors are listed. Pure functions over the packed payload of
// lib/list-data.ts, so the desktop list and the phone list cannot disagree.

import { HQ_OPTIONS, hqOption } from "@/lib/company-geo";
import {
  ROW_BAND,
  ROW_CITY,
  ROW_COUNTRY,
  ROW_GRADUATION,
  ROW_INVESTOR,
  ROW_STAGE,
  ROW_STRIDE,
  STAGE_UNKNOWN,
  type ListData,
  type ListInvestor,
} from "@/lib/list-data";

export const STAGE_LABELS = ["Pre-Seed", "Seed", "Series A", "Growth"] as const;

/** 0 Pre-Seed, 1 Seed, 2 Series A, 3 Growth. */
export type StageIndex = 0 | 1 | 2 | 3;
const STAGE_INDEXES: readonly StageIndex[] = [0, 1, 2, 3];

/** The entry stage filter: one stage, or null for all stages. */
export type StageFilter = StageIndex | null;

/** The list opens on Seed (Erik, 2026-09-30). */
export const DEFAULT_STAGE: StageFilter = 1;

export type Filters = {
  stage: StageFilter;
  /** Headquarter option slugs; a company matches when any of them holds it. */
  hq: string[];
};

/**
 * The valuation each entry stage is measured against: a company counts when
 * it is valued at the mark or more today.
 */
export const STAGE_MARK: ReadonlyArray<{ band: number; label: string }> = [
  { band: 1, label: "$1B" },
  { band: 1, label: "$1B" },
  { band: 1, label: "$1B" },
  { band: 2, label: "$10B" },
];

/**
 * Entries at a stage before a share is drawn and the investor is ordered by
 * it; under the floor the count stands alone. One floor for both (Erik,
 * 2026-10-08), so a share that is printed is always the one the order uses.
 */
export const SHARE_FLOOR = 20;

export type StageCount = {
  /** Companies the investor entered at this stage, inside the filtered set. */
  entries: number;
  /** Of those, the ones valued at the stage's mark or more today. */
  atMark: number;
};

export type InvestorStats = {
  investor: ListInvestor;
  stages: [StageCount, StageCount, StageCount, StageCount];
  /** Companies in the filtered set whose entry round is on record. */
  companies: number;
  /** The stage the investor entered most companies at, over its whole book. */
  mainStage: StageIndex;
  /** Seed entries in the filtered set: the graduation cohort and its outcome. */
  seed: { graduated: number; cohort: number; tooRecent: number };
};

export type ListIndex = {
  data: ListData;
  /** Per headquarter option slug: the city and country indexes it holds. */
  places: Map<string, { cities: Set<number> | null; countries: Set<number> }>;
  mainStage: StageIndex[];
};

export function buildIndex(data: ListData): ListIndex {
  const cityIndex = new Map(data.cities.map((city, index) => [city, index]));
  const countryIndex = new Map(data.countries.map((country, index) => [country, index]));
  const pick = (values: readonly string[], index: Map<string, number>): Set<number> => {
    const found = new Set<number>();
    values.forEach((value) => {
      const position = index.get(value);
      if (position !== undefined) found.add(position);
    });
    return found;
  };

  const places: ListIndex["places"] = new Map();
  HQ_OPTIONS.forEach((option) => {
    places.set(option.slug, {
      cities: option.cities ? pick(option.cities, cityIndex) : null,
      countries: pick(option.countries, countryIndex),
    });
  });

  const entries = data.investors.map(() => [0, 0, 0, 0]);
  for (let at = 0; at < data.rows.length; at += ROW_STRIDE) {
    const stage = data.rows[at + ROW_STAGE];
    if (stage !== STAGE_UNKNOWN) entries[data.rows[at + ROW_INVESTOR]][stage] += 1;
  }
  const mainStage = entries.map((counts) =>
    STAGE_INDEXES.reduce<StageIndex>((best, stage) => (counts[stage] > counts[best] ? stage : best), 0),
  );

  return { data, places, mainStage };
}

/** Counts per investor and entry stage inside the filtered set. */
export function computeStats(index: ListIndex, filters: Filters): InvestorStats[] {
  const { data } = index;
  const stats: InvestorStats[] = data.investors.map((investor, position) => ({
    investor,
    stages: [
      { entries: 0, atMark: 0 },
      { entries: 0, atMark: 0 },
      { entries: 0, atMark: 0 },
      { entries: 0, atMark: 0 },
    ],
    companies: 0,
    mainStage: index.mainStage[position],
    seed: { graduated: 0, cohort: 0, tooRecent: 0 },
  }));

  const selected = filters.hq
    .map((slug) => index.places.get(slug))
    .filter((place): place is NonNullable<typeof place> => place !== undefined);

  for (let at = 0; at < data.rows.length; at += ROW_STRIDE) {
    const stage = data.rows[at + ROW_STAGE];
    // A company whose entry round is not on record belongs to no stage; it is
    // left out so that a share always matches the count printed under it.
    if (stage === STAGE_UNKNOWN) continue;
    if (selected.length > 0) {
      const city = data.rows[at + ROW_CITY];
      const country = data.rows[at + ROW_COUNTRY];
      const held = selected.some(
        (place) => place.countries.has(country) && (place.cities === null || place.cities.has(city)),
      );
      if (!held) continue;
    }

    const row = stats[data.rows[at + ROW_INVESTOR]];
    const count = row.stages[stage];
    row.companies += 1;
    count.entries += 1;
    if (data.rows[at + ROW_BAND] >= STAGE_MARK[stage].band) count.atMark += 1;
    if (stage === 1) {
      const graduation = data.rows[at + ROW_GRADUATION];
      if (graduation === 1) {
        row.seed.graduated += 1;
        row.seed.cohort += 1;
      } else if (graduation === 2) {
        row.seed.cohort += 1;
      } else if (graduation === 3) {
        row.seed.tooRecent += 1;
      }
    }
  }

  return stats;
}

export type ListGroup = {
  /** Set when the list is split by main stage; null for a single ordered list. */
  title: string | null;
  rows: InvestorStats[];
};

export type Ranking = {
  /** Investors ordered by their share: enough entries, and a company at the mark. */
  groups: ListGroup[];
  /**
   * The parts under the ordered list, each under its own divider: investors
   * under the floor that have a company at the mark, then investors with none.
   */
  tail: Array<{ title: string; rows: InvestorStats[] }>;
  /** Investors with no company in the filtered set, named in one closing line. */
  gone: InvestorStats[];
  goneTitle: string;
};

const byName = (a: InvestorStats, b: InvestorStats) => a.investor.name.localeCompare(b.investor.name);

/**
 * The order of the list.
 *
 * Each investor is measured at one stage: the picked entry stage, or, with no
 * stage picked, the stage it invests at most, so seed investors are compared
 * with seed investors and growth investors with growth investors. The list
 * then has three parts, and an investor with a company at the mark is never
 * listed under one with none (Erik, 2026-10-08):
 *
 * 1. SHARE_FLOOR entries or more and a company at the mark: by share.
 * 2. Under the floor with a company at the mark: by companies at the mark.
 * 3. No company at the mark: by number of entries.
 *
 * Investors with nothing in the filtered set are named, not listed.
 */
export function rank(stats: InvestorStats[], filters: Filters): Ranking {
  const picked = filters.stage;
  const where = filters.hq.length > 0 ? " in the filtered set" : "";

  const at = (row: InvestorStats) => row.stages[picked ?? row.mainStage];
  // What an investor has in the filtered set: entries at the picked stage,
  // or, with no stage picked, companies at any stage.
  const size = (row: InvestorStats) => (picked !== null ? row.stages[picked].entries : row.companies);

  const byShare = (a: InvestorStats, b: InvestorStats) =>
    at(b).atMark / at(b).entries - at(a).atMark / at(a).entries || at(b).entries - at(a).entries || byName(a, b);

  const hit = stats.filter((row) => at(row).atMark > 0);
  const miss = stats.filter((row) => at(row).atMark === 0);
  const ordered = hit.filter((row) => at(row).entries >= SHARE_FLOOR);
  const few = hit
    .filter((row) => at(row).entries < SHARE_FLOOR)
    .sort((a, b) => at(b).atMark - at(a).atMark || at(b).entries - at(a).entries || byName(a, b));
  const none = miss.filter((row) => size(row) > 0).sort((a, b) => size(b) - size(a) || byName(a, b));
  const gone = miss.filter((row) => size(row) === 0).sort(byName);

  if (picked !== null) {
    const label = STAGE_LABELS[picked];
    return {
      groups: [{ title: null, rows: ordered.sort(byShare) }],
      tail: [
        { title: `Fewer than ${SHARE_FLOOR} ${label} entries`, rows: few },
        { title: `No ${label} entry valued at ${STAGE_MARK[picked].label}+ today`, rows: none },
      ],
      gone,
      goneTitle: `no ${label} entries${where}`,
    };
  }

  return {
    groups: STAGE_INDEXES.map((stage) => ({
      title: `Invests mostly at ${STAGE_LABELS[stage]}`,
      rows: ordered.filter((row) => row.mainStage === stage).sort(byShare),
    })).filter((group) => group.rows.length > 0),
    tail: [
      { title: `Fewer than ${SHARE_FLOOR} entries at the main stage`, rows: few },
      {
        title: `No entry at the main stage valued at ${STAGE_MARK[0].label}+ today (${STAGE_MARK[3].label}+ for Growth)`,
        rows: none,
      },
    ],
    gone,
    goneTitle: `no companies${where}`,
  };
}

/** "Seed entries · Berlin or Munich". */
export function filteredSetLabel(filters: Filters): string {
  const parts: string[] = [];
  parts.push(filters.stage === null ? "All entry stages" : `${STAGE_LABELS[filters.stage]} entries`);
  if (filters.hq.length > 0) {
    parts.push(
      filters.hq
        .map((slug) => hqOption(slug)?.label)
        .filter((label): label is string => Boolean(label))
        .join(" or "),
    );
  }
  return parts.join(" · ");
}

/** 25.7 -> "25.7%", 8 -> "8%". */
export function formatShare(part: number, whole: number): string {
  if (whole <= 0) return "0%";
  const rounded = Math.round((part / whole) * 1000) / 10;
  return `${rounded % 1 === 0 ? rounded.toFixed(0) : rounded.toFixed(1)}%`;
}
