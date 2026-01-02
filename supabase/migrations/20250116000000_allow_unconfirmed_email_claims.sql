BEGIN;

-- Drop the UNIQUE constraint on email column
ALTER TABLE public."Supporters" DROP CONSTRAINT IF EXISTS "Supporters_email_key";

-- Create partial unique index that only enforces uniqueness for confirmed emails
CREATE UNIQUE INDEX IF NOT EXISTS idx_supporters_email_confirmed_unique 
ON public."Supporters"(email) 
WHERE email_confirmed_at IS NOT NULL;

-- Update insert_supporter function to handle unconfirmed email claims
CREATE OR REPLACE FUNCTION insert_supporter(
  p_first_name text,
  p_last_name text,
  p_company text,
  p_position text,
  p_email text,
  p_referred_by_token text DEFAULT NULL
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
  v_confirmation_token text;
  v_expires_at timestamptz;
  v_sharing_token text;
  v_supporter_id uuid;
  v_result jsonb;
  v_existing_supporter record;
BEGIN
  -- Check if email already exists and is confirmed
  SELECT id, email_confirmed_at INTO v_existing_supporter
  FROM public."Supporters"
  WHERE email = p_email AND email_confirmed_at IS NOT NULL
  LIMIT 1;
  
  IF v_existing_supporter.id IS NOT NULL THEN
    -- Email is already confirmed, reject
    RAISE EXCEPTION 'Email already registered and confirmed' USING ERRCODE = '23505';
  END IF;
  
  -- Delete any existing unconfirmed records for this email
  DELETE FROM public."Supporters"
  WHERE email = p_email AND email_confirmed_at IS NULL;
  
  -- Generate confirmation token
  v_confirmation_token := gen_random_uuid()::text;
  v_expires_at := now() + interval '7 days';
  
  -- Generate sharing token
  v_sharing_token := generate_sharing_token(p_first_name, p_last_name);
  
  -- Insert supporter record
  INSERT INTO public."Supporters" (
    first_name,
    last_name,
    company,
    position,
    email,
    sharing_token,
    email_confirmation_token,
    email_confirmation_expires_at,
    sharing_link_active,
    referred_by_token,
    direct_clicks,
    direct_conversions,
    network_clicks,
    network_conversions
  ) VALUES (
    p_first_name,
    p_last_name,
    p_company,
    p_position,
    p_email,
    v_sharing_token,
    v_confirmation_token,
    v_expires_at,
    false,
    p_referred_by_token,
    0,
    0,
    0,
    0
  )
  RETURNING id INTO v_supporter_id;
  
  -- Return result
  v_result := jsonb_build_object(
    'id', v_supporter_id,
    'confirmation_token', v_confirmation_token,
    'sharing_token', v_sharing_token,
    'email', p_email,
    'first_name', p_first_name
  );
  
  RETURN v_result;
END;
$$;

COMMIT;

