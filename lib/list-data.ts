// Server-side loader for the investor index.
//
// The list recomputes every row for the filtered set of companies (entry
// stage, headquarters), so it needs the company rows and not only the
// derived investor columns. They are read in pages (lib/postgrest.ts) and
// packed into one compact payload the page fetches once.

import { REVALIDATE_SECONDS, restFetch, restFetchAll } from './postgrest';

export { REVALIDATE_SECONDS };

/** The investor columns a list row draws. */
export type ListInvestor = {
  id: string;
  slug: string;
  name: string;
  icon_url: string | null;
  investment_geo: unknown;
  investment_stage: unknown;
  investment_range: unknown;
  investment_scope: unknown;
};

/**
 * One number group per company, flattened: ROW_STRIDE numbers per company in
 * the order of the ROW_* offsets below.
 */
export type ListData = {
  investors: ListInvestor[];
  cities: string[];
  countries: string[];
  rows: number[];
};

export const ROW_STRIDE = 6;
export const ROW_INVESTOR = 0;
/** 0 Pre-Seed, 1 Seed, 2 Series A, 3 Growth, 4 entry round not on record. */
export const ROW_STAGE = 1;
/** Index into `cities`, -1 when the city is not on record. */
export const ROW_CITY = 2;
/** Index into `countries`, -1 when the country is not on record. */
export const ROW_COUNTRY = 3;
/** 0 below $1B, 1 $1B+, 2 $10B+, 3 $100B+. */
export const ROW_BAND = 4;
/** Seed entries only: 1 graduated, 2 not graduated, 3 too recent. 0 otherwise. */
export const ROW_GRADUATION = 5;

export const STAGE_UNKNOWN = 4;

const STAGE_CODE: Record<string, number> = { 'Pre-Seed': 0, Seed: 1, 'Series A': 2, Growth: 3 };
const BAND_CODE: Record<string, number> = { below_1b: 0, '1b_plus': 1, '10b_plus': 2, '100b_plus': 3 };
const GRADUATION_CODE: Record<string, number> = { graduated: 1, not_graduated: 2, censored: 3 };

type CompanyRow = {
  investor_id: string;
  entry_stage: string;
  hq_city: string | null;
  hq_country: string | null;
  valuation_range: string;
  seed_to_a_graduation: string | null;
};

const COMPANY_COLUMNS = 'investor_id,entry_stage,hq_city,hq_country,valuation_range,seed_to_a_graduation';
const INVESTOR_COLUMNS = 'id,slug,name,icon_url,investment_geo,investment_stage,investment_range,investment_scope';

export async function loadListData(): Promise<ListData> {
  const [investors, companies] = await Promise.all([
    restFetch(`investors?select=${INVESTOR_COLUMNS}&order=name`).then((r) => r.json() as Promise<ListInvestor[]>),
    restFetchAll<CompanyRow>(`companies?select=${COMPANY_COLUMNS}&order=id`),
  ]);

  const investorIndex = new Map(investors.map((investor, index) => [investor.id, index]));
  const cities: string[] = [];
  const cityIndex = new Map<string, number>();
  const countries: string[] = [];
  const countryIndex = new Map<string, number>();
  const intern = (value: string | null, list: string[], index: Map<string, number>): number => {
    const key = (value ?? '').trim();
    if (!key) return -1;
    let position = index.get(key);
    if (position === undefined) {
      position = list.length;
      list.push(key);
      index.set(key, position);
    }
    return position;
  };

  const rows: number[] = [];
  companies.forEach((company) => {
    const investor = investorIndex.get(company.investor_id);
    const band = BAND_CODE[company.valuation_range];
    // A company that could not be identified reads `undetermined` in the band
    // and is outside every metric (recompute_investor_metrics uses the same
    // basis).
    if (investor === undefined || band === undefined) return;
    rows.push(
      investor,
      STAGE_CODE[company.entry_stage] ?? STAGE_UNKNOWN,
      intern(company.hq_city, cities, cityIndex),
      intern(company.hq_country, countries, countryIndex),
      band,
      GRADUATION_CODE[company.seed_to_a_graduation ?? ''] ?? 0,
    );
  });

  return { investors, cities, countries, rows };
}
