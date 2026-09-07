# Retired: the run-local https shims

`scratch/wayback-pull-https.py` and `scratch/partner-roster-https.py` were
run-local copies of the two `scripts/` pullers with every `web.archive.org`
URL switched from http to https. They are deleted as of 2026-09-06.

**Their stated premise was wrong.** They claimed the archive was refusing
plain-HTTP (port 80) while https answered — measured here as curl rc=7 on 2 of
3 http tries against 3 of 3 on https, n=3 a side. The YC session measured it
properly, 9 paced alternating requests: **http 7/9, https 6/9, and the failures
were rc=28 timeouts on both schemes.** The archive was flaky for everyone that
hour. The scheme swap was cosmetic; the shims "worked" because re-running is a
retry.

The real defect was in both upstream pullers and in this run's own
`scratch/build-early-eras.py`: none of them checked curl's return code, so a
year whose probe never connected was recorded and printed exactly like a year
the archive genuinely has nothing for — `0 entries`, `no capture`. Absence was
being read off silence.

Fixed upstream by the YC session in `12402a7` (3 retries with backoff, then a
loud line naming the affected years as UNKNOWN), and mirrored here in
`build-early-eras.py`. Use `scripts/wayback-pull.py` and
`scripts/partner-roster.py` directly; they are correct now and the shims would
only drift.

What the fix recovered on re-run: 3 of the 4 year-slots this run had recorded
as "no capture" (`index-oid152` 2006, `index-oid157` 2003 and 2005), and with
them one company the base never had (Amp'd Mobile) and one `first_seen`
correction (CGEN, 2007 -> 2006). See `report.md` §9 write-back 1.
