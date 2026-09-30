// The investor list's arithmetic: which companies are in the filtered set,
// what each investor's counts are per entry stage, and in which order the
// investors are listed. Pure functions over the packed payload of
// lib/list-data.ts, so the desktop list and the phone list cannot disagree.

import { FOCUS_VALUES } from "@/lib/taxonomy";
import { HQ_OPTIONS, hqOption } from "@/lib/company-geo";
import {
  ROW_BAND,
  ROW_CITY,
  ROW_COUNTRY,
  ROW_FOCUS,
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
  /** Index into FOCUS_VALUES, null for all sectors. */
  sector: number | null;
  /** Headquarter option slugs; a company matches when any of them holds it. */
  hq: string[];
};

/**
 * The valuation each entry stage is measured against: a company counts when
 * it is valued at the mark or more today. `barFull` is the share at which the
 * bar is full.
 */
export const STAGE_MARK: ReadonlyArray<{ band: number; label: string; barFull: number }> = [
  { band: 1, label: "$1B", barFull: 0.5 },
  { band: 1, label: "$1B", barFull: 0.5 },
  { band: 1, label: "$1B", barFull: 0.5 },
  { band: 2, label: "$10B", barFull: 0.25 },
];

/** Entries at a stage before an investor is ordered by its share there. */
export const ORDER_FLOOR = 20;
/** Entries at a stage before a share is drawn; under it the count stands alone. */
export const SHARE_FLOOR = 10;

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
    if (filters.sector !== null && data.rows[at + ROW_FOCUS] !== filters.sector) continue;
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
  /** Investors with enough entries to be ordered by their share. */
  groups: ListGroup[];
  /** Investors under the floor, ordered by their number of companies. */
  rest: InvestorStats[];
  restTitle: string;
  /** Investors with no company in the filtered set, named in one closing line. */
  gone: InvestorStats[];
  goneTitle: string;
};

const byName = (a: InvestorStats, b: InvestorStats) => a.investor.name.localeCompare(b.investor.name);

const share = (row: InvestorStats, stage: StageIndex) => row.stages[stage].atMark / row.stages[stage].entries;

/**
 * The order of the list.
 *
 * With an entry stage picked: one list, by share at that stage. With no stage
 * picked: each investor under the stage it invests at most, by its share
 * there, so seed investors are compared with seed investors and growth
 * investors with growth investors. Either way an investor is ordered by share
 * only from ORDER_FLOOR entries; under it the order is the number of companies
 * in the filtered set, and investors with none are named, not listed.
 */
export function rank(stats: InvestorStats[], filters: Filters): Ranking {
  const narrowed = filters.sector !== null || filters.hq.length > 0;
  const where = narrowed ? " in the filtered set" : "";

  const split = (pool: InvestorStats[], stage: StageIndex, count: (row: InvestorStats) => number) => {
    const top = pool
      .filter((row) => row.stages[stage].entries >= ORDER_FLOOR)
      .sort(
        (a, b) => share(b, stage) - share(a, stage) || b.stages[stage].entries - a.stages[stage].entries || byName(a, b),
      );
    const low = pool.filter((row) => row.stages[stage].entries < ORDER_FLOOR);
    return {
      top,
      rest: low.filter((row) => count(row) > 0).sort((a, b) => count(b) - count(a) || byName(a, b)),
      gone: low.filter((row) => count(row) === 0).sort(byName),
    };
  };

  if (filters.stage !== null) {
    const stage = filters.stage;
    const label = STAGE_LABELS[stage];
    const result = split(stats, stage, (row) => row.stages[stage].entries);
    return {
      groups: [{ title: null, rows: result.top }],
      rest: result.rest,
      restTitle: `Fewer than ${ORDER_FLOOR} ${label} entries, ordered by number of entries`,
      gone: result.gone,
      goneTitle: `no ${label} entries${where}`,
    };
  }

  const groups: ListGroup[] = [];
  const rest: InvestorStats[] = [];
  const gone: InvestorStats[] = [];
  STAGE_INDEXES.forEach((stage) => {
    const result = split(
      stats.filter((row) => row.mainStage === stage),
      stage,
      (row) => row.companies,
    );
    if (result.top.length > 0) groups.push({ title: `Invests mostly at ${STAGE_LABELS[stage]}`, rows: result.top });
    rest.push(...result.rest);
    gone.push(...result.gone);
  });
  return {
    groups,
    rest: rest.sort((a, b) => b.companies - a.companies || byName(a, b)),
    restTitle: `Fewer than ${ORDER_FLOOR} entries at the main stage, ordered by number of companies`,
    gone: gone.sort(byName),
    goneTitle: `no companies${where}`,
  };
}

/** "Seed investments · Fintech & Payments · Berlin or Munich". */
export function filteredSetLabel(filters: Filters): string {
  const parts: string[] = [];
  parts.push(filters.stage === null ? "All entry stages" : `${STAGE_LABELS[filters.stage]} entries`);
  if (filters.sector !== null) parts.push(FOCUS_VALUES[filters.sector]);
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
