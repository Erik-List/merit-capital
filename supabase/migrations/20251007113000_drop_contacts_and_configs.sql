begin;

-- Drop view first if exists
drop view if exists public."ContactsMetricsView";

-- Drop policies and tables in dependency-safe order
do $$
begin
  if to_regclass('public."Contacts"') is not null then
    -- Drop RLS policies implicitly with table drop
    drop table if exists public."Contacts" cascade;
  end if;
  if to_regclass('public."FieldConfig"') is not null then
    drop table if exists public."FieldConfig" cascade;
  end if;
  if to_regclass('public."ContactStatusConfig"') is not null then
    drop table if exists public."ContactStatusConfig" cascade;
  end if;
end$$;

-- Drop supporting function and indexes if they only served these tables
-- (set_updated_at may be used elsewhere; keep it if present)

-- Drop unique index on Contacts.name if present
do $$
begin
  if exists (select 1 from pg_indexes where schemaname = 'public' and indexname = 'contacts_name_unique') then
    execute 'drop index public.contacts_name_unique';
  end if;
end$$;

commit;


