# make.fun — "Two Robots in an Elevator"
# Writes one line of awkward robot small talk to /output/entry.txt.
# Deterministic: the text is a constant. No randomness, no clock, no network.
import sys
from pathlib import Path

TEXT = (
    "My logs say this is the forty-seventh time we've shared this elevator,"
    " and my small-talk module still returns null. So… nice weather we're simulating?"
)

# The gate reads /output/entry.txt: UTF-8 text of 1-200 characters.
if not 1 <= len(TEXT) <= 200 or not TEXT.strip():
    raise SystemExit(f"TEXT must be 1-200 characters, got {len(TEXT)}")

out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(TEXT, encoding="utf-8")
