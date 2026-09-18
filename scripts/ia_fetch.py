"""Status-aware Internet Archive fetching, shared by every IA caller.

We cannot obey a rate limit we cannot see. Both IA callers used to run
`curl -sfL ... check=True`: `-f` turns any HTTP error into a non-zero exit, so
429 "slow down", 503 "temporarily offline" and 404 arrived as one generic
failure and were retried after a flat 3 s. IA's rule is that 429s ignored for
more than a minute earn an hour-long IP block that doubles on each recurrence,
so the retry loop was the block's cause. 775 of 816 logged IA failures were
rc=7, a TCP refusal in ~85 ms: the block, not overload.

Two regimes, opposite responses, so the caller must be able to tell them apart:

  firewall block     rc=7, refused in ~85 ms   -> stop the whole machine
  backend degraded   503, or CDX taking 5-30 s -> back off, keep going

Everything here goes through `shared_throttle.wait("ia")`, whose guarantee is
aggregate: the total across every process on the machine stays at the ceiling
however many sessions run.
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import shared_throttle  # noqa: E402

UA = "MeritCapitalResearch/1.0 (erik@meritcapit.al)"
DEFAULT_RETRY_AFTER = 60.0
MAX_503_BACKOFF = 60.0
# Headers IA's edge sets that say which regime we are in; logged on failure so
# the next investigation reads a log instead of re-deriving it from curl codes.
TELEMETRY = ("x-rl", "x-nid", "x-app-server", "x-location", "retry-after")


def _final_status(head: str) -> str:
    """Last HTTP status in a header dump (curl -L records every hop)."""
    codes = re.findall(r"HTTP/[\d.]+\s+(\d{3})", head)
    return codes[-1] if codes else "000"


def _retry_after(head: str) -> float:
    m = re.search(r"(?im)^retry-after:\s*(\d+)", head)
    return float(m.group(1)) if m else DEFAULT_RETRY_AFTER


def telemetry(head: str) -> str:
    bits = []
    for h in TELEMETRY:
        m = re.search(rf"(?im)^{re.escape(h)}:\s*(.+)$", head)
        if m:
            bits.append(f"{h}={m.group(1).strip()}")
    return " ".join(bits)


def _note_block(where: str, head: str) -> None:
    expiry = shared_throttle.cooldown("ia")
    left = max(0.0, expiry - time.time())
    print(f"  !! IA refused the connection ({where}) — firewall block signature.",
          file=sys.stderr, flush=True)
    print(f"     Machine-wide cooldown set: {left/60:.0f} min. Every session on "
          f"this machine now waits, so the block does not double.",
          file=sys.stderr, flush=True)
    if head:
        print(f"     {telemetry(head)}", file=sys.stderr, flush=True)


def _run(args: list[str], tries: int, where: str) -> tuple[bytes, str, str]:
    """Paced, status-aware curl. Returns (stdout, code, headers).

    `code` is the HTTP status as a string, or "rc<N>" for a transport failure.
    Never raises on an HTTP error and never turns one into an empty success:
    the caller decides what a 404 or an empty 200 means, which is what lets
    `cdx()` tell "matched nothing" from "the request failed".
    """
    last: tuple[bytes, str, str] = (b"", "rc-1", "")
    attempt = 0
    while attempt < tries:
        shared_throttle.wait("ia")
        with tempfile.NamedTemporaryFile(suffix=".hdr") as hf:
            r = subprocess.run(args + ["-D", hf.name], capture_output=True)
            head = Path(hf.name).read_text(errors="replace")
        if r.returncode == 7:
            # The firewall signature. Do not retry into it: that is what
            # doubles the ban. Stop the machine and hand the caller "rc7".
            _note_block(where, head)
            return b"", "rc7", head
        if r.returncode != 0:
            last = (b"", f"rc{r.returncode}", head)
            attempt += 1
            continue
        code = _final_status(head)
        last = (r.stdout, code, head)
        if code == "429":
            # The one branch that stops us earning blocks. Honour what IA asks
            # for and do NOT count it as an attempt: being told to slow down
            # is not a failure, it is an instruction.
            wait_s = _retry_after(head)
            print(f"  IA 429 on {where}; honouring Retry-After {wait_s:.0f}s "
                  f"({telemetry(head)})", file=sys.stderr, flush=True)
            time.sleep(wait_s)
            continue
        if code == "503":
            # IA-side degradation, not our rate. Back off, keep going, and
            # label it so a run is not misread as our fault.
            back = min(MAX_503_BACKOFF, 5.0 * (2 ** attempt))
            print(f"  IA 503 on {where} (service degraded, not our rate); "
                  f"backing off {back:.0f}s", file=sys.stderr, flush=True)
            time.sleep(back)
            attempt += 1
            continue
        return r.stdout, code, head
    return last


def get(url: str, tries: int = 3, compressed: bool = True) -> tuple[bytes, str]:
    """Fetch `url`. Returns (body, code) — code "200", "404", "rc7", ..."""
    args = ["curl", "-sL", "--max-time", "90", "-H", f"User-Agent: {UA}"]
    if compressed:
        args.append("--compressed")
    args.append(url)
    body, code, _ = _run(args, tries, url.split("?")[0][-60:])
    return body, code


def probe(url: str, date: str, tries: int = 3) -> tuple[str, str]:
    """Replay probe -> (effective_url, code), for reading a capture timestamp.

    A transport failure comes back as "rc<N>", never as an empty answer a
    caller could read as absence (12402a7: the Redpoint run recorded 10 of 14
    era-years as empty because the return code was never read).
    """
    target = f"https://web.archive.org/web/{date}id_/{url}"
    args = ["curl", "-sL", "--max-time", "90", "-o", "/dev/null",
            "-w", "%{url_effective}", "-H", f"User-Agent: {UA}", target]
    body, code, _ = _run(args, tries, f"{date}/{url.split('//')[-1][:40]}")
    if code.startswith("rc"):
        return "", code
    return body.decode(errors="replace").strip(), code


def blocked() -> float:
    """Seconds left on the machine-wide IA cooldown, 0 if clear."""
    return shared_throttle.cooldown_remaining("ia")
