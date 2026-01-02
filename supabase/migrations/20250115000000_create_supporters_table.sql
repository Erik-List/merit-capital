BEGIN;

-- Create Supporters table
CREATE TABLE IF NOT EXISTS public."Supporters" (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  first_name text NOT NULL,
  last_name text NOT NULL,
  company text NOT NULL,
  position text NOT NULL,
  email text NOT NULL UNIQUE,
  
  -- Sharing token (format: firstname-lastname-[4-digit-code])
  sharing_token text UNIQUE,
  
  -- Email confirmation
  email_confirmation_token text UNIQUE,
  email_confirmed_at timestamptz,
  email_confirmation_expires_at timestamptz NOT NULL DEFAULT (now() + interval '7 days'),
  
  -- Link status
  sharing_link_active boolean NOT NULL DEFAULT false,
  
  -- Referral tracking
  referred_by_token text REFERENCES public."Supporters"(sharing_token) ON DELETE SET NULL,
  
  -- Tracking counts
  direct_clicks integer NOT NULL DEFAULT 0,
  direct_conversions integer NOT NULL DEFAULT 0,
  network_clicks integer NOT NULL DEFAULT 0,
  network_conversions integer NOT NULL DEFAULT 0,
  
  -- Timestamps
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  
  -- Constraint: email confirmed implies link active
  CONSTRAINT email_confirmed_implies_active CHECK (
    (email_confirmed_at IS NULL) OR (sharing_link_active = true)
  )
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_supporters_email ON public."Supporters"(email);
CREATE INDEX IF NOT EXISTS idx_supporters_sharing_token ON public."Supporters"(sharing_token);
CREATE INDEX IF NOT EXISTS idx_supporters_email_token ON public."Supporters"(email_confirmation_token);
CREATE INDEX IF NOT EXISTS idx_supporters_referred_by ON public."Supporters"(referred_by_token);
CREATE INDEX IF NOT EXISTS idx_supporters_email_confirmed ON public."Supporters"(email_confirmed_at) WHERE email_confirmed_at IS NOT NULL;

-- Trigger for updated_at
CREATE TRIGGER set_supporters_updated_at
BEFORE UPDATE ON public."Supporters"
FOR EACH ROW EXECUTE FUNCTION public.set_updated_at();

COMMIT;

