# Mechanical fixes after the first pass (2026-09-29): countries on rows where only the city was given,
# bands for acquired rows whose status was pre-filled, statuses for listed rows, one missing flag.
US = ["calendly", "captivateiq", "collibra", "docusign", "figma", "fivetran", "gitlab", "honest-company", "houzz", "lucid",
      "netskope", "ninjaone", "notable", "notion", "people-ai", "pepper", "pinecone", "pontera", "ramp", "shopmonkey",
      "sierra", "smartling", "snowflake", "squire"]
J = [dict(s=s, hc="US") for s in US] + [
 dict(s="canva", hc="AU"),
 dict(s="backstory", hc="US", hconf="low", fl=["country_prior"], n="Country from the firm's US desk (an inferred value); no head office on record."),
 dict(s="enfusion", vr="below_1b"), dict(s="flipkart", vr="below_1b"), dict(s="wolt", vr="below_1b"),
 dict(s="alibaba", st="public"), dict(s="groww", st="public"),
 dict(s="clara", fl=["cite_pending"]),
]
