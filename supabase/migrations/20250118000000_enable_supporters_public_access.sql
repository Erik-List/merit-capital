BEGIN;

-- Enable RLS on Supporters table to prevent public browsing
ALTER TABLE public."Supporters" ENABLE ROW LEVEL SECURITY;

-- Create a SECURITY DEFINER function to check sharing token
-- This allows querying by specific token only, not browsing all records
CREATE OR REPLACE FUNCTION check_sharing_token(p_token text)
RETURNS TABLE (
  sharing_token text,
  sharing_link_active boolean
)
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  RETURN QUERY
  SELECT 
    s.sharing_token,
    s.sharing_link_active
  FROM public."Supporters" s
  WHERE s.sharing_token = p_token;
END;
$$;

-- Grant execute permission on the function to anon and authenticated roles
-- This allows public access to check specific tokens only
GRANT EXECUTE ON FUNCTION check_sharing_token(text) TO anon, authenticated;

-- Deny direct SELECT on the table (RLS will block it)
-- Users can only access via the function with a specific token
-- No RLS policy needed - the function uses SECURITY DEFINER to bypass RLS

COMMIT;

