"""f1b: follow-up to F1. The three pre-1995 rows ruled not_member on the Public/PIPES label alone (dallas-semiconductor,
nellcor, immunex-corporation), checked for an NEA partner on the board or NEA funds in a holder table before the IPO.
Only dallas-semiconductor gets a line: the record dates its listing and its pre-IPO backer. Nellcor and Immunex are
left as recorded (no source shows NEA either before or after the listing beyond the firm's own year).
Run: NQ_TAG=f1 python3 judgments-f1b.py"""
import judge_lib as jl
from judge_lib import verdict

TAIL = "X1: a listed purchase (decisions.md); if Erik rules a PIPE a venture entry, this row enters at Growth."
DALLAS_PROXY = "https://www.sec.gov/Archives/edgar/data/749420/0000950134-95-000322.txt"

L = [
    verdict("dallas-semiconductor", "not_member",
            "Dallas Semiconductor went public on the NYSE in 1987 (encyclopedia.com company history). Its founding "
            "capital in 1984 came from Southwest Enterprise Associates, whose general partners are C. Vin Prothro, "
            "the company's chairman since 1984 (1995 proxy), and NEA Partners Southwest, which files from NEA's "
            "Baltimore office with Charles Newhall signing (SEA's 13G of 2000-02-14, EDGAR CIK 729085). Decisions D1 "
            "lists Southwest as an external affiliate run by its own team in Dallas (the Chemicals & Materials "
            "reading), so SEA's 1984 money is not NEA's; no NEA fund or partner appears in the company's filings "
            "before the listing, and the firm dates NEA's own entry 1990, labelled Public/PIPES. Flag: if Erik reads "
            "SEA as an NEA sleeve (the Spectra test: an NEA Partners entity at NEA's office as general partner), this "
            "row is a member from 1984, round not named. " + TAIL,
            ec="fund_filing", conf="medium", cite=DALLAS_PROXY),
]

jl.write("f1b", L)
