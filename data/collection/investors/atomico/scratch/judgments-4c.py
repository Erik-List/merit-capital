"""PRO-79 grind: IQube, the one listing name no source identifies."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(jl)

L = [jl.cls("iqube", status="unknown", rng="undetermined", stage="undetermined", grad="undetermined",
            flags=["identity_unresolved"],
            note="Listed on the firm's 2008 site (portfolio.php; its own page /OurPortfolio/IQube.xml is in the CDX, 2008-04-28 to 2008-09-08, but the Internet Archive refused this machine before it could be read); no press, filing or register record names an 'IQube' tied to Atomico (the only candidate, a Swedish investor 'IQUBE' in a vendor database, is unverified) -> the company cannot be named: undetermined in every outcome column, excluded from every metric")]

if __name__ == "__main__":
    jl.write("batch-004c", L)
