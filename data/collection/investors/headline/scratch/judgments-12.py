"""Stage pass, group 2 (BV Capital era; research agent stage-2.json, URLs checked with
verify-urls.py and the prospectus quotes read with an SEC user agent). Every row keeps
its researched rounds under funding_rounds, an empty or partial list meaning the search
ran (COLLECTION.md s6)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, note_plus  # noqa: E402
from research_lib import research, rounds_of  # noqa: E402

R = research(2)
def base(slug, **kw):
    return cls(slug, rounds=rounds_of(R[slug]), **kw)

SONOS_EX = "https://www.sec.gov/Archives/edgar/data/1314727/000119312518213468/d403417dex402.htm"
L = [
    base("shopping-com", stage="Growth", stage_src="web_verified", stage_conf="medium",
         stage_cite="https://www.sec.gov/Archives/edgar/data/1108482/000119312504177779/d424b1.htm", entry_date="2001",
         note="acq. by eBay, 2005 ($620M). BV Capital's stake came through Epinions, not DealTime: the Shopping.com prospectus (Epinions statements, note 8) says 'BV Capital, which holds 34% of the Series C Preferred Stock' (issued 2001, $11.8M); Epinions merged with DealTime in 2003 to form Shopping.com. The DealTime holder 'Bertelsmann Nederland B.V.' is the Bertelsmann corporate, not the fund. Series C, or B if BV was also in it: Growth either way."),
    base("cranite", stage="Growth", stage_src="web_verified", stage_conf="high", entry_date="2002-09",
         stage_cite=R["cranite"]["entry"]["url"],
         note=note_plus("cranite", "The company's release (2002-09-23): '$12 million in Series C financing' led by JK&B, 'BV Capital and Diamondhead Ventures join JK&B as new investors'; Jan Buettner to the board. Later fate not established.")),
    base("pronto-networks", status="unknown", stage="Growth", stage_src="web_verified", stage_conf="high", entry_date="2004-02",
         stage_cite=R["pronto-networks"]["entry"]["url"], flags=["model_disputes_source"],
         note="Pronto Networks (Pleasanton, Wi-Fi operations software). The company's release: '$11.3 Million in Series B Funding ... led by US and Europe based BV Capital' (February 2004); the 2003 first round was DFJ and Intel only. Still operating in 2016 (Delhi Metro Wi-Fi release), no exit found; the 'acquired' pre-fill is not supported."),
    base("myfab", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2009-06",
         note=note_plus("myfab", "The June 2009 release calls the BV Capital and Alven Capital investment (over EUR 5M) the 'zweite Finanzierungsrunde' after about EUR 2M from business angels at launch: the first venture round, Series A. EUR 5.0M @ ECB 2009-06-15 (EUR/USD 1.385) = $6.9M (a floor).")),
    base("fotolog", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2005-03",
         note=note_plus("fotolog", "BV Capital's $2.4M in March 2005 (Blog Herald 2005-03-30) was Fotolog's first outside venture money; unnamed in the report, above the era's $1.5M seed ceiling: Series A. 3i came in later.")),
    base("sonos", stage="Series A", stage_src="model", stage_conf="medium", entry_date="2005-07", flags=["cite_pending"],
         note=note_plus("sonos", "Entry read from two cited facts: the firm dates its entry 'Early 2005', and the 2018 S-1 exhibit dates Sonos's first preferred, the Series A, to July 25, 2005 (about $15.0M); BV Capital is party to the 2012 investors' rights agreement among the Series A to C holders. No page names BV in the Series A itself.")),
    base("sonim-technologies",
         note=note_plus("sonim-technologies", "BV Capital put $3M into the 'first round of institutional funding' (August to October 2002, $21.6M, co-led by 3i and Apax), Schilling to the board; the next named round was a Series C (2004), so the 2002 round's letter may have been B: stage left undetermined.")),
    base("angie-s-list", note=note_plus("angie-s-list", "The S-1/A ties BV Capital only to the April 2010 conversion (BV's AL BV Investment, Inc. exchanged for common and Series A preferred); the round BV bought around 2006 (LLC Class D units) is not named.")),
    base("expertcity", note=note_plus("expertcity", "The December 1999 $30M release (led by Sun and ZDNet) names Bertelsmann Ventures as a previous investor that joined again, so its entry was an earlier, unnamed round.")),
    base("fanhattan-inc", note=note_plus("fanhattan-inc", "The company's 2010 investors page listed NEA, Redpoint and BV Capital before launch: BV was in the first venture money, which no page names.")),
    base("k2-network", status="unknown",
         note=note_plus("k2-network", "Correction: in July 2012 K2 Network merged with its own subsidiary Reloaded Games and continued under that name (GamesIndustry.biz), which is not an exit; later state not established. The Khosla row reads 'acquired': cross-investor alignment item.")),
    base("rendition-networks", note=note_plus("rendition-networks", "Incorporated 1998 as imandi.com, renamed 2001; Opsware's 8-K/A gives Series A 1999, B 2000 and C 2004 without holders, so BV's series is not on record.")),
    base("rojo", note=note_plus("rojo", "BV's round (probably after February 2005) is not on record.")),
    base("moretv", city="Hamburg", clear=["city_unknown"],
         note="moreTV Broadcasting GmbH, Hamburg (PVR and EPG software 'maxPLUS'); BV Capital listed it 2008-2010 and not in February 2012, with no exit entry; no round or later fate found."),
    base("mr-ted"), base("citydeal"), base("darberry"), base("ebook"), base("experteer"), base("infiniroute"),
]
if __name__ == "__main__":
    write("stage-002", L, record="--dry" not in sys.argv)
