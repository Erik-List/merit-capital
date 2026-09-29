"""Rule-10 alignment from the 20VC run (PRO-76), approved by Erik 2026-09-28
("fix the valuation or status revealed in 20VC's collection run for other
investors, afterwards ingest"). One classification line per stale row, written
to scratch/align/<investor>.jsonl and recorded into that investor's book with
`run.py record --investor <investor>` (per-key merge; a key Erik set by hand
is kept). Every citation was read 2026-09-28 (verify-url.py). The stale side
was found by scratch/align/compare.py; Factory's September 2026 round was
found here, so 20VC's own Factory row is corrected with the others.

Usage: python3 align.py [--dry]   (--dry writes the jsonl files, records nothing)
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
WHO = "agent-align-pro76"
TAG = "Aligned 2026-09-28 from the 20VC run (PRO-76, rule 10)"

WORKOS = "https://siliconangle.com/2026/03/03/jetstream-security-guild-ai-workos-land-fresh-funding-amid-growing-agentic-ai-infrastructure-push/"
FUSE = "https://www.balderton.com/news/fuse-energy-hits-5bn-valuation-in-its-third-year/"
POOLSIDE = "https://www.forbes.com/sites/jonmarkman/2026/08/24/nvidia-pays-poolside-6b-to-license-its-model-factory-and-109-workers/"
FACTORY = "https://techfundingnews.com/factory-jumps-to-5b-in-5-months-with-200m-for-its-ai-droids/"
COGNITION = "https://techcrunch.com/2026/09/08/cognition-hits-48b-valuation-signaling-investors-believe-ai-coding-is-far-from-a-winner-take-all-market/"


def value(slug, rng, usd, asof, cite, note, flags=(), clear=()):
    r = {"slug": slug, "who": WHO, "valuation_range": rng, "valuation_usd": usd,
         "valuation_source": "web_verified", "valuation_range_source": "web_verified",
         "valuation_asof": asof, "valuation_citation": cite, "valuation_confidence": "high",
         "note": f"{TAG}: {note}"}
    if flags:
        r["flags"] = sorted(flags)
    if clear:
        r["clear_flags"] = sorted(clear)
    return r


def status(slug, st, note):
    return {"slug": slug, "who": WHO, "status": st, "note": f"{TAG}: {note}"}


FACTORY_NOTE = ("Factory 'has raised $200 million at a $5 billion valuation, more than tripling the "
                "$1.5 billion price tag it carried five months ago' (Tech Funding News, 2026-09-16, after "
                "The Wall Street Journal and Reuters of 2026-09-15), following the $150M Series C at $1.5B "
                "(April 2026) and a $120M extension at $4B (July 2026).")
COGNITION_NOTE = ("the $2B Series E at $48B (TechCrunch, 2026-09-08; led by Andreessen Horowitz, Accel, "
                  "Founders Fund, General Catalyst and Avenir), as in the Bain Capital Ventures, Ribbit and "
                  "20VC rows; it supersedes the $10.2B of September 2025 and the $26B of May 2026.")

LINES = {
    "accel": [status("kevin", "defunct",
        "defunct. 'Fintech kevin declared insolvent by Vilnius court': bankruptcy proceedings opened and an "
        "insolvency administrator appointed (The Paypers, September 2024, "
        "https://thepaypers.com/fintech/news/fintech-kevin-declared-insolvent-by-vilnius-court); the Bank of "
        "Lithuania revoked the payment-institution licence of Kevin EU (October 2024).")],
    "sequoia-capital": [
        status("nxyz", "acquired",
            "acquired. 'Snowflake Inc. entered into a definitive agreement to acquire NXYZ, Inc.' (MarketScreener, "
            "2023-07-26, https://www.marketscreener.com/quote/stock/SNOWFLAKE-INC-112440376/news/"
            "Snowflake-Inc-entered-into-a-definitive-agreement-to-acquire-NXYZ-Inc-44572045/); the nxyz API was "
            "retired on 2023-08-23."),
        value("factory", "1b_plus", 5000000000, "2026-09-15", FACTORY,
            FACTORY_NOTE + " The entry stage stays as recorded (model-read) and is flagged cite_pending, which "
            "a $1B+ row requires (rule 4).", flags=["cite_pending"]),
    ],
    "lightspeed": [value("workos", "1b_plus", 2000000000, "2026-03-03", WORKOS,
        "'WorkOS's $100 million Series C round was raised at a valuation of $2 billion and was led by Meritech "
        "Capital Partners LP and Sapphire Ventures' (SiliconANGLE, 2026-03-03), as in the 20VC row.")],
    "creandum": [value("fuse-energy", "1b_plus", 5000000000, "2025-12-18", FUSE,
        "the value this row left open: 'Fuse Energy hits $5bn valuation in its third year' on the $70M Series B "
        "(Balderton's post, 2025-12-18), as in the Balderton, Ribbit and 20VC rows.")],
    "redpoint-ventures": [value("poolside", "10b_plus", 12000000000, "2026-08-24", POOLSIDE,
        "$12B, the value of Nvidia's August 2026 deal (a $6B licence of the Model Factory and $1B invested at "
        "a $12B pre-money; Forbes, 2026-08-24; SaaStr's write-up of the 20VC x SaaStr episode, 2026-08-27), as "
        "in the Bain Capital Ventures, Felicis, Point Nine and 20VC rows; the $3B of the October 2024 Series B "
        "is superseded.", clear=["needs_web_value"])],
    "khosla-ventures": [
        value("factory", "1b_plus", 5000000000, "2026-09-15", FACTORY, FACTORY_NOTE),
        value("cognition", "10b_plus", 48000000000, "2026-09-08", COGNITION, COGNITION_NOTE,
              clear=["needs_web_value"]),
    ],
    "lux-capital": [
        value("factory", "1b_plus", 5000000000, "2026-09-15", FACTORY, FACTORY_NOTE),
        value("cognition", "10b_plus", 48000000000, "2026-09-08", COGNITION, COGNITION_NOTE),
    ],
    "8vc": [value("cognition", "10b_plus", 48000000000, "2026-09-08", COGNITION, COGNITION_NOTE)],
    "general-catalyst": [value("cognition", "10b_plus", 48000000000, "2026-09-08", COGNITION,
        COGNITION_NOTE + " General Catalyst co-led the round.")],
    "20vc": [value("factory", "1b_plus", 5000000000, "2026-09-15", FACTORY, FACTORY_NOTE)],
}

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    for inv, lines in LINES.items():
        p = HERE / f"{inv}.jsonl"
        p.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n")
        print(f"== {inv}: {len(lines)} line(s) -> {p.name}")
        if dry:
            continue
        r = subprocess.run([sys.executable, "scripts/run.py", "record", "--investor", inv, str(p)],
                           cwd=ROOT, capture_output=True, text=True)
        print((r.stdout + r.stderr).strip()[-1500:])
        if r.returncode:
            sys.exit(f"record failed for {inv}; stopping")
