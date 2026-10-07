-- Requests to add an investor to the index, filed through the form the index
-- shows when a search finds no investor.
--
-- Access follows investors and companies: no row level security, the grants
-- are the gate, the public reads and only the service role writes. The one
-- exception is the email column: the read grant names the other columns, so
-- the requester's address cannot be selected by anon, by authenticated, or
-- through the /data proxy (Erik, 2026-10-01).
--
-- Accepted consequence: a request without `select` asks for every column,
-- email included, and is refused. Readers name the columns.

BEGIN;

CREATE TABLE public.investor_requests (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  created_at timestamptz NOT NULL DEFAULT now(),
  -- Room for one investor: the longest name in the index is 27 characters.
  investor_name text NOT NULL CHECK (char_length(investor_name) BETWEEN 1 AND 40),
  email text NOT NULL CHECK (char_length(email) BETWEEN 3 AND 254)
);

CREATE INDEX investor_requests_created_at_idx
  ON public.investor_requests (created_at DESC);

-- Supabase default privileges grant new public-schema tables to
-- anon/authenticated; take them back, then open the readable columns.
REVOKE ALL ON public.investor_requests FROM anon, authenticated;
GRANT SELECT (id, created_at, investor_name)
  ON public.investor_requests TO anon, authenticated;

-- Documentation. PostgREST maps these into the live OpenAPI spec; they are
-- the only documentation an agent gets.
COMMENT ON TABLE public.investor_requests IS
'Requests from visitors to add an investor to the index, one row per request,
filed through the form on the index page. The email column is not readable,
so name the columns you read: ?select=id,created_at,investor_name. A request
without select asks for every column and is refused. Rows are written by the
form only.';

COMMENT ON COLUMN public.investor_requests.id IS
'Stable unique identifier (uuid).';
COMMENT ON COLUMN public.investor_requests.created_at IS
'When the request was filed.';
COMMENT ON COLUMN public.investor_requests.investor_name IS
'The investor the visitor asked for, as typed, at most 40 characters. Visitor input, not checked.';
COMMENT ON COLUMN public.investor_requests.email IS
'Not readable: the requester''s email address, kept private and used only to answer the request. Selecting it is refused.';

COMMIT;

NOTIFY pgrst, 'reload schema';
