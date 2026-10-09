// Server-side loader for the investor page's "Investment Outcome by entry
// stage" table: per entry stage, how many companies the investor first
// invested in there and how many of them are valued at $1B, $10B and $100B or
// more, or are public, today. Read from the company rows, since the derived
// investor columns hold no per-stage outcome.

import { restFetchAll } from './postgrest';

export const OUTCOME_STAGES = ['Pre-Seed', 'Seed', 'Series A', 'Growth'] as const;

export type StageOutcome = {
  stage: (typeof OUTCOME_STAGES)[number];
  /** Companies first invested in at this stage. */
  entries: number;
  /** Of those, valued at $1B or more today (the bands nest: $100B+ is in all three). */
  oneB: number;
  tenB: number;
  hundredB: number;
  /** Of those, public today. */
  isPublic: number;
};

/** The counts of a StageOutcome without the stage: a total over all of them. */
export type OutcomeCounts = Omit<StageOutcome, 'stage'>;

export type InvestorOutcomes = {
  stages: StageOutcome[];
  /**
   * Every counted company, whether or not its entry round is on record, so
   * `all.entries` equals `companies` and matches the index's "All" count.
   */
  all: OutcomeCounts;
  /** Companies whose entry round is on record, over every company counted. */
  covered: number;
  companies: number;
};

type CompanyRow = {
  entry_stage: string;
  valuation_range: string;
  status: string;
};

const BAND_RANK: Record<string, number> = { below_1b: 0, '1b_plus': 1, '10b_plus': 2, '100b_plus': 3 };

export async function loadInvestorOutcomes(investorId: string): Promise<InvestorOutcomes> {
  const rows = await restFetchAll<CompanyRow>(
    `companies?select=entry_stage,valuation_range,status&investor_id=eq.${encodeURIComponent(investorId)}&order=id`,
  );

  const stages: StageOutcome[] = OUTCOME_STAGES.map((stage) => ({
    stage,
    entries: 0,
    oneB: 0,
    tenB: 0,
    hundredB: 0,
    isPublic: 0,
  }));
  const all: OutcomeCounts = { entries: 0, oneB: 0, tenB: 0, hundredB: 0, isPublic: 0 };
  let covered = 0;

  const tally = (outcome: OutcomeCounts, band: number, status: string) => {
    outcome.entries += 1;
    if (band >= 1) outcome.oneB += 1;
    if (band >= 2) outcome.tenB += 1;
    if (band >= 3) outcome.hundredB += 1;
    if (status === 'public') outcome.isPublic += 1;
  };

  rows.forEach((row) => {
    const band = BAND_RANK[row.valuation_range];
    // A company that could not be identified reads `undetermined` in the band
    // and is outside every metric, as in recompute_investor_metrics.
    if (band === undefined) return;
    tally(all, band, row.status);
    const outcome = stages.find((entry) => entry.stage === row.entry_stage);
    if (!outcome) return;
    covered += 1;
    tally(outcome, band, row.status);
  });

  return { stages, all, covered, companies: all.entries };
}
