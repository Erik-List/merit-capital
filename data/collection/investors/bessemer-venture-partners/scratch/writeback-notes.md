# Playbook write-back notes (PRO-80, Bessemer). Draft for report.md and the COLLECTION.md diff at close.

1. **A firm's "complete" historical list still omits its failures.** bvp.com's 2008-2012 list printed every
   investment back to 1957 with its year (294 to 328 rows) and looked complete. The 1999-2007 pages on the Internet
   Archive (the one-page portfolio and the per-practice pages) added 110 companies it had dropped, almost all
   dot-com, telecom and optical-era failures. A historical list that reads as complete is the list of what the firm
   chose to keep; the era's own captures are still owed (s5, archive layer).
2. **A first-party history or "successes" page is stage evidence.** The firm's history narrative and its 2002
   successes page state the round for the famous deals ("invested for Bessemer in the B round", "led the Series A",
   "Bessemer invested in Maxim's first three rounds, starting in 1983", "August 1992"). Parse such pages into a
   source file and show them to the judge beside the listing; they decided dozens of pre-2005 stages.
3. **A site generation can print a stored date wrong.** The 2012-2015 site printed the investment year one year
   early wherever the stored date was a January 1 placeholder (a time-zone shift): 98 companies, 301 rows. Compare
   the year across site generations before trusting any one; correct at the parse, keep the printed value.
4. **The rebuild's rename step matches departures to arrivals on a shared listing URL.** Excluded companies' other
   name renderings resurface as new rows at the rebuild (the build applies exclusions before merging name variants),
   and `rekey_overlays` then moved verdicts and classification from three unrelated departing rows onto them
   (flat-world-knowledge -> logicnow-gfi, homelight -> beyond-pricing, innovati -> vts-formerly-hightower). On a book
   whose archive rows all cite one listing page, "first wayback capture" is not unique evidence. Proposed: (a) the
   build merges name variants BEFORE applying exclusions, or carries a not_member verdict to every variant of the
   excluded row; (b) rekey never moves onto an arrival when the departure is a merge duplicate or already in
   excluded.json; (c) rekey ignores a capture URL shared by more than a handful of rows.
5. **A rebuild can run while judges record**, if it holds `record`'s lock (shared_throttle.exclusive
   "record-<slug>"): scratch/rebuild-locked.py. Proposed as a `run.py rebuild` subcommand.
6. **The team launch of a new strategy leaks its people's prior-firm companies onto the main portfolio page** (the
   partner-carried class at firm scale): one capture, no year, no partner, eleven rows. A row seen in exactly one
   capture with none of the fields its neighbours carry is checked against the firm's team pages before it is seeded.
7. **The anti-portfolio as a negative control.** A firm that publishes the companies it passed on gives the run a
   free false-positive test per recall layer (27 names: 0 in the base; 3 of 296 EDGAR full-text registrants, all
   rejected). Worth a line in s5 for any firm with such a page.
8. **Cheaper judges leave the stage column empty.** Four Sonnet judges decided about 10 stages per 90 rows where the
   Fable judges decided about 70; a second Opus pass with the older site text decided 121 of 285. Budget the stage
   research on the strongest model, or plan the second pass.
9. **Single-deal vehicles are attributed by their Form D related-person list**, not by the adviser's 7.B roster: the
   Gator Co-Invest vehicles sit on the venture adviser's ADV but carry the buyout team's names and were filed within
   weeks of buyout announcements.
10. **Disk and usage are run constraints**: the machine's disk filled (swap) with eleven agents; the weekly usage
    limit was exhausted by one run on the strongest judges. Check both before launching a wave; park on usage.
11. **A bare request to web.archive.org from a judge re-arms the machine-wide cooldown for every session.** Briefs must
    forbid it explicitly whenever the archive is in cooldown (one judge did it; the cooldown doubled twice today).
