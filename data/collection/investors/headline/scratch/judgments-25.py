"""Duty 7 (COLLECTION.md s8): blind re-judgment of a random 5% (14 rows, seed 20260927,
scratch/blind-sample.json -> scratch/blind-rejudge.json). Seven rows disagreed on a field;
Scopely's is the blind judge's error (an acquired row carries no figure and reads below_1b in
every book; the CMS 'Growth 2016' label sets its stage under R4). Six are flagged unstable and
adjudicated here. Duty 9 swept the class behind Flowhub (a recall row staged 'Growth by
sequence' without checking the firm's earlier rounds): The Young Turks had the same error."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, rnd  # noqa: E402

FLOW = "https://www.newcannabisventures.com/cannabis-software-company-flowhub-raises-23-million/"
ADD_A = "https://www.prnewswire.com/news-releases/all-def-digital-raises-5m-series-a-financing-led-by-greycroft-partners-270228981.html"
ADD_SALE = "https://www.digitalmusicnews.com/2019/12/19/russell-simmons-all-def-digital-finds-buyer/"
TYT = "https://www.tubefilter.com/2017/08/08/the-young-turks-20-million-funding-jeffrey-katzenberg-wndrco/"
L = [
    cls("flowhub", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=FLOW,
        entry_date="2019-10-15", flags=["unstable"],
        note="Duty 7 correction: e.ventures co-led the $23M Series A with Evolv Ventures and Poseidon (New Cannabis Ventures, 2019-10-15), its first cannabis investment; the 2021 $19M strategic round was a follow-on, so the entry is Series A, not Growth.",
        rounds=[rnd("2019-10-15", "Series A", 23000000, "e.ventures; Evolv Ventures; Poseidon", True, FLOW, "press"),
                rnd("2021-10", "Strategic (unnamed)", 19000000, "Headline; Poseidon; Shawn Carter", True,
                    "https://www.prnewswire.com/news-releases/flowhub-announces-19-million-strategic-funding-led-by-headline-poseidon-and-shawn-jay-z-carter-301397403.html", "press")]),
    cls("tvsmiles", status="acquired", flags=["unstable"],
        note="Duty 7 correction: the app is now operated by Verve Group Europe GmbH (tvsmiles.tv imprint, https://tvsmiles.tv/en/imprint/; its LinkedIn page reads 'Now part of Verve Group'; the deal dates to December 2019): acquired, not unknown."),
    cls("all-def-digital", status="acquired", stage="Series A", stage_src="web_verified", stage_conf="high",
        stage_cite=ADD_A, entry_date="2014-08-06", flags=["unstable"],
        note="Duty 7 correction: e.ventures joined the $5M Series A led by Greycroft (PR Newswire, 2014-08-06). All Def Digital stopped operating in mid-2019 and Culture Genesis bought its IP, channels and content library in December 2019 (Digital Music News): an asset sale after the wind-down reads acquired (COLLECTION.md s6). The a16z row reads defunct: cross-investor item.",
        rounds=[rnd("2014-08-06", "Series A", 5000000, "Greycroft Partners", True, ADD_A, "press")]),
    cls("the-young-turks", stage="Series A", stage_src="model", stage_conf="low",
        note="Duty 9 sweep (the Flowhub class): the 2014 raise was a $4M convertible note, and Tubefilter calls the August 2017 $20M round 'TYT's first mainstream raise' (https://www.tubefilter.com/2017/08/08/the-young-turks-20-million-funding-jeffrey-katzenberg-wndrco/): the first priced round reads Series A by sequence, not Growth; no page names the letter."),
    cls("ncircle", flags=["unstable"],
        note="Duty 7: the blind judge read BV Capital's entry as the August 2001 Series B from a VC-database snippet whose page did not load; no release confirms it, so the stage stays undetermined."),
    cls("test-ai", flags=["unstable"],
        note="Duty 7: the blind judge read acquired from a June 2023 interview ('decided to sell the majority of the company'); no buyer is named and test.ai redirects to icebergqa.com, so the status stays unknown."),
    cls("circadia", flags=["unstable"],
        note="Duty 7: the blind judge read US, Los Angeles from the November 2024 FDA release (Circadia Health, datelined Los Angeles, 250+ US nursing facilities); the release states no headquarters, so London stands, open to a relocation check."),
]
if __name__ == "__main__":
    write("duties-003", L, record="--dry" not in sys.argv)
