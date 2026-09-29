# Web pass 5 (PRO-169): the momentum slice's four unrecorded checks, and Trulioo's missing mark. Judge: this session, 2026-09-29.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _post import post
J = [
 {"s": "trulioo", "v": 1750000000, "va": "2021-06", "vc": post("trulioo-closes"), "vs": "web_verified",
  "hc": "CA", "hcc": post("trulioo-closes"),
  "n": "Correction: the row carried no figure and read below $1B, against its own note. The $394M Series D TCV led in June 2021 valued Trulioo at $1.75B (the firm's own copy of the release, 'Trulioo closes USD 394M Series D led by TCV at 1.75B valuation'); no later priced round found (Google News sweep, 2026-09-29). Vancouver."},
 {"s": "arize-ai", "vr": "below_1b", "vc": "https://pulse2.com/arize-ai-70-million-series-c-closed-for-ai-observability-and-llm-evaluation-company/", "va": "2025-03",
  "n": "Momentum check (2026-09-29): the $70M Series C of March 2025 led by Adams Street, with TCV among existing investors, disclosed no valuation (Pulse 2.0); no unicorn mark found. Below $1B."},
 {"s": "cloudsmith", "vr": "below_1b", "vc": "https://siliconangle.com/2026/04/23/software-artifact-management-startup-cloudsmith-raises-72m/", "va": "2026-04",
  "n": "Momentum check (2026-09-29): TCV led the $72M Series C of April 2026 (SiliconANGLE); no valuation disclosed and no unicorn mark found. Below $1B."},
 {"s": "layerx", "es": "Growth", "esc": "https://techcrunch.com/2025/09/01/layerx-uses-ai-to-cut-enterprise-back-office-workload-scores-100m-in-series-b/", "ess": "web_verified", "econf": "high", "ed": "2025-09",
  "vr": "below_1b", "vc": "https://techcrunch.com/2025/09/01/layerx-uses-ai-to-cut-enterprise-back-office-workload-scores-100m-in-series-b/", "va": "2025-09",
  "n": "Correction: TCV led the $100M Series B of September 2025, 'marking the U.S. fund's first investment in a Japanese startup' (TechCrunch, 2025-09-01): Growth. The company declined to disclose its valuation; no unicorn mark found (momentum check, 2026-09-29). Below $1B."},
]
