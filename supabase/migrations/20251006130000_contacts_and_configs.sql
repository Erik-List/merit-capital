begin;

-- util: updated_at
create or replace function public.set_updated_at()
returns trigger
language plpgsql
as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

-- core contacts
create table if not exists public."Contacts" (
  id uuid primary key default gen_random_uuid(),
  name text not null,

  -- pipeline stage (editable via ContactStatusConfig; text key for flexibility)
  status text not null default 'NotContacted',

  -- flexible, UI-defined columns
  fields jsonb not null default '{}'::jsonb,

  -- multi-channel outreach scaffold
  -- shape example:
  -- {
  --   "email":    { "enabled": true,  "status": "Queued",      "notes": "...", "external_id": "..." },
  --   "linkedin": { "enabled": false, "status": "NotStarted",  "notes": null,  "external_id": null },
  --   "x":        { "enabled": true,  "status": "InProgress",  "notes": "",    "external_id": "..." },
  --   "phone":    { "enabled": false, "status": "NotStarted",  "notes": null,  "external_id": null }
  -- }
  outreach_status jsonb not null default '{}'::jsonb,

  -- contact info (tooltip on name)
  -- { "email": "...", "linkedin_url": "...", "twitter_handle": "...", "phone_number": "..." }
  contact_info jsonb not null default '{}'::jsonb,

  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create trigger set_contacts_updated_at
before update on public."Contacts"
for each row execute function public.set_updated_at();

create index if not exists contacts_fields_gin on public."Contacts" using gin ((fields));
create index if not exists contacts_status_idx on public."Contacts"(status);

-- dynamic field config
create table if not exists public."FieldConfig" (
  key text primary key,
  label text not null,
  type text not null default 'boolean' check (type in ('boolean','text','number')),
  position int not null default 0,
  visible boolean not null default true,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create trigger set_field_config_updated_at
before update on public."FieldConfig"
for each row execute function public.set_updated_at();

-- contact status config (ordered pipeline)
create table if not exists public."ContactStatusConfig" (
  key text primary key,
  label text not null,
  position int not null default 0,
  is_default boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create trigger set_contact_status_config_updated_at
before update on public."ContactStatusConfig"
for each row execute function public.set_updated_at();

-- metrics view: total only (no won/yes rate)
create or replace view public."ContactsMetricsView" as
select count(*)::bigint as total_contacts from public."Contacts";

-- RLS
alter table public."Contacts" enable row level security;
alter table public."FieldConfig" enable row level security;
alter table public."ContactStatusConfig" enable row level security;

drop policy if exists "contacts_select" on public."Contacts";
drop policy if exists "contacts_insert" on public."Contacts";
drop policy if exists "contacts_update" on public."Contacts";
drop policy if exists "contacts_delete" on public."Contacts";

create policy "contacts_select" on public."Contacts"
  for select using (auth.uid() is not null);
create policy "contacts_insert" on public."Contacts"
  for insert with check (auth.uid() is not null);
create policy "contacts_update" on public."Contacts"
  for update using (auth.uid() is not null) with check (auth.uid() is not null);
create policy "contacts_delete" on public."Contacts"
  for delete using (auth.uid() is not null);

drop policy if exists "field_config_all" on public."FieldConfig";
create policy "field_config_all" on public."FieldConfig"
  for all using (auth.uid() is not null) with check (auth.uid() is not null);

drop policy if exists "contact_status_config_all" on public."ContactStatusConfig";
create policy "contact_status_config_all" on public."ContactStatusConfig"
  for all using (auth.uid() is not null) with check (auth.uid() is not null);

-- seeds
insert into public."ContactStatusConfig"(key,label,position,is_default) values
  ('NotContacted','Not Contacted',10,true),
  ('Researched','Researched',20,false),
  ('Contacted','Contacted',30,false),
  ('Engaged','Engaged',40,false),
  ('Convinced','Convinced',50,false)
on conflict (key) do update set label=excluded.label, position=excluded.position, is_default=excluded.is_default;

insert into public."FieldConfig"(key,label,type,position,visible) values
  ('m1','M1','boolean',10,true),
  ('m2','M2','boolean',20,true),
  ('m3','M3','boolean',30,true)
on conflict (key) do update set label=excluded.label, type=excluded.type, position=excluded.position, visible=excluded.visible;

commit;



