#!/usr/bin/env python3
"""Fetch the candidate instruments and write the corpus plus its manifest.

Run `tools/recon.py` first and read its output. This script re-runs the same identity check and
refuses to store anything whose title does not match, but recon is where a human confirms the
work-list is the one they meant — that judgement is not automatable and should not be skipped.

    python3 tools/harvest.py             # everything not already stored
    python3 tools/harvest.py --force     # refetch everything
    python3 tools/harvest.py 32016R0679  # one instrument
"""

import argparse
import datetime
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from candidates import CANDIDATES  # noqa: E402
from recon import titles_of  # noqa: E402

from lawcorpus.fetch.eurlex import ACCEPT_NOTICE_BRANCH, EurLexError, EurLexFetcher  # noqa: E402
from lawcorpus.formex import FormexError, to_text  # noqa: E402
from lawcorpus.manifest import Manifest, ManifestItem  # noqa: E402
from lawcorpus.store import CorpusStore  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"

# Cellar answers 429 if pushed. One second between instruments is ample for a list this size and
# costs under a minute overall.
PAUSE_SECONDS = 1.0

# Every item on the candidate list is EUR-Lex text in English, and the EU's 24 language versions
# are each authentic — so this is the only value any row here could carry, and it is a constant
# rather than a field on Candidate. See `this.i` @ubk6kugi for what has to change the day this
# corpus stores something that is not authentic EU text.
TRANSLATION_STATUS = "authoritative"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("celex", nargs="*", help="limit to these CELEX numbers")
    p.add_argument("--force", action="store_true", help="refetch even if already stored")
    args = p.parse_args(argv)

    wanted = [c for c in CANDIDATES if not args.celex or c.celex in args.celex]
    if args.celex and not wanted:
        print(f"No candidate matches {args.celex}.", file=sys.stderr)
        return 2

    store = CorpusStore(CORPUS)
    fetcher = EurLexFetcher()
    retrieved = datetime.date.today().isoformat()

    manifest_path = CORPUS / "MANIFEST.tsv"
    existing = {i.item_id: i for i in Manifest.read(manifest_path)} if manifest_path.exists() else {}

    failures = []
    for n, cand in enumerate(wanted):
        if not args.force and cand.celex in existing and store.exists(cand.celex):
            print(f"{cand.celex}  already stored, skipping")
            continue
        if n:
            time.sleep(PAUSE_SECONDS)
        print(f"{cand.celex}  {cand.citation}")
        try:
            # Identity check first, so a wrong CELEX never reaches the corpus.
            notice = fetcher.fetch(cand.celex, accept=ACCEPT_NOTICE_BRANCH)
            found = titles_of(notice.body)
            if not any(cand.expect_in_title.lower() in t.lower() for t in found):
                raise EurLexError(
                    f"The title check failed for {cand.celex}: expected to see "
                    f"'{cand.expect_in_title}' in one of {len(found)} titles, and it is in none. "
                    f"First title: '{found[0][:110]}'. Fix the candidate entry or the CELEX before "
                    f"storing anything."
                )

            doc = fetcher.fetch_formex(cand.celex)
            # ~65ak doc.annex_bodies is discarded here, so the four multi-member instruments
            # (the SCCs and the Japan, Korea and US adequacy decisions) are stored without their
            # annexes. Measured, with the cost of fixing it, in the tick.
            text = to_text(doc.body)
            written = store.write(cand.celex, text)
        except (EurLexError, FormexError) as e:
            print(f"  FAILED: {e}")
            failures.append((cand.celex, str(e)))
            continue

        existing[cand.celex] = ManifestItem(
            item_id=cand.celex,
            citation=cand.citation,
            title=cand.title,
            authority_tier=cand.authority_tier,
            validity=cand.validity,
            validity_note=cand.validity_note,
            translation_status=TRANSLATION_STATUS,
            version_id=cand.version_id or cand.celex,
            lang="eng",
            source_url=doc.url,
            retrieved=retrieved,
            media_type=doc.media_type,
            bytes=written.bytes,
            sha256=written.sha256,
        )
        print(f"  stored {written.bytes:,} bytes ({len(text.split()):,} words)")

    Manifest(list(existing.values())).write(manifest_path)
    print(f"\nManifest: {len(existing)} item(s) at {manifest_path}")
    if failures:
        print(f"{len(failures)} failure(s):")
        for celex, msg in failures:
            print(f"  {celex}: {msg[:160]}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
