"""PRO-82: the four rows the grind left open, settled by web search on 2026-10-01 (WebSearch 2-5 of the session's 200)."""
import importlib.util
from pathlib import Path
spec = importlib.util.spec_from_file_location("gl", Path(__file__).with_name("gl.py"))
gl = importlib.util.module_from_spec(spec); spec.loader.exec_module(gl)
C, post, rnd, verdict = gl.C, gl.post, gl.rnd, gl.verdict
L = []
u = post("the-garden-a-peoples-university")
L.append(C("the-garden", dispute=("country",), status="unknown", country="GB", city="London", stage="Seed", stage_src="web_verified", stage_conf="high", stage_cite=u, entry_date="2022-07",
    rng="below_1b", focus="Consumer & Marketplaces",
    note="Live and on-demand talks by academics and experts, 'a people's university' (London; founded by Sophie Adelman of Multiverse); GBP 3M in seed funding led by Index and Village Global (the firm's post, 2022-07-13; Tech.eu), Hannah Seal the partner; no later round and no outcome on any surface read; the pre-filled AU is a name join",
    rounds=[rnd("2022-07-13", "Seed", None, "Index Ventures, Village Global", True, u, "firm")]))
L.append(C("quixotic", status="defunct", country="US", stage="undetermined", rng="below_1b", focus="Crypto & Web3", flags=["city_unknown", "country_prior"],
    note="NFT marketplace on the Optimism network (Fanbase Labs, Inc., founded 2021; the firm's 2023 page files it under the slug 'fanbase'); renamed Quix and wound down in 2023; which round the firm joined is not on any surface read", rounds=[]))
L.append(C("dot-product", status="private", country="US", stage="undetermined", rng="below_1b", focus="AI & Applied AI", flags=["city_unknown", "country_prior"],
    note="AI coworkers for operations and support teams (dotproduct.xyz; founded 2024 by a former Pipe CTO and an early Coinbase engineer); on the firm's list from 2025; a 2024 round of about $6M with Index and angels is carried only by vendor profiles, so the round is not on record (Rule A)", rounds=[]))
L.append(verdict("v-watch", "not_member", "life_sciences_desk (decisions.md D3): V-Watch (Strasbourg), a clinically validated ambulatory sleep-monitoring device company, on the firm's 2014 list only and with no technology-team partner; a medical-device position of the life sciences practice, which became Medicxi in 2016 with its whole book",
                 ec="site_listing", conf="medium", cite=gl.Q["v-watch"].get("wayback_first_link")))
gl.write("open-rows", L)
