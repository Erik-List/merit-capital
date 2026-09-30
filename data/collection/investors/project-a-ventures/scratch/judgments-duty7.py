"""Duty 7 adjudication (PRO-102): the blind 5% re-judgment (documentation/duty7-blind.json).
Note-free patches; the ESV note is rewritten under the record lock (record-note-join bug)."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from judge_lib import cls, write  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "scripts"))
from shared_throttle import exclusive  # noqa: E402

REG = "https://brasilapi.com.br/api/cnpj/v1/17466851000127"
L = [
    cls("esv-digital-brazil", status="defunct", flags=["unstable"],
        extra={"status_citation": REG}),
    cls("gabi", flags=["unstable"]),
]

ESV_NOTE = ("Performance-marketing agency, São Paulo: a joint venture the firm lists as its own ('Joint Venture', founded "
            "01/2013) from its Brazilian company-builder period with the French group ESV Digital, which bought Project "
            "A's Adtrade in 2014. No round (a joint-venture stake, judged as the firm's listed position like HV's "
            "Audible.de). Defunct: the Receita Federal record for ESV DIGITAL AGENCIA DE PUBLICIDADE LTDA. (ESVBR, CNPJ "
            "17.466.851/0001-27) has read INAPTA since 2022-06-07 for failing to file returns; the ESVBR site's last "
            "post is April 2018 and esvbr.com is now a domain-sale page. No sale is on record. Found by the duty-7 blind "
            "judge; the grind had read it unknown.")

if __name__ == "__main__":
    write("duty7", L)
    p = Path(__file__).resolve().parents[1] / "companies" / "classification.json"
    with exclusive("record-project-a-ventures"):
        d = json.loads(p.read_text())
        rows = d.get("companies", d)
        rows["esv-digital-brazil"]["note"] = ESV_NOTE
        p.write_text(json.dumps(d, indent=1, sort_keys=True))
    print("esv note rewritten")
