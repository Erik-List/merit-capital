BEGIN;

-- Function to generate sharing token (firstname-lastname-[4-digit-code])
CREATE OR REPLACE FUNCTION generate_sharing_token(
  p_first_name text,
  p_last_name text
)
RETURNS text
LANGUAGE plpgsql
AS $$
DECLARE
  base_token text;
  code text;
  candidate_token text;
  attempt int;
  max_attempts int := 10;
BEGIN
  -- Normalize names: lowercase, replace spaces with hyphens
  base_token := LOWER(REPLACE(p_first_name || '-' || p_last_name, ' ', '-'));
  
  -- Remove special characters, keep only alphanumeric and hyphens
  base_token := REGEXP_REPLACE(base_token, '[^a-z0-9-]', '', 'g');
  
  -- Remove multiple consecutive hyphens
  base_token := REGEXP_REPLACE(base_token, '-+', '-', 'g');
  
  -- Remove leading/trailing hyphens
  base_token := TRIM(BOTH '-' FROM base_token);
  
  -- Generate unique token with 4-digit code
  attempt := 0;
  LOOP
    attempt := attempt + 1;
    
    -- Generate random 4-digit code (0000-9999)
    code := LPAD(FLOOR(RANDOM() * 10000)::text, 4, '0');
    candidate_token := base_token || '-' || code;
    
    -- Check uniqueness
    IF NOT EXISTS (
      SELECT 1 FROM public."Supporters" 
      WHERE sharing_token = candidate_token
    ) THEN
      RETURN candidate_token;
    END IF;
    
    -- Exit if max attempts reached
    IF attempt >= max_attempts THEN
      EXIT;
    END IF;
  END LOOP;
  
  -- Fallback: use UUID-based suffix if collisions persist
  RETURN base_token || '-' || SUBSTRING(REPLACE(gen_random_uuid()::text, '-', ''), 1, 8);
END;
$$;

-- Function to insert supporter
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
BEGIN
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
EXCEPTION
  WHEN unique_violation THEN
    -- Handle duplicate email
    RAISE EXCEPTION 'Email already registered' USING ERRCODE = '23505';
END;
$$;

-- Function to increment sharing clicks
CREATE OR REPLACE FUNCTION increment_sharing_clicks(p_sharing_token text)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  UPDATE public."Supporters"
  SET direct_clicks = COALESCE(direct_clicks, 0) + 1
  WHERE sharing_token = p_sharing_token
    AND sharing_link_active = true;
END;
$$;

-- Function to increment sharing conversions
CREATE OR REPLACE FUNCTION increment_sharing_conversions(p_sharing_token text)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  UPDATE public."Supporters"
  SET direct_conversions = COALESCE(direct_conversions, 0) + 1
  WHERE sharing_token = p_sharing_token
    AND sharing_link_active = true;
END;
$$;

-- Grant execute permissions
GRANT EXECUTE ON FUNCTION insert_supporter(text, text, text, text, text, text) TO anon, authenticated;
GRANT EXECUTE ON FUNCTION increment_sharing_clicks(text) TO anon, authenticated;
GRANT EXECUTE ON FUNCTION increment_sharing_conversions(text) TO anon, authenticated;

COMMIT;

