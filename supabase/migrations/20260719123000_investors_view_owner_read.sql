-- With the base tables no longer granted to anon/authenticated
-- (20260719120000), the security_invoker view denies those roles too: an
-- invoker view checks the caller's privileges on the underlying tables.
-- Switch to the standard owner-view pattern: the view reads with its owner's
-- privileges, and anon/authenticated hold SELECT on the view alone. RLS is
-- disabled everywhere on this dataset, so the owner read exposes exactly the
-- view's own projection and nothing else.
ALTER VIEW public.investors SET (security_invoker = false);
