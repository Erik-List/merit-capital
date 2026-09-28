"""E1 delta, duty 7: blind re-judgment of 7 random desk rows (seed 20260928,
scratch/blind-sample-e1.json -> scratch/blind-rejudge-e1.json). Two real disagreements, both
ours, corrected and flagged unstable; the rest agree (spelling of accents aside)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write, rnd  # noqa: E402

OLIST = "https://www.baguete.com.br/noticias/01/08/2016/olist-tem-aporte-da-redpoint-eventures"
L = [
    cls("olist", stage="Series A", stage_src="web_verified", stage_conf="high", stage_cite=OLIST, entry_date="2016-08",
        flags=["unstable"],
        note="Duty 7 correction: Baguete (2016-08-01) names the desk's entry: Olist 'concluiu seu segundo round de investimentos, denominado Series A', led by Redpoint eventures (20%, Romero Rodrigues to the board, Gazeta do Povo). The CMS 'Early 2015' is the founding year, not the desk's entry.",
        rounds=[rnd("2016-08-01", "Series A", None, "Redpoint eventures", True, OLIST, "press")]),
    cls("smartbreak", city="Osasco", city_src="web_verified", flags=["unstable"],
        note="Duty 7 correction: the Brazilian company registry (CNPJ, active) puts the head office in Osasco, Greater Sao Paulo, not Sao Paulo itself."),
]
if __name__ == "__main__":
    write("e1-blind", L, record="--dry" not in sys.argv)
