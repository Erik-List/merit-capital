BEGIN;

-- Ensure the client can select from the view
GRANT SELECT ON TABLE public."InvestorView" TO anon, authenticated;

-- Enable RLS (no-op if already enabled)
ALTER TABLE public."IndividualInvestor" ENABLE ROW LEVEL SECURITY;
ALTER TABLE public."InstitutionalInvestor" ENABLE ROW LEVEL SECURITY;

-- Allow reading subtype rows only when the parent investor is APPROVED
DROP POLICY IF EXISTS "read individual when parent approved" ON public."IndividualInvestor";
CREATE POLICY "read individual when parent approved"
ON public."IndividualInvestor"
FOR SELECT
TO anon, authenticated
USING (
  EXISTS (
    SELECT 1 FROM public."Investor" i
    WHERE i.id = public."IndividualInvestor".investor_id
      AND i.status = 'APPROVED'
  )
);

DROP POLICY IF EXISTS "read institutional when parent approved" ON public."InstitutionalInvestor";
CREATE POLICY "read institutional when parent approved"
ON public."InstitutionalInvestor"
FOR SELECT
TO anon, authenticated
USING (
  EXISTS (
    SELECT 1 FROM public."Investor" i
    WHERE i.id = public."InstitutionalInvestor".investor_id
      AND i.status = 'APPROVED'
  )
);

COMMIT;
