-- Drop cut-feature database objects for the v1 scope reduction.
--
-- v1 removes the rating system (Rating, User) and the sharing/referral
-- "Supporters" system (table + tracking/confirmation functions). The
-- contacts/configs CRM tables were already dropped in
-- 20251007113000_drop_contacts_and_configs.sql.
--
-- Kept: Investor, IndividualInvestor, InstitutionalInvestor, InvestorView, and
-- the ApprovalStatus enum (still used by Investor.status). InvestorView does not
-- depend on Rating/User, so dropping them is safe. All drops use IF EXISTS so
-- the migration is idempotent regardless of what is currently applied remotely.

-- Rating references User (Rating_user_id_fkey); CASCADE handles ordering and any
-- dependent policies/constraints.
DROP TABLE IF EXISTS "Rating" CASCADE;
DROP TABLE IF EXISTS "User" CASCADE;

-- Sharing/referral system.
DROP TABLE IF EXISTS "Supporters" CASCADE;

-- Sharing/referral helper functions (signature-agnostic, safe if absent).
DO $$
DECLARE
  fn record;
BEGIN
  FOR fn IN
    SELECT p.oid::regprocedure AS sig
    FROM pg_proc p
    WHERE p.pronamespace = 'public'::regnamespace
      AND p.proname IN (
        'check_confirmation_token',
        'check_sharing_token',
        'confirm_supporter_email',
        'generate_sharing_token',
        'increment_sharing_clicks',
        'increment_sharing_conversions',
        'insert_supporter'
      )
  LOOP
    EXECUTE 'DROP FUNCTION ' || fn.sig || ' CASCADE';
  END LOOP;
END $$;

-- Rating-only enum (ApprovalStatus is intentionally kept for Investor.status).
DROP TYPE IF EXISTS "RatingType";
