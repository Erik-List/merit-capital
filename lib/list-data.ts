// Server-side loader for the investor list.
//
// The list recomputes every row for the filtered set of companies (entry
// stage, sector, headquarter), so it needs the company rows and not only the
// derived investor columns. PostgREST caps a response at 1,000 rows, so the
// rows are paged here, on the server, and packed into one compact payload the
// page fetches once. Every upstream page is cached for REVALIDATE_SECONDS.

import { FOCUS_VALUES } from './taxonomy';

export const REVALIDATE_SECONDS = 600;

const PAGE_SIZE = 1000;

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

export const ROW_STRIDE = 7;
export const ROW_INVESTOR = 0;
/** 0 Pre-Seed, 1 Seed, 2 Series A, 3 Growth, 4 entry round not on record. */
export const ROW_STAGE = 1;
/** Index into FOCUS_VALUES, -1 outside the taxonomy. */
export const ROW_FOCUS = 2;
/** Index into `cities`, -1 when the city is not on record. */
export const ROW_CITY = 3;
/** Index into `countries`, -1 when the country is not on record. */
export const ROW_COUNTRY = 4;
/** 0 below $1B, 1 $1B+, 2 $10B+, 3 $100B+. */
export const ROW_BAND = 5;
/** Seed entries only: 1 graduated, 2 not graduated, 3 too recent. 0 otherwise. */
export const ROW_GRADUATION = 6;

export const STAGE_UNKNOWN = 4;

const STAGE_CODE: Record<string, number> = { 'Pre-Seed': 0, Seed: 1, 'Series A': 2, Growth: 3 };
const BAND_CODE: Record<string, number> = { below_1b: 0, '1b_plus': 1, '10b_plus': 2, '100b_plus': 3 };
const GRADUATION_CODE: Record<string, number> = { graduated: 1, not_graduated: 2, censored: 3 };

type CompanyRow = {
  investor_id: string;
  entry_stage: string;
  focus: string | null;
  hq_city: string | null;
  hq_country: string | null;
  valuation_range: string;
  seed_to_a_graduation: string | null;
};

const COMPANY_COLUMNS = 'investor_id,entry_stage,focus,hq_city,hq_country,valuation_range,seed_to_a_graduation';
const INVESTOR_COLUMNS = 'id,slug,name,icon_url,investment_geo,investment_stage,investment_range,investment_scope';

async function restFetch(path: string, prefer?: string): Promise<Response> {
  const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;
  const headers: Record<string, string> = { apikey: anonKey, Authorization: `Bearer ${anonKey}` };
  if (prefer) headers.Prefer = prefer;
  const response = await fetch(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest/v1/${path}`, {
    headers,
    next: { revalidate: REVALIDATE_SECONDS },
  });
  if (!response.ok) {
    throw new Error(`list data: ${path.split('?')[0]} answered ${response.status}`);
  }
  return response;
}

const companiesPath = (offset: number) =>
  `companies?select=${COMPANY_COLUMNS}&order=id&limit=${PAGE_SIZE}&offset=${offset}`;

async function loadCompanies(): Promise<CompanyRow[]> {
  // The first page carries the exact total in Content-Range ("0-999/24236"),
  // which sizes the remaining pages.
  const first = await restFetch(companiesPath(0), 'count=exact');
  const total = Number((first.headers.get('content-range') ?? '').split('/')[1]);
  const firstRows = (await first.json()) as CompanyRow[];
  if (!Number.isFinite(total)) {
    throw new Error('list data: companies answered without a total');
  }

  const offsets: number[] = [];
  for (let offset = PAGE_SIZE; offset < total; offset += PAGE_SIZE) offsets.push(offset);
  const rest = await Promise.all(
    offsets.map(async (offset) => (await restFetch(companiesPath(offset))).json() as Promise<CompanyRow[]>),
  );

  const rows = firstRows.concat(...rest);
  // A page that came back short would silently drop companies from every
  // count on the list; refuse instead of publishing a partial book.
  if (rows.length !== total) {
    throw new Error(`list data: read ${rows.length} of ${total} companies`);
  }
  return rows;
}

export async function loadListData(): Promise<ListData> {
  const [investors, companies] = await Promise.all([
    restFetch(`investors?select=${INVESTOR_COLUMNS}&order=name`).then((r) => r.json() as Promise<ListInvestor[]>),
    loadCompanies(),
  ]);

  const investorIndex = new Map(investors.map((investor, index) => [investor.id, index]));
  const focusIndex = new Map(FOCUS_VALUES.map((focus, index) => [focus, index]));
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
      company.focus === null ? -1 : focusIndex.get(company.focus) ?? -1,
      intern(company.hq_city, cities, cityIndex),
      intern(company.hq_country, countries, countryIndex),
      band,
      GRADUATION_CODE[company.seed_to_a_graduation ?? ''] ?? 0,
    );
  });

  return { investors, cities, countries, rows };
}
