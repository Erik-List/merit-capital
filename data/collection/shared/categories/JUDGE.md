# Category judge

One batch file in `queue/batch-NNN.json` holds up to 100 companies. Each item
has `key`, `name`, and `holders`: what every investor's book has on the company
(`today` is the current single sector, `firm_words` the investor's own sector
words, `note` the collection note, `hq`, `status`, `first_seen`). A company held
by several books shows several holders; they are ONE company, judge it once.

Judge from the item and your own knowledge. No web search, no network tool.

Give each company one to three categories from this list, exact spelling:

Market or product: Fintech, Payments & Insurance · Healthcare · Biotech & Life
Sciences · Climate, Energy & Agriculture · Industrial & Manufacturing ·
Logistics, Mobility & Transport · Real Estate & Construction · Education ·
Work, HR & Productivity · Legal & Compliance · Sales, Marketing & Customer
Service · Media, Social & Gaming · Commerce & Consumer Goods · Travel &
Hospitality · Aerospace, Defense & Government
Technology: AI · Data & Analytics · Developer Tools & Infrastructure ·
Cybersecurity · Crypto & Web3 · Hardware, Robotics & Semiconductors
Customer: Consumer · B2B
Business model: SaaS · Marketplace

Rules
- At most three. At most ONE market or product category, and it comes first
  when one fits. A pure tooling company (a database, a cloud service) carries
  technology and customer categories only.
- Developer Tools & Infrastructure takes networking and telecom infrastructure;
  Hardware, Robotics & Semiconductors takes chips, devices and consumer
  electronics; Sales, Marketing & Customer Service takes support and CX tools;
  Media, Social & Gaming takes social and messaging apps; Fintech, Payments &
  Insurance takes lending, wealth and insurance.
- Customer: give Consumer or B2B whenever the item or your knowledge says who
  buys or uses the product: Consumer for households and individuals, B2B for
  businesses, hospitals, schools and governments. A medical device company
  sells to hospitals, so it is B2B. Only a drug or therapeutics developer, a
  research-stage company, or a company whose customer stays unknown carries
  no customer category.
- Business model: SaaS only when the company sells software by subscription;
  Marketplace only when it matches two sides (buyers and sellers, riders and
  drivers). Neither for hardware, services, content or a pure consumer app.
- A wrong join: when one holder plainly describes a different company from
  the others, judge the company the key names (its CIK or domain) and say so
  in `why`.
- `fit`: "good" when the categories describe the company well; "forced" when a
  category is a stretch (then say what would fit in `suggest`); "none" when
  nothing fits (empty `tags`, a `suggest`).
- `unknown`: true when the item does not say what the company does (a name and
  "on the firm's list only"). Then leave `tags` empty with fit "none" unless the
  name or your own knowledge settles it; never guess from a name alone.
- `why`: one sentence, at most 20 words: what the company does and which clue
  decided the categories.

Write `queue/batch-NNN.out.jsonl`, one JSON object per line, every key of the
batch exactly once:
{"key": "...", "tags": ["...", "..."], "fit": "good|forced|none", "unknown": false, "suggest": "", "why": "..."}
