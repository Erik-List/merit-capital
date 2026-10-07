// The date the pages give their values: the last ingestion of company rows.
// Every companies ingest stamps all rows of the investor's book with one
// clock value (scripts/ingest-companies.ts), so the newest `updated_at` is
// the last ingestion; of one investor, or of any investor when none is named
// (Erik, 2026-10-01).

import { restFetch } from './postgrest';

export async function loadLastIngest(investorId?: string): Promise<string | null> {
  const filter = investorId ? `&investor_id=eq.${encodeURIComponent(investorId)}` : '';
  const response = await restFetch(`companies?select=updated_at&order=updated_at.desc&limit=1${filter}`);
  const rows = (await response.json()) as Array<{ updated_at: string }>;
  return rows[0]?.updated_at ?? null;
}
