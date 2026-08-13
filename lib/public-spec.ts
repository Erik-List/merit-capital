// Shared access to the live PostgREST OpenAPI spec, filtered to the public
// API surface. Supabase only serves the spec to the service role, and a
// service-role spec describes everything that role can see, so the spec is
// fetched server-side and cut down to the allowlisted objects before anything
// public-facing touches it. Used by the /data proxy root and the
// /api-reference page.

// The public surface: objects anon holds SELECT on (see migration
// 20260719120000_single_public_endpoint.sql). Extend when a new object is
// deliberately made public.
const PUBLIC_OBJECTS = ['investors'];

export type SpecProperty = {
  description?: string;
  type?: string;
  format?: string;
};

export type SpecDefinition = {
  description?: string;
  properties?: Record<string, SpecProperty>;
  required?: string[];
};

// OpenAPI 2.0 (swagger) document as emitted by PostgREST.
export type PublicSpec = {
  swagger?: string;
  host?: string;
  basePath?: string;
  schemes?: string[];
  paths?: Record<string, unknown>;
  definitions?: Record<string, SpecDefinition>;
  [key: string]: unknown;
};

export async function getPublicSpec(): Promise<PublicSpec | null> {
  const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
  const serviceKey = process.env.SUPABASE_SERVICE_ROLE_KEY!;
  let spec: PublicSpec;
  try {
    const response = await fetch(`${supabaseUrl}/rest/v1/`, {
      headers: {
        apikey: serviceKey,
        Authorization: `Bearer ${serviceKey}`,
      },
      next: { revalidate: 3600 },
    });
    if (!response.ok) return null;
    spec = await response.json();
  } catch {
    return null;
  }

  if (spec.paths) {
    spec.paths = Object.fromEntries(
      Object.entries(spec.paths).filter(
        ([path]) => path === '/' || PUBLIC_OBJECTS.includes(path.slice(1))
      )
    );
  }
  if (spec.definitions) {
    spec.definitions = Object.fromEntries(
      Object.entries(spec.definitions).filter(([name]) =>
        PUBLIC_OBJECTS.includes(name)
      )
    );
  }
  return spec;
}
