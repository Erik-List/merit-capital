"""PRO-83 rule-10 alignments on this book's side, and the weak-join quarantine: the pre-filled SEC floats and
public flags on rows whose CIK join is a name collision are cleared so nothing publishes them."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("jl", Path(__file__).with_name("judge_lib.py"))
jl = importlib.util.module_from_spec(spec); spec.loader.exec_module(jl)
c, loc, V = jl.c, jl.loc, jl.V
Q = {"is_public": False, "public_since": None, "valuation_asof": None, "valuation_source": None,
     "valuation_confidence": None, "valuation_range_source": None}
L = [c(s, extra=dict(Q)) for s in ("beeline", "gaia", "pace", "paid", "wave", "beagle", "ciao", "gameplan", "greenhouse",
                                    "pronto", "protagonist", "sunrise", "tilt")]
L += [
    c("fina", status="defunct",
      note="Beginner crypto and investing app (fina, heyfina.com, now for sale; Berlin, founders Leonie Riviere and Tim Oliver Pietsch); defunct as "
           "in the Visionaries Club book; on the firm's lists 2022-2024 (logo 2022-10), on no post read; the pre-filled acquired/SA is a one-word "
           "Wikidata join and is disputed"),
    c("popup", status="private",
      note="No-code storefront personalisation for online merchants; the firm's post of 2022-11-23: 'Popup raised $3.5M in pre-seed round funding "
           "led by Accel, joined by us'; private as in the Accel and 20VC books (US); on the firm's lists only 2022-2024"),
    c("riff", status="private",
      note="Voice-first chat for remote teams (Riff Technologies; CEO Isabel Bescos); the firm's post of 2020-08-20: 'back Isabel and Matthew ... "
           "as part of a $1.5M seed round led by our friends at Balderton'; Companies House 12611399 active, private as in the Balderton book; "
           "not the Oslo Riff in the Northzone book"),
    c("troop", **loc("US", "New York"), status="private",
      note="Collective shareholder activism for retail investors (Troop, founded in Brooklyn; TechCrunch, 2022-11-02); 'We are excited to support "
           "Troop' (the firm's 2021 post), no round named; New York and private as in the Northzone book"),
    c("safara", status="defunct",
      note="Hotel booking with cashback (the original Safara, founders Maya Poulton and Joey Kotkins, 2020); it shut down during COVID and the Resy "
           "founders bought its remnants in 2021 to build Safara Travel, Inc. (Los Angeles), a different company (Sequoia's row); no round named"),
    c("cymmetria", status="defunct",
      note="Cyber deception platform; on the firm's Fund III seed list (2015-09-21) and its 2015-06-29 post 'Cymmetria exits stealth, having "
           "raised a seed round with Seedcamp' (alongside Felicis and Y Combinator); $9M Series A led by Sherpa Capital (Dark Reading); Stage "
           "Fund bought it in Sep 2019 and its employees filed for its liquidation in Dec 2019 (Calcalist), so defunct as in the Felicis book"),
]
if __name__ == "__main__":
    jl.write("fixups-03", L)
