# sources/wayback for thrive-capital

`partner-roster.json` is CURATED, not the output of `partner-roster.py`: thrivecap.com has
no team page and no people namespace was ever archived (config.json roster._note). Rows come
from the ADV Schedule A officer list (CRD 162771, amendment of 2026-07-06), the related persons
on the firm's own fund Form Ds (Joshua Kushner, Jared Weinstein) and press-dated partner
tenures (decisions.md ruling 11). `years_seen` is the tenure window the record supports, so the
base build's tenure check (last_seen, snapshots) dates a filing seat against it; `snapshots`
equals the number of tenure years so departed partners are not treated as current.

`parsed/` is empty by design: no era of thrivecap.com listed companies (config.json
wayback._eras_note); the survivorship and roster jobs of the capture layer are carried by EDGAR
and press for this investor.
