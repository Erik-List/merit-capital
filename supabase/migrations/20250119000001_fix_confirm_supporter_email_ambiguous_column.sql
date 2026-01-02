BEGIN;

-- Fix ambiguous column reference in confirm_supporter_email function
-- The WHERE clause needs to qualify column names to avoid conflict with RETURN TABLE columns
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
  WHERE public."Supporters".id = p_supporter_id
    AND public."Supporters".email_confirmed_at IS NULL;
  
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

COMMIT;














