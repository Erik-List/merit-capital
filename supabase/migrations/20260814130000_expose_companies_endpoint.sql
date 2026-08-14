-- Expose public.companies as the second public endpoint (PRO-26).
--
-- Decision recorded in PRO-26: expose both endpoints, block nothing. The
-- earlier "one endpoint, no embedding" stance predated the view merge
-- (20260719140000); today investors and companies are two real tables joined
-- by a real FK, which makes PostgREST resource embedding the platform's
-- native behavior. The same grant that opens /companies necessarily opens
-- /investors?select=*,companies(*), and that is now intended: embedding is
-- how slug-based drill-down works at all, since investors.id is opaque
-- uuid-text and companies carries no slug columns.
--
-- Accepted and documented rather than blocked: an unbounded embed is a fat
-- response (max_rows = 1000 caps the top level), and embedded lists carry no
-- Content-Range, so pagination always happens on /companies itself.

BEGIN;

GRANT SELECT ON public.companies TO anon, authenticated;

-- Restate the table comment with query guidance; PostgREST maps it into the
-- live OpenAPI spec, and it is the only documentation an agent gets.
COMMENT ON TABLE public.companies IS
'Portfolio companies as classified by the outcome pipeline, one row per
(investor, company) pair. A company backed by two investors appears twice.
Also the derivation source for the investor-level metrics:
recompute_investor_metrics aggregates these rows into investors.track_record,
graduation_rate and the three company_*_distribution columns on every write
to this table. Filter one portfolio by investor_id, or by slug through an
embedded filter: ?select=*,investors!inner(slug)&investors.slug=eq.<slug>.
Embedding investors<->companies works in both directions, but embedded lists
carry no Content-Range; paginate on this endpoint, never inside an embed.';

COMMIT;

NOTIFY pgrst, 'reload schema';
