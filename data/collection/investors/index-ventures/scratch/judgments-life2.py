"""PRO-82: the four rows whose desk the 2008-2025 captures did not show, settled before the rebuild (decisions.md D3).
directmedica: the firm's 2002 pages file it under Life Sciences (Healthcare Infrastructure). novocure, infection-control,
diartis: healthcare companies of the practice by what they are; the firm's later life lists were not captured for them."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gl", H / "gl.py")
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
IA = json.loads((H.parent / "sources/wayback/archive-facts.json").read_text())["ia"]
first = lambda s: gl.Q[s].get("wayback_first_link")
D3 = "; the practice became Medicxi in 2016 with its whole book"
L = [
 gl.verdict("directmedica", "not_member", "life_sciences_desk (decisions.md D3): the firm's own pages of 2001-2002 file it under 'Life Sciences and eHealth', then under Life Sciences / Healthcare Infrastructure beside Medicentrix (a pharmacists' portal and marketplace, Paris)" + D3,
            ec="site_listing", conf="medium", cite=[e for e in IA["directmedica"]["desk"] if e["value"] == "life"][0]["capture_url"]),
 gl.verdict("novocure", "not_member", "life_sciences_desk (decisions.md D3): a medical device company (the Novo-TTF tumour treating fields device) funded in 2009 beside Pfizer and Johnson & Johnson (the firm's own news item of 2009-10-02); a healthcare position like Micromet, on the firm's 2010-2014 lists" + D3,
            ec="site_listing", conf="medium", cite=first("novocure")),
 gl.verdict("infection-control", "not_member", "life_sciences_desk (decisions.md D3): a healthcare company by its name and nothing else on record (the firm's 2008-2013 lists carry the name without a technology sector or partner); ruled with the practice" + D3,
            ec="site_listing", conf="low", cite=first("infection-control")),
 gl.verdict("diartis", "not_member", "life_sciences_desk (decisions.md D3): Diartis Pharmaceuticals, a Swiss drug developer on the firm's 2012-2013 lists" + D3,
            ec="site_listing", conf="medium", cite=first("diartis")),
]
print([(x["slug"], bool(x.get("citation"))) for x in L])
gl.write("life-desk-2", L)
