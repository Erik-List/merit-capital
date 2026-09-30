# Post-grind fix list and rebuild merges (collected from judge reports)

## Identity merges for the scheduled rebuild (canonical <- duplicate)
From m3 (2026-09-30):
- willow <- exploramed-nc7-inc
- revelle-aesthetics <- nc8-inc
- fusion-io <- fusion-multisystems-inc
- the-wing <- refresh-club-inc
- ifonly <- traina-interactive-corp
- lot18 <- l18-holdings-inc
- elements-behavioral-health <- ebh-holding-company-inc
- brale <- stable-coin-inc
- (one filer, CIK 1809817: mitolab-inc and march-therapeutics-inc, both not_member; no merge needed)

## Corrections for canonical rows (apply in the fixes pass, cited)
From m3:
- elements-behavioral-health: acquired, not defunct (BlueMountain bought the assets out of the 2018 bankruptcy;
  bhbusiness.com, 2026-08-20); check R1 control reading.
- the-wing: entry NEA's Series A, 2017-04 (not the band's Growth).
- lot18: entry NEA's Series B, 2011-05 (not the band's Series A).
- fusion-io: entry NEA's Series A, 2008-03 (Wikipedia; the band read Growth 2011).
- willow: country US, Mountain View (the GB claim is wrong).

## Open for later passes
- azuray-technologies-inc status unknown; nc8-inc, azuray, unite-genomics stage undetermined.

## From c13 (batch 25 + 26 listed)
Membership re-judges (verdict lines with citations in the fixes pass):
- paladina-health: R1 control (NEAPH Acquisitionco bought it from DaVita, Equity Purchase Agreement 2018-05-24, Everside
  S-1 exhibit 10.14); successors everside-health and marathon-health are the same NEA position: control_position.
- achaogen-inc: X1 (first NEA purchase June 2016 through GEO Fund IV, IPO 2014).
- the-spectranetics-corporation: D8 check (stock from Advanced Interventional Systems' 1994 merger into Spectranetics).
Merges (canonical <- duplicate; pick canonical = live-site row):
- nationwide-remittance-centers <- nrc (nrc's CIK join is a different, public company: clear it)
- semiconductor-manufacturing-international-corporation-smic <- semiconductor-manufacturing-int-l
- limitless <- rewind ; forallsecure <- mayhem ; topia <- move-guides ; howl <- narrativ ; springpath <- storvisor ;
  union <- tabbedout ; medisys-edutech <- medrc-edutech ; catalyst-biosciences <- targacept ;
  occam-networks-inc <- accelerated-networks-inc   (check which of each pair is the live-site row before writing)
Classification notes:
- positron-ai: 1b_plus at $5B (NEA co-led Series C, 2026-09-10) recorded by c13.
- mode, rewind: Wikidata GB/NZ disputed, both US.
- status unknown (15): maxiscale, nazomi, pacificdental, peptimmune, primary-health, primax, reshape, recce, skyline-solar,
  svaya, t-ram, think3, united-medical-plan, visual-edge, rapid-mobile-media.
- stage settleable later: mode (NEA led the 2017 Series A; firm's year 2015), medrc.
- Sibling contradiction: First Round's Limitless note (TechCrunch calls NEA's 2023 round the Series A).

## From c9 (batches 17-18)
- Verdicts recorded on listed rows (kept): not_member X1/R2 repros-therapeutics, rigel-pharmaceuticals, seattle-genetics,
  savara, solta-medical; not_member D5 rock-health (a seed fund and accelerator). rf-monolithics, silicon-graphics stay
  members (an NEA partner on the board before listing).
- Merges: sagimet-biosciences <- 3-v-biosciences-inc (CIK 1400118, renamed); serious-materials-inc <- serious-energy
  (CIK 1418835; check canonical); sitetracker <- sitetraker (CIK 1711376).
- revspring: R1 control test open (NEA beside Frazier's 2024 buyout).
- Rule-10: sentry 1b_plus ($3B 2022, stale) vs Accel below_1b: align Accel at ingest.
- status unknown: satori, sengled, serious-energy, serious-materials-inc, solfocus-inc; simsolid country/city open.

## From c8 (batches 15-16)
- Merges (same CIK): everactive <- psikick-inc ; expanse <- qadium ; onkure-therapeutics-inc vs reneo-pharmaceuticals
  (check which is live; Reneo merged into OnKure 2024).
- Membership re-judges: X1 orexigen-therapeutics, oric, peplin, phathom-pharmaceuticals, regulus-therapeutics;
  D8 pharmos (NEA stock came from Pharmos's 2006 purchase of Vela: recall candidate Vela Pharmaceuticals);
  D5 prospex-medical-iii-inc (device incubator entity).
- Sibling rows stale: pulse (Lightspeed, Redpoint carry BG; US), plusmo (Felicis defunct; acquired by AT&T 2009),
  qualified-health (Menlo SF; Palo Alto), outrider (8VC Golden; Brighton).
- status unknown: poggled, prospex-medical-iii-inc; city unknown: pilot-ai, plusmo, pponext, prime-financial-technologies.

## From m1
- Merges (duplicate of site row, flagged identity_conflated): the-climate-corporation <- climate-corp, weatherbill-inc ;
  vuclip <- xinlab-inc ; travelbank <- travelator-inc ; pulse <- alphonso-labs-inc ; drobo <- data-robotics-inc ;
  turi <- graphlab-inc ; mojo-vision <- tectus-corp ; block-renovation <- lyra-technologies-inc ; super <- nusantara-holdings-inc ;
  trivascular <- tv2-holding-co ; the-well <- wrii-corp.
- Same-CIK pairs, both not_member (no merge needed): ancora-heart/guided-delivery-systems; kareo/tebra; whiteglove x2.
- super: prefilled defunct + US is a wrong join; NEA's Super is the Indonesian company (fix status/country/city).
- Recall addition at rebuild: Avivo Corporation (NEA 10 an 'AVIVO INVESTOR' on WebSideStory's 2006 purchase of Visual
  Sciences, LLC; citation https://www.sec.gov/Archives/edgar/data/1357525/000095013408003738/v37326exv2w4.txt);
  then websidestory: D8 check (sale consideration).
- Verdicts: northern-power-systems not_member (R1 control); visual-sciences not_member (D8, NEA held Avivo); stx member.
- status unknown: mayan-networks, viacor-inc; city_unknown home-account-network.

## From c2 (batches 3-4)
- blend: is Blend Therapeutics (later Tarveda, liquidated 2022), not Blend Labs; carries Blend Systems' Form Ds (CIK
  1560253, a different company): check a merge with tarveda-therapeutics / blend-therapeutics and a never_merge or
  reject for the Blend Systems filings.
- catalyst-biosciences is Targacept (now Gyre Therapeutics); cerecor is now Avalo Therapeutics (names only).
- Membership re-judges: X1 cadence (Cadence Pharmaceuticals), cascadian-therapeutics, celcuity, champions-oncology;
  caremark-rx (D8 or X1); braincells stage Pre-Seed looks wrong.
- Sibling alignments (NEA holds fresher cited evidence): belly (a16z defunct -> acquired); boku (a16z, Benchmark,
  Khosla: San Francisco -> London, GB); chaos (8VC, Accel below_1b -> 1b_plus $4.5B); care-com (IVP Waltham -> Dallas);
  champions-oncology (Battery Baltimore -> Hackensack); bright-health (Headline Minneapolis -> Doral);
  charm-therapeutics (GC unknown, US -> private, GB).
- status unknown: braincells-inc, bedrocket; no city: basalt, backflip-ai, bnto, boxc, change-io, ceramic, brenig.

## From c5 (batches 9-10)
- Verdicts recorded on listed rows (kept, X1/R2): geron, gossamer-bio, genocea, hemosense, immunex-corporation,
  immunomedics, infinity-pharmaceuticals. inhibitex stays a member (NEA 10 Series D 2002, pre-IPO).
- Merges: omio <- goeuro (renamed 2019); one-concern <- grey-rhino (same description, year, board member: verify).
- Wrong joins: glacier's Form D (CIK 1470797) is another Glacier (replaced); genies' rounds include CIK 1528747 (not Genies).
- grubwithus: defunct kept; the firm now links goat.com (check whether the stock carried into GOAT).
- imara, glycomimetics: public -> acquired (reverse mergers; the Battery reading).
- status unknown: hdmessaging, hyperfair, illumitex-inc.
- Tooling: two judges shared NQ_TAG=c5 (shared news-extra-c5.json); harmless, NEWS() refuses a missing item.

## From c3 (batches 5-6)
- Verdicts recorded (kept): not_member X1 cti-biopharma, dallas-semiconductor; not_member R1 dsi-renal (control_position).
- Merges: cohere-technologies <- cohere-networks (verify) ; dasan-zhone-solutions-inc / zhone-technologies (one company,
  Zhone renamed DASAN Zhone 2016) ; aetherflux <- cowboy-space (verify) ; imergy-power-systems <- deeya-energy-inc ;
  drobo <- data-robotics-inc (also from m1) ; curana-health <- allyalign-health (c3 says merged).
- Re-judge flags: curana-health (R1: NEA formed it by uniting three companies); comprehensive-pharmacy-services (2019
  deal, possible control); cirrus-logic (firm's 1990 year after the 1989 IPO: X1 check).
- Rule-10: cloudflare 100b_plus $125.27B vs USV $99.31B (10b_plus): align USV at ingest. First Round's Drop has FR.
- status unknown: china-gtel, compass-labs, complexa, cydan, denali-medical-ii.

## From c1 (batches 1-2)
- X1/R2 re-judge (classified, still members): acadia-pharmaceuticals, addex, affimed (underwritten offering), akari,
  alimera, aradigm, aurinia, aveo.
- 3com-corporation: firm's year 1996, 12 years after 3Com's listing: D8 / X1 check (the firm's 2012 post "The Big
  Score" names "the funding of Bob Metcalfe and 3Com": read whether it claims NEA's own funding).
- american-pathology-partners: NEA's $75M founding equity commitment: R1 control check.
- Base defects: advanced-cardiovascular carries 2018 and Actions Semiconductor's description (parser bleed in the old
  eras? check); advanced-cardiac-therapeutics became EPIX Therapeutics; 3-v-biosciences now Sagimet (merge listed);
  anterior: Sequoia's note says Sequoia led the A; VentureBeat says NEA led.
- amplitude: NEA's is the 1990s calendaring company; the prefilled float was Amplitude Inc's (cleared).
- Tooling: judges' shared scratchpad files collided (q1.log, b1.txt); next briefs: per-tag subfolders.
- advanced-cardiovascular: confirmed a copy error in the firm's own CMS (description and year 2018 duplicated from
  Actions Semiconductor), not a parser bleed; the 2008 archive row (Advanced Cardiovascular Systems) governs; never read
  entry_date off the CMS year for this row.

## From c12 (batches 23-24)
- Verdicts (kept): not_member harvard-experiment-fund, indous-ventures-llc (traps), exploramed-ii-inc (D5, medium:
  review), info-edge (X1), everside-health (R1 control); uncertain future-retail (listed company; X1 likely).
- Merges: onshape <- belmont-technology ; newglobe / bridge-international-academies ; fenris-creations / ccp-games ;
  tamr <- data-tamer ; alfred <- hello-alfred ; (also listed above: zhone, aetherflux, imergy, paladina/everside).
- A/B MUST CHECK: chinaway-technologies-limited marked $2.2B as G7 on the judge's own knowledge of the identity (no
  source ties Chinaway to G7): cite or revert.
- Sibling alignments: aetherflux (a16z below_1b -> 1b_plus $2B, May 2026 B); ccp-games (a16z acquired -> private,
  management buyback 2026); enverv (Benchmark unknown -> acquired by Semtech).
- identity_unresolved: gaov, gtel. status unknown ~20 (zyngenia, 3jam, avos, fetchr, huddler, koozoo, likelihood, lsf).

## From c11 (batches 21-22)
- Verdict (kept): upwork-formerly-odesk not_member (D8; matches the trap).
- X1 re-judge (classified, membership open): verona-pharma, vistagen-therapeutics, xenon-pharma, x4-pharmaceuticals (a
  $20M private placement closing with the 2017 Arsanis IPO; check for an NEA round in private X4 before the 2019
  reverse merger). vitesse-semiconductor stays a member (Spectra/NEA on the board from 1987, pre-IPO).
- R1 control checks: trivascular (2008 buyback from Boston Scientific), xcel-pharmaceuticals (2001, Elan products).
- New marks to A/B: world-labs $8.2B (AMD all-stock agreement 2026-09-29, unclosed: private at the agreed price),
  tulip $1.3B, wispr $2B, uniphore $2.5B (stale).
- Sibling: weaviate (NEA Amsterdam/NL from the 2023 release vs Battery SF/US): check current HQ before aligning.

## From c4 (batches 7-8)
- R3 (recorded in decisions): not_member exploramed-iv, exploramed-v, foundry-therapeutics-1 (exploramed-ii-inc already
  not_member by c12).
- Re-judge: erytech (X1, Public/PIPES); eci-acquisition-holdings (R1 control check).
- Renames: element3-health -> Grouper (2024-01); erytech -> Phaxiam (liquidated 2025-06: defunct).
- exent: prefilled acquired unconfirmed.
- Sibling: forethought (8VC private -> acquired by Zendesk 2026-03). elevenlabs country disagreement across siblings
  (US vs PL): not rule 10, note only.

## From c6 (batches 11-12)
- TOOLING DEFECT: evidence-pack.py's norm() strips "therapeutics"/"health"/"bio", so a site record can attach to a
  namesake (Intrinsic Therapeutics' record on `intrinsic`, the VMware-acquired security company). Fix norm and list
  every row whose site record differs from its own site_url, then have those rows re-checked.
- Merge: liquidia-corporation <- liquidia-technologies (flagged identity_conflated).
- X1 re-judge: interleukin-genetics, intermune, inventiva-pharma, leonabio (is Athira Pharma), lexicon-pharmaceuticals,
  marker-therapeutics, mei-pharma (now Lite Strategy).
- letgo: D8 question (NEA's 2016 stake possibly consideration from the Wallapop US combination): check.
- Sibling: lithium-technologies (Benchmark carries the same wrong $4.8M float; acquired): align Benchmark.
- Renames: iobeam -> Timescale -> TigerData; Mashape -> Kong; MediSys EduTech shows as MedRC EduTech.
- koudai needs_web_value (A/B). status unknown: learnup, legato-medical, luminate-wireless.
- Pack-mismatch check (evidence-pack norm defect): 5 rows got another row's site record; 4 are genuine twins
  (cohere-networks, liquidia-technologies, climate-corp, players-tribune-inc -> the-players-tribune: add merge), 1 wrong
  (intrinsic, caught by c6). Pack regenerated with the fixed norm before the delta.

## From m2
- Merges (legal-name twins, flagged identity_conflated): timescale <- 440-labs ; addthis <- clearspring ; eegeo <- kimble ;
  fugue <- luminal ; upskill <- apx-labs ; evenly <- cloudline ; goji-solutions <- goji-food ; snagfilms <- viewlift ;
  benchprep <- watermelon-express ; fightcamp <- hykso ; playvs <- play-versus ; deltastream <- araz ;
  outrider <- azevtec ; flox <- floxdev ; zosano <- zp-holdings ; logikcull <- logik-systems ;
  tabbedout/union <- atx-innovation ; dots-technology-corp <- dots-devices ; hearsay-social <- hearsay-labs ;
  the-players-tribune <- players-tribune(-inc) ; nuelle <- exploramed-nc6 ; reneo-pharmaceuticals/onkure ;
  videology <- tidaltv.
- Out pairs (no merge): respira/portaero; wine-mosquito/coravin; experiment-fund-llc = harvard-experiment-fund (D5).
- snagfilms: reads defunct, but the same issuer (ViewLift) was bought by DAZN 2026-05: acquired.
- fightcamp city: Costa Mesa (filing) vs IVP Newport Beach.
- Borderline members at medium (A/B): agenebio, quick-hit, cyren-call, jobfox (name-match seats, no NEA source).

## From c10 (batches 19-20)
- Verdicts (kept): not_member D8 synopsys (stock from selling Logic Modeling, 1994); X1 sunesis, supergen, tele-atlas
  (medium), telebit-corp (medium), trillium-therapeutics. strongbridge-biopharma open under X1 (F1 has it).
- AT REBUILD: sunesis is a merge canonical now not_member, so viracta-therapeutics-formerly-sunesis resurfaces: give it
  its own not_member verdict in the delta.
- Recall candidate: Logic Modeling (the member behind Synopsys, per the firm's archived page).
- Merges written: tigerdata <- timescale, 440-labs-inc; spring-mobile-solutions <- spring-wireless; spyglass-pharma <-
  spyglass-ophthalmics; testmart <- technical-communities; philo <- tivli.
- Sibling: tcv testmart (defunct -> private, site live 2026); felicis tivli (acquired -> renamed Philo 2013); YC Super
  copied another company's defunct.
- tri-alpha-energy private at $6.0B (signed, unclosed merger with Trump Media, S-4): A/B check.

## From F1 (X1 sweep)
- 42 rows decided: 31 not_member (listed purchase), 10 member (pre-IPO round documented), 1 uncertain (future-retail).
- FINDING: the firm's Public/PIPES label (and its year) is wrong on every pre-1995 row a filing could test (SGI,
  Telebit, Vitesse, RF Monolithics, Cirrus Logic: NEA partners on the boards before the IPOs). Re-check the pre-1995 rows
  ruled out on the label alone: dallas-semiconductor (c3), nellcor (F1, medium), immunex-corporation (c5).
- OTC quotation read as listed: champions-oncology, interleukin-genetics, strongbridge-biopharma (medium; if Erik rules
  a pre-exchange placement a venture entry, Strongbridge enters at Growth, Dec 2014).
- RECONCILE with F2: caremark-rx-inc is a member (NEA VI Series A 1993-09, pre-IPO 1995) per F1; F2's line must agree.

## From the stage pass s3
- 16/103 staged; 87 undetermined with funding_rounds recorded.
- Membership fixes: heliogen-inc (Forms 3/4 filed by Krishna Kolluri and NeoTribe Ventures, his firm after NEA: not_member,
  T4); satsuma-pharmaceuticals-inc and neurometrix-inc (X1: NEA money only into the listed companies).
- houzz: Sequoia's row calls the Dec 2011 round a Series A; VentureBeat calls it the Series B (sibling note).
- wheelhouse: the firm's 2014 year is likely its Lyric investment (Wheelhouse spun out of Lyric 2022).

## From the stage pass s4
- 10/102 staged; 92 undetermined with funding_rounds.
- Membership doubts: pcorder (IPO prospectus shows no NEA holding; Barris a director; stake may sit in parent Trilogy);
  dura-pharmaceuticals (1993 purchase possibly into the listed company: X1 check).
- first_seen/entry corrections noted in rows: broadview (NEA by 1999), actelis (Morris on the board by 2000).

## From the stage pass s2
- 21/103 staged. Fix batch 2 (membership): amisys-managed-care (R1: 1994 buyout from AIG with Greylock and ABS);
  tempest-therapeutics (NEA's Millendo stock carried through the 2021 reverse merger; no NEA fund among legacy Tempest's
  holders: merger stock, the imara/glycomimetics reading); premier-laser-systems-inc (X1 check).
- Rows with only a stage and other columns open (microcide, lumisys, premier-laser): the delta prepare queues them.

## FIX BATCH 2 (to run after s1, s5): heliogen-inc (T4), satsuma-pharmaceuticals-inc, neurometrix-inc (X1), pcorder
  (Trilogy?), dura-pharmaceuticals (X1), amisys-managed-care (R1), tempest-therapeutics (merger stock),
  premier-laser-systems-inc (X1).

## From the stage pass s1
- 19/103 staged. Merge: china-health-citic <- citic-pharmaceuticals (same description and acquirer).
- brightkite: NEA's stake came through Limbo Inc., which merged with Brightkite and took its name (note only).
- NOTE-JOIN DEFECT HIT: s1 recorded judgments-s1b.py twice; 48 of its 53 rows kept only the s1b sentence. Restored by
  scratch/repair-notes.py (replay of all out files in mtime order, written under the record lock). Write-back: the
  record defect (prev.update before the join check) still bites; propose the run.py fix again.
- strive-health: a Modern Healthcare headline reports a $1.8B valuation (Sept 2025); ab1 checks it (R6 too).

## From the stage pass s5
- 26/102 staged. Merges written: iomai-corporation <- intercell-usa-inc; zhone-technologies <- zti-merger-subsidiary-iii-inc.
- Fix batch 3 (membership): arca-biopharma-inc (2015), aryx-therapeutics-inc (2008) X1; censtor-corp-ca,
  graphix-zone-inc-de, opta-food-ingredients-inc-de (13G-only holdings: X1 check).
- mode: carries stale entry_stage_source/citation/confidence keys on an undetermined stage: clear at the verify fixes.
- careerbuilder (Class B preferred, first venture round) and tripod stay undetermined (the retired first-round convention).
- mecommerce is ThirdLove's parent: defunct (shared with Felicis) doubtful: check.

## From ab2 (momentum slice + duty 6)
- 43 momentum rows checked 2026-09-30, none at $1B+ (26 now web_verified to their latest round).
- Duty 6: 51 unicorn-list hits settled (namesakes noted: amber-therapeutics, shape-therapeutics, eucalyptus-systems, divvy).
- Verify clean-up: stash carries valuation_source unicorn_list with no figure; mode carries stage source keys on undetermined.

## From ab1 (private $1B+)
- 55/55 carry a cited non-vendor mark; cite_pending 11 (bloomreach, bytedance-toutiao, chinaway, collective-health,
  genies, iobeam, mindtickle, physical-intelligence, splashtop, tigerdata, world-labs); stale 27.
- Merge: tigerdata <- iobeam (added).
- radiology-partners stays a member, flagged for Erik under R6 (NEA the only institutional funder until 2019; one of 11
  board seats; physicians hold about a third).
- Rule-10 band/status disagreements to align at ingest: chaos (8VC, Accel), cowboy-space (a16z), cuspai (Lightspeed),
  sentry (Accel), grubwithus (a16z, First Round: defunct vs GOAT). Figure-only differences (same band): elevenlabs,
  instabase, plaid, world-labs, anyscale, databricks (Battery $134B).

## From F5 (fix batch 2+3)
- not_member: heliogen-inc (T4), satsuma, neurometrix, aryx, dura (X1), pcorder (a Trilogy subsidiary), graphix-zone
  (X1 + D8; StarPress Multimedia possibly the venture position, unestablished), amisys-managed-care (R1 control),
  tempest-therapeutics (D8 merger stock). members kept: premier-laser-systems (NEA IV notes Dec 1993; flag: D8 if the
  notes were part of the Proclosure technology price), censtor (never listed; defunct), opta-food-ingredients (medium).
- Cross-book: Greylock's AMISYS reads member on the same 1994 buyout (report; membership is not a rule-10 column).
