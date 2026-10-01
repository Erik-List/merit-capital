"""Cross-book pass cx1 (PRO-99, rule 10): Kleiner Perkins rows only. Plan: cross-plan-cx1.json."""
import judge_lib as jl

# Read 2026-09-30 with WebFetch: Ormat's own release names the Blue Mountain plant and Cyrq Energy as the seller.
ORMAT = ("https://investor.ormat.com/news-events/news/news-details/2025/Ormat-Announces-the-Completion-of-Its-"
         "Acquisition-of-the-Blue-Mountain-Geothermal-Power-Plant-From-Cyrq-Energy/default.aspx")
# Read 2026-09-30 with WebFetch: "In 2023, Texas-based Blade Energy Partners Ltd. and AltaRock Energy formed a new
# company, Mazama Energy Inc."
BEND = "https://bendbulletin.com/2025/01/11/can-super-hot-rocks-under-newberry-volcano-produce-clean-energy/"

lines = [
    # kp_stale: the acquired status rested on a misread sentence; aligned with the Khosla row (unknown).
    jl.cls("altarock-energy-inc", status="unknown",
           note="Cross-book 2026-09-30 (rule 10, Khosla): the acquired status is withdrawn, because what Ormat "
                f"bought on 2025-06-18 was the Blue Mountain power plant, from Cyrq Energy ({ORMAT}), not AltaRock "
                "Energy. No sale or shutdown of the company is on record (it co-founded Mazama Energy with Blade "
                f"Energy Partners in 2023, {BEND}, and its own site is live but undated), so its state is not "
                "established: unknown, as the Khosla row reads."),
    # Note only: the row's values stand; its earlier note wrongly called the ICONIQ row a namesake.
    jl.cls("assured",
           note="Cross-book 2026-09-30 (rule 10): the ICONIQ row is this company, not a namesake; ICONIQ's own grid "
                "describes Assured as the AI engine for insurance claims and links assured.com, and Bloomberg's "
                "headline names Iconiq in the $1B round. Only the First Round row is the New York credentialing "
                "company."),
]
jl.write("cx1", lines)
