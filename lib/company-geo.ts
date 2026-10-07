// Headquarter options for the investor index: one mixed list of cities and
// metros, countries and regions, matched against companies.hq_city and
// companies.hq_country.
//
// companies.hq_city stores the bare municipality (COLLECTION.md §6), so a
// metro is a list of municipalities inside one country: the country keeps
// Cambridge, Massachusetts apart from Cambridge, England, and the list absorbs
// spelling variants (Bangalore / Bengaluru, Tel Aviv / Tel Aviv-Yafo). A
// company without a city never matches a metro; it still matches its country
// and region.
//
// Order is the order of the filter: PRIMARY options are always shown, the
// rest sit under "Show more locations" in three groups. The metros under the
// fold are ordered by relevance for the venture ecosystem, a judged order and
// not a company count (Erik, 2026-09-30).

import { BAY_AREA_CITIES, BAY_AREA_LABEL } from './geo';

export type HqKind = 'metro' | 'country' | 'region';

export type HqOption = {
  /** URL token, stable across label changes. */
  slug: string;
  label: string;
  kind: HqKind;
  /** Shown without expanding the list. */
  primary: boolean;
  /** ISO 3166-1 alpha-2 codes. A metro has exactly one. */
  countries: readonly string[];
  /** Municipalities as companies.hq_city spells them. Metros only. */
  cities?: readonly string[];
};

const metro = (slug: string, label: string, country: string, cities: readonly string[], primary = false): HqOption => ({
  slug,
  label,
  kind: 'metro',
  primary,
  countries: [country],
  cities,
});

const country = (slug: string, label: string, code: string): HqOption => ({
  slug,
  label,
  kind: 'country',
  primary: false,
  countries: [code],
});

const region = (slug: string, label: string, codes: readonly string[], primary = false): HqOption => ({
  slug,
  label,
  kind: 'region',
  primary,
  countries: codes,
});

const EUROPE = [
  'GB', 'DE', 'FR', 'SE', 'NL', 'ES', 'IT', 'CH', 'DK', 'NO', 'FI', 'IE', 'BE', 'AT', 'PT', 'PL', 'EE', 'LT',
  'LV', 'CZ', 'RO', 'HU', 'GR', 'LU', 'IS', 'BG', 'HR', 'SI', 'SK', 'UA', 'CY', 'MT', 'RS', 'TR',
] as const;

export const HQ_OPTIONS: readonly HqOption[] = [
  // Always shown.
  region('europe', 'Europe', EUROPE, true),
  metro('sf-bay-area', BAY_AREA_LABEL, 'US', Array.from(BAY_AREA_CITIES), true),
  metro('new-york', 'New York', 'US', ['New York', 'Brooklyn', 'Jersey City', 'Hoboken', 'Long Island City'], true),
  metro('london', 'London', 'GB', ['London'], true),
  metro('stockholm', 'Stockholm', 'SE', ['Stockholm'], true),
  metro('munich', 'Munich', 'DE', ['Munich', 'München'], true),

  // Cities and metros, by relevance for the venture ecosystem.
  metro('los-angeles', 'Los Angeles', 'US', [
    'Los Angeles', 'Santa Monica', 'Culver City', 'El Segundo', 'Venice', 'Pasadena', 'Burbank', 'Beverly Hills',
    'West Hollywood', 'Playa Vista', 'Marina del Rey', 'Long Beach', 'Torrance', 'Hawthorne', 'Glendale',
  ]),
  metro('berlin', 'Berlin', 'DE', ['Berlin']),
  metro('paris', 'Paris', 'FR', ['Paris']),
  metro('tel-aviv', 'Tel Aviv', 'IL', [
    'Tel Aviv', 'Tel Aviv-Yafo', 'Herzliya', 'Ramat Gan', 'Petah Tikva', 'Givatayim', 'Bnei Brak',
  ]),
  metro('boston', 'Boston', 'US', ['Boston', 'Cambridge', 'Somerville', 'Waltham', 'Watertown', 'Woburn', 'Needham']),
  metro('bangalore', 'Bangalore', 'IN', ['Bangalore', 'Bengaluru']),
  metro('singapore', 'Singapore', 'SG', ['Singapore']),
  metro('seattle', 'Seattle', 'US', ['Seattle', 'Bellevue', 'Redmond', 'Kirkland']),
  metro('austin', 'Austin', 'US', ['Austin']),
  metro('amsterdam', 'Amsterdam', 'NL', ['Amsterdam']),
  metro('toronto', 'Toronto', 'CA', ['Toronto']),
  metro('washington-dc', 'Washington DC', 'US', ['Washington', 'Arlington', 'McLean', 'Reston', 'Bethesda']),
  metro('chicago', 'Chicago', 'US', ['Chicago']),
  metro('san-diego', 'San Diego', 'US', ['San Diego', 'La Jolla', 'Carlsbad']),
  metro('denver', 'Denver', 'US', ['Denver', 'Boulder']),
  metro('atlanta', 'Atlanta', 'US', ['Atlanta']),

  // Countries.
  country('united-states', 'United States', 'US'),
  country('united-kingdom', 'United Kingdom', 'GB'),
  country('germany', 'Germany', 'DE'),
  country('india', 'India', 'IN'),
  country('israel', 'Israel', 'IL'),
  country('canada', 'Canada', 'CA'),
  country('france', 'France', 'FR'),
  country('sweden', 'Sweden', 'SE'),
  country('mexico', 'Mexico', 'MX'),
  country('china', 'China', 'CN'),
  country('netherlands', 'Netherlands', 'NL'),
  country('spain', 'Spain', 'ES'),
  country('brazil', 'Brazil', 'BR'),
  country('australia', 'Australia', 'AU'),
  country('finland', 'Finland', 'FI'),
  country('denmark', 'Denmark', 'DK'),
  country('switzerland', 'Switzerland', 'CH'),
  country('japan', 'Japan', 'JP'),

  // Regions.
  region('dach', 'DACH', ['DE', 'AT', 'CH']),
  region('nordics', 'Nordics', ['SE', 'DK', 'NO', 'FI', 'IS']),
  region('middle-east', 'Middle East', ['IL', 'AE', 'SA', 'QA', 'BH', 'KW', 'JO', 'TR', 'EG']),
  region('asia', 'Asia', ['IN', 'CN', 'HK', 'JP', 'KR', 'SG', 'ID', 'VN', 'TH', 'MY', 'PH', 'PK', 'BD', 'TW']),
  region('latin-america', 'Latin America', ['MX', 'BR', 'AR', 'CO', 'CL', 'PE', 'UY', 'EC']),
  region('southeast-asia', 'Southeast Asia', ['SG', 'ID', 'VN', 'TH', 'MY', 'PH']),
  region('africa', 'Africa', ['NG', 'KE', 'ZA', 'EG', 'GH', 'MA', 'TN', 'RW', 'UG', 'TZ', 'SN', 'CI', 'ET']),
];

const HQ_BY_SLUG = new Map(HQ_OPTIONS.map((option) => [option.slug, option]));

export function hqOption(slug: string): HqOption | null {
  return HQ_BY_SLUG.get(slug) ?? null;
}

/** The groups under "Show more locations", in display order. */
export const HQ_MORE_GROUPS: ReadonlyArray<{ kind: HqKind; label: string }> = [
  { kind: 'metro', label: 'Cities and metros' },
  { kind: 'country', label: 'Countries' },
  { kind: 'region', label: 'Regions' },
];
