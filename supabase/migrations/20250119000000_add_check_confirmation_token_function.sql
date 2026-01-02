BEGIN;

-- Create a SECURITY DEFINER function to check confirmation token
-- This allows querying by specific confirmation token only, bypassing RLS
CREATE OR REPLACE FUNCTION check_confirmation_token(p_token text)
RETURNS TABLE (
  id uuid,
  sharing_token text,
  email_confirmed_at timestamptz,
  email_confirmation_expires_at timestamptz
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  RETURN QUERY
  SELECT 
    s.id,
    s.sharing_token,
    s.email_confirmed_at,
    s.email_confirmation_expires_at
  FROM public."Supporters" s
  WHERE s.email_confirmation_token = p_token;
END;
$$;

-- Grant execute permission on the function to anon and authenticated roles
-- This allows public access to check specific confirmation tokens only
GRANT EXECUTE ON FUNCTION check_confirmation_token(text) TO anon, authenticated;

-- Create a SECURITY DEFINER function to confirm email and activate sharing link
-- This allows updating the supporter record after confirmation, bypassing RLS
CREATE OR REPLACE FUNCTION confirm_supporter_email(p_supporter_id uuid)
RETURNS TABLE (
  id uuid,
  email text,
  first_name text,
  sharing_token text,
  referred_by_token text
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  UPDATE public."Supporters"
  SET 
    email_confirmed_at = now(),
    sharing_link_active = true,
    updated_at = now()
  WHERE id = p_supporter_id
    AND email_confirmed_at IS NULL;
  
  RETURN QUERY
  SELECT 
    s.id,
    s.email,
    s.first_name,
    s.sharing_token,
    s.referred_by_token
  FROM public."Supporters" s
  WHERE s.id = p_supporter_id;
END;
$$;

-- Grant execute permission on the function to anon and authenticated roles
GRANT EXECUTE ON FUNCTION confirm_supporter_email(uuid) TO anon, authenticated;

COMMIT;

