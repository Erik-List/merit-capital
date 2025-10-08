begin;

-- Ensure we can upsert by name
create unique index if not exists contacts_name_unique on public."Contacts"(name);

-- Upsert milestone field configs with friendly labels
insert into public."FieldConfig"(key,label,type,position,visible) values
  ('m1','Milestone 1','boolean',10,true),
  ('m2','Milestone 2','boolean',20,true),
  ('m3','Milestone 3','boolean',30,true),
  ('m4','Milestone 4','boolean',40,true)
on conflict (key) do update set
  label = excluded.label,
  type = excluded.type,
  position = excluded.position,
  visible = excluded.visible;

with rows(name, won, m1, m2, m3, m4) as (
  values
    ('Louis Wübben', false, true,  false, true,  true),
    ('Linus Wetzig', true,  true,  false, true,  true),
    ('Tom Amthauer', true,  false, false, true,  true),
    ('Lukas Esch', true,  true,  false, true,  true),
    ('Simon Hipp', false, true,  false, true,  true),
    ('Martin Bender', false, true,  false, true,  true),
    ('Alex Nedelchev', false, true,  false, true,  true),
    ('Julius de Gruyter', false, true,  false, true,  true),
    ('Paul Goth', false, false, false, true,  true),
    ('Ahmad Zadnia', true,  true,  false, true,  true),
    ('Patrick Trost', false, false, false, true,  true),
    ('Ennio Eberwein', false, true,  false, true,  true),
    ('Luca Micke', false, true,  false, true,  true),
    ('Ennie Raguse', false, true,  false, true,  true),
    ('Paulo Ramirez', false, true,  false, true,  true),
    ('Fabio Sobirey', false, true,  false, true,  true),
    ('Sander Bock', true,  true,  false, true,  true),
    ('Finn zur Mühlen', false, true,  false, true,  true),
    ('Alexander Sporenberg', false, true,  false, true,  true),
    ('Felix Haas from Lovable', false, true,  false, true,  true),
    ('Flo Heinemann', false, true,  false, true,  true),
    ('Timon Gregg', false, false, false, true,  true),
    ('Julius Hillebrand', false, false, false, true,  true),
    ('Simon Romanski', true,  false, false, true,  true),
    ('Cleo Rilling', false, true,  false, true,  true),
    ('Anna Horvath', true,  true,  false, true,  true),
    ('Max Arnold', true,  true,  false, true,  true),
    ('Arne Strickmann', true,  false, false, true,  true),
    ('Chris Treble', false, true,  false, true,  true),
    ('Martin Rudigier', false, true,  false, true,  true),
    ('Roland Graser', false, true,  false, true,  true),
    ('Nick Linck', false, false, false, true,  true),
    ('Jakob Stein', false, false, false, true,  true),
    ('Mats Funke', false, true,  false, true,  true),
    ('Raphael Kaiser', true,  true,  false, true,  true),
    ('Raphael Volpert', false, true,  false, true,  true),
    ('Sheng Xin Yu', true,  true,  false, true,  true),
    ('Lauritz Lucas', false, true,  false, true,  true),
    ('Ruben Reuter', false, false, false, true,  true),
    ('Joe Lammers', false, false, false, true,  true),
    ('Arthur Körner', false, true,  false, true,  true),
    ('Jonas von Seggern', false, true,  false, true,  true),
    ('Sean Sdahl', false, false, false, true,  true),
    ('Julian Döttinger', true,  false, false, true,  true),
    ('Leopold Schmidt', true,  true,  false, true,  true),
    ('Moritz Erfert', false, false, false, true,  true),
    ('Robert Maier', false, false, false, true,  true),
    ('Behsad Riemer', false, false, false, true,  true),
    ('Christian Byza', false, true,  false, true,  true),
    ('Stefan Feistinger', false, true,  false, true,  true),
    ('Cornelius Menke', false, true,  false, true,  true),
    ('Ferdinand Dabitz', false, false, true,  true,  true),
    ('Lennart Schmidt', false, false, true,  true,  true),
    ('Leopold von Waldthausen', false, false, true,  true,  true),
    ('Allegro Sproute', false, true,  false, true,  true),
    ('Marius Meiners', false, false, true,  true,  true),
    ('Bela Wiertz', false, true,  false, true,  true)
)
insert into public."Contacts"(name, status, fields)
select
  name,
  case when won then 'Convinced' else 'NotContacted' end as status,
  jsonb_build_object(
    'm1', m1,
    'm2', m2,
    'm3', m3,
    'm4', m4
  ) as fields
from rows
on conflict (name) do update
set status = excluded.status,
    fields = excluded.fields,
    updated_at = now();

commit;


