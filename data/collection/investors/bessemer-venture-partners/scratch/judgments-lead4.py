"""Lead overrides 4 (2026-10-06): status fixes surfaced by the graduation pass."""
import judge_lib as jl
lines = [
    jl.cls("visor", status="acquired", rng="below_1b",
           note="Status 2026-10-06: acquired. The company's own blog (2026-03-03, "
                "https://www.visor.us/blog/how-to-export-your-visor-data-before-we-shut-down/) says 'On July 31, 2026, "
                "Visor will shut down as part of our company's transition to MCP Manager under Usercentrics': the "
                "company continues as MCP Manager inside Usercentrics, so it reads acquired, not defunct; the price "
                "and date of the Usercentrics deal were not found."),
]
jl.write("lead4", lines)
