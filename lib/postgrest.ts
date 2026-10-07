// Server-side reads of the public PostgREST surface. PostgREST caps a
// response at 1,000 rows, so a table read is paged here and refused when a
// page comes back short: a silent gap would drop companies from every count
// drawn on the page. Every upstream page is cached for REVALIDATE_SECONDS.

export const REVALIDATE_SECONDS = 600;

export const PAGE_SIZE = 1000;

/** `fresh` reads past the cache, for a second try after a failed read. */
export async function restFetch(path: string, prefer?: string, fresh = false): Promise<Response> {
  const anonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;
  const headers: Record<string, string> = { apikey: anonKey, Authorization: `Bearer ${anonKey}` };
  if (prefer) headers.Prefer = prefer;
  const response = await fetch(`${process.env.NEXT_PUBLIC_SUPABASE_URL}/rest/v1/${path}`, {
    headers,
    ...(fresh ? { cache: 'no-store' as const } : { next: { revalidate: REVALIDATE_SECONDS } }),
  });
  if (!response.ok) {
    throw new Error(`${path.split('?')[0]} answered ${response.status}`);
  }
  return response;
}

/**
 * Every row of a query, read in pages of PAGE_SIZE. `path` is the query
 * without limit and offset; it must carry an `order` so the pages tile.
 *
 * The pages are cached one by one, so after an ingest they can be of
 * different ages for a moment: the first page carries the new total while a
 * later page still holds the old rows, and the count does not add up. A read
 * that fails is therefore tried once more past the cache before it is refused.
 */
export async function restFetchAll<T>(path: string): Promise<T[]> {
  try {
    return await readAll<T>(path, false);
  } catch (error) {
    console.warn(`${path.split('?')[0]}: cached read failed, reading again past the cache`, error);
    return readAll<T>(path, true);
  }
}

async function readAll<T>(path: string, fresh: boolean): Promise<T[]> {
  const page = (offset: number) => `${path}&limit=${PAGE_SIZE}&offset=${offset}`;

  // The first page carries the exact total in Content-Range ("0-999/24236"),
  // which sizes the remaining pages.
  const first = await restFetch(page(0), 'count=exact', fresh);
  const total = Number((first.headers.get('content-range') ?? '').split('/')[1]);
  const firstRows = (await first.json()) as T[];
  if (!Number.isFinite(total)) {
    throw new Error(`${path.split('?')[0]} answered without a total`);
  }

  const offsets: number[] = [];
  for (let offset = PAGE_SIZE; offset < total; offset += PAGE_SIZE) offsets.push(offset);
  const rest = await Promise.all(
    offsets.map(async (offset) => (await restFetch(page(offset), undefined, fresh)).json() as Promise<T[]>),
  );

  const rows = firstRows.concat(...rest);
  if (rows.length !== total) {
    throw new Error(`${path.split('?')[0]}: read ${rows.length} of ${total} rows`);
  }
  return rows;
}
