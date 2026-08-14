// SF Bay Area municipalities across the nine counties, spelled exactly as
// companies.hq_city stores them (bare municipality, no state suffix).
//
// Display-only rollup: the derived company_geo_distribution stays per-city
// and the recompute trigger never sees this list; investor-details.tsx folds
// matching city entries into one "SF Bay Area" element at render. A Bay Area
// municipality missing from this list renders as its own entry until added.
export const BAY_AREA_LABEL = 'SF Bay Area';

export const BAY_AREA_CITIES: ReadonlySet<string> = new Set([
  // San Francisco
  'San Francisco',
  // San Mateo
  'Atherton',
  'Belmont',
  'Brisbane',
  'Burlingame',
  'Daly City',
  'East Palo Alto',
  'Foster City',
  'Half Moon Bay',
  'Menlo Park',
  'Millbrae',
  'Pacifica',
  'Redwood City',
  'San Bruno',
  'San Carlos',
  'San Mateo',
  'South San Francisco',
  'Woodside',
  // Santa Clara
  'Campbell',
  'Cupertino',
  'Gilroy',
  'Los Altos',
  'Los Altos Hills',
  'Los Gatos',
  'Milpitas',
  'Morgan Hill',
  'Mountain View',
  'Palo Alto',
  'San Jose',
  'Santa Clara',
  'Saratoga',
  'Sunnyvale',
  // Alameda
  'Alameda',
  'Berkeley',
  'Dublin',
  'Emeryville',
  'Fremont',
  'Hayward',
  'Livermore',
  'Newark',
  'Oakland',
  'Pleasanton',
  'San Leandro',
  'Union City',
  // Contra Costa
  'Concord',
  'Danville',
  'Lafayette',
  'Richmond',
  'San Ramon',
  'Walnut Creek',
  // Marin
  'Larkspur',
  'Mill Valley',
  'Novato',
  'San Rafael',
  'Sausalito',
  // Sonoma
  'Petaluma',
  'Santa Rosa',
  // Napa
  'Napa',
  // Solano
  'Benicia',
  'Fairfield',
  'Vallejo',
]);
