# Delta brief: the rows the rebuild added, PRO-80 Bessemer Venture Partners

Read `JUDGE-BRIEF.md` first and completely, then `judge_lib.py` (whole), `../documentation/decisions.md` (D1 to D10,
X1, rulings R1 to R8) and COLLECTION.md section 6 (`grep -n "^## 6. Classification columns\|^## 7. "
../../../COLLECTION.md`). Everything in JUDGE-BRIEF.md holds. This file says what is different about the delta.

Your rows come from `python3 show.py --batch <N>`. They are of three kinds:

1. **Companies from the firm's own pre-2008 site** (eras `html-people` 1999 to 2001, `asp-onepage` 2002 to 2007,
   `asp-success`), read from the Internet Archive. Most are dot-com, telecom and optical-era companies that failed
   or were sold cheaply and that the firm's 2008 to 2012 list no longer carried. Membership is seeded on the firm's
   own listing. For each:
   - **Identity first.** Check `../companies/base.json` for the same company under another name (a later brand, a
     merger partner, an acquirer). If it is a duplicate of an existing row, still classify it, add the flag
     `identity_conflated`, and name both slugs in your report.
   - **Status**: find what became of it (one `wikifetch.py` or `nq.py` lookup; the listing's "(acq. by X)" is the
     firm's own record). A dot-com that vanished with no trace after 2001 to 2003 and whose site is gone reads
     `defunct` only with a source saying it closed; otherwise `unknown` with a specific note.
   - **Entry stage and date**: the 1999 to 2001 pages give the firm's investment year and deal partner; the 2002+
     pages give a sentence. A round is named only where a source names it; otherwise `undetermined` with the
     entry date from the firm's year.
   - **Not a member**: the firm's own sentence sometimes shows the position is stock received for another portfolio
     company ("Voyant acquired BVP's portfolio company Octave Communications"): `not_member`, sale consideration
     (R6), naming the acquired company. A company that was already listed when Bessemer bought in (a BSE or NSE
     listed Indian company, a NASDAQ company bought in a PIPE): `not_member` (T3 / R3) unless a private round came
     first. A fund or holding vehicle: `not_member` (D7).
2. **Recall additions** (the note starts "recall addition:" and carries the citation that ties a Bessemer fund to
   the company). Membership is seeded; classify every column. The citation usually names the round: use it for the
   entry stage where it says Bessemer joined in that round, and check whether that round was the firm's FIRST
   (an existing investor "participating" entered earlier: find the earlier round).
   Measurex, Fotomat and Interdata are deals of the venture group before the 1981 spin-out, named on the firm's
   history page (R2): add the flag `pre_spinout`; the entry year is to be found (the 1960s to early 1970s).
3. **Rows whose identity changed in the rebuild** (a merge folded two rows into one): check that the stored answers
   still describe the merged company and correct what does not fit.

Everything else as in JUDGE-BRIEF.md: one classification line per member row answering every column in `need`
(status, valuation_range, entry_stage with entry_date and rounds, hq_country, hq_city, focus), two files of at most
25 rows, `NQ_TAG=<TAG>` on every nq.py and judgments run, notes in plain prose without em-dashes, WebSearch at most
5 calls.
