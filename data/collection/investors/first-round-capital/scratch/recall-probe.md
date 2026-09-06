# Recall probe — First Round Capital (PRO-93)

Run 2026-09-06, before the single scheduled rebuild (COLLECTION.md §3).
Expected-member lists built from sources independent of the base, then diffed.

## Layer 1 — the firm's own NETWORK directory (invented for this run)

First Round's `/team/` namespace holds two populations. The capitalised half,
`/team/<First_Last>`, is **not the firm's roster**: it is a directory of the
FOUNDERS AND CEOs of its portfolio companies, each page headed
"<Role> at <Company>" (config `roster._note`). Pulled in full:
**212 profiles, 124 naming a company** (`sources/web/network-directory.json`,
`scratch/network-directory.py`).

Diffed against the base: **one company the base did not have — One Kings Lane**,
recorded as a recall addition with its citation. Every other named company was
already a base row, several of them only under a logo-wall filename, which is
itself corroboration that the name-fix map is right.

This is the same namespace that would have poisoned the Form D sweep with
hundreds of founder names if the roster pattern had not been narrowed to the
lowercase namespace. Used the other way round it is a recall layer, and it is
the layer that found the run's only site-invisible member.

## Layer 2 — Wikipedia insource sweep

94 articles naming the firm, 21 company candidates outside the base. All but
one resolved to rows already present under an artifact name (Gigya, Kno,
Outright, Pantheon, Path, Yummly, Fandom = Wikia, Upstart, The Meet Group).
**FiscalNote** is a genuine addition and is recorded with its citation.
Recorded rejections: B Capital (Howard Morgan's later firm), Winklevoss
Capital, Entrepreneurs Roundtable Accelerator, Energy Impact Center, Bolt
(the article names WikiYou, which is already a base row), Zapier, Zenreach,
Zulip — each mentions the firm without evidencing a First Round position.

## Layer 3 — exit-side EDGAR full-text sweep

93 registrants naming the firm's entities. Every third-party registrant that
is a portfolio company was already a base row (Uber, Warby Parker, Rover,
Blue Apron, Roblox, Upstart, Bazaarvoice, On Deck, Constant Contact,
Internet Brands, Merlin, Notable Labs, Latch, CCC — the last two as acquirers
of base rows). The remainder is the expected noise class: SPAC shells,
Regulation-CF issuers and "first round" as a common noun.

The sweep's most valuable hit was not a company at all: **FR Capital Holdings,
L.P. (CIK 1776703)**, the firm's own Schedule 13G filer, which matches no
"first round" name pattern and was therefore missing from the entity registry.

## Layer 4 — parametric enumeration, and one recorded self-correction

The kickoff `verify.known_positions` list was written from model priors and
carried six names that are **not First Round positions**: Brex, Carta,
Linktree, Warp (plus Figma and Shopify by the same route). All six come from
`firstround.com/ai/<company>` — the firm's editorial AI case studies, not a
portfolio list. Reading an editorial surface as a listing surface is exactly
the failure §5's surface enumeration warns about, and the list was replaced
with names the base evidences.

## Result

**Two additions on a 698-row base.** The site, capture and Form D layers carry
recall for this investor; the noise is precision-side, which is the Sequoia
shape the playbook predicts and the opposite of what PRO-93 expected ("expect
the recall probe to do real work"). The reason is visible in the layers: First
Round has published a company list continuously since 2007 across four site
generations, so there is very little that never reached a list.
