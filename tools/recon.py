#!/usr/bin/env python3
"""Verify a candidate CELEX list before harvesting it.

The whole point of this repo is that citations are checkable rather than recalled. That discipline
has to start with the work-list itself: a CELEX number remembered from training data is exactly the
kind of plausible-looking fabrication the corpus exists to catch.

So before anything is stored, this fetches each candidate's metadata notice, prints the title the
EU actually returns, and reports whether the text is available as Formex. Read the output and
confirm each row is the instrument you meant. Nothing is written to the corpus here.

    python3 tools/recon.py            # check the whole candidate list
    python3 tools/recon.py 32016R0679 # check one
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from candidates import CANDIDATES  # noqa: E402

from lawcorpus.fetch.eurlex import ACCEPT_NOTICE_BRANCH, EurLexError, EurLexFetcher  # noqa: E402
from lawcorpus.formex import FormexError, articles, recitals, to_text  # noqa: E402

# The *branch* notice carries titles; the object notice does not carry one at all. Within the
# branch notice, EXPRESSION_TITLE appears once per language expression and the first match is
# whichever language Cellar felt like ordering first (observed: Hungarian for the GDPR, German
# for Schrems II). The plain <TITLE> is the work-level title in the requested language.
_TITLE = re.compile(r"<TITLE[^>]*>(.*?)</TITLE>", re.S)
_TAGS = re.compile(r"<[^>]+>")


def titles_of(notice_xml: bytes) -> list:
    """Every <TITLE> in the notice.

    One instrument carries several: the adopted title, the proposal's title, an inter-institutional
    procedure reference like 'PE/53/2018/REV/1', and for judgments a short form with only the date.
    Checking only the first produces false mismatches, so the identity check looks at all of them.
    """
    out = []
    for m in _TITLE.finditer(notice_xml.decode("utf-8", "replace")):
        text = " ".join(_TAGS.sub(" ", m.group(1)).split())
        if text and text not in out:
            out.append(text)
    return out or ["(no title in notice)"]


def main(argv):
    wanted = [c for c in CANDIDATES if not argv or c.celex in argv]
    if argv and not wanted:
        print(f"No candidate matches {argv}.", file=sys.stderr)
        return 2

    fetcher = EurLexFetcher()
    problems = 0
    for cand in wanted:
        print(f"\n{cand.celex}  [{cand.authority_tier}]")
        print(f"  expected: {cand.title}")
        try:
            notice = fetcher.fetch(cand.celex, accept=ACCEPT_NOTICE_BRANCH)
        except EurLexError as e:
            print(f"  METADATA FAILED: {e}")
            problems += 1
            continue
        found = titles_of(notice.body)
        print(f"  actual:   {found[0][:150]}")
        for extra in found[1:]:
            print(f"            | {extra[:150]}")
        if not any(cand.expect_in_title.lower() in t.lower() for t in found):
            print(f"  *** MISMATCH: '{cand.expect_in_title}' appears in none of the titles ***")
            problems += 1

        try:
            body = fetcher.fetch_formex(cand.celex).body
            text = to_text(body)
            # Word count is the portable size check. Article/recital counts are meaningful for
            # acts and meaningless for judgments, which use a different Formex structure — a
            # judgment reporting "0 articles" is normal, not a failed extraction.
            shape = f"{len(text.split()):,} words"
            n_art, n_rec = len(articles(body)), len(recitals(body))
            if n_art or n_rec:
                shape += f" ({n_art} ARTICLE, {n_rec} CONSID elements)"
            print(f"  formex:   {shape}")
            if len(text.split()) < 300:
                print("  *** SUSPICIOUSLY SHORT — check this is the document and not a stub ***")
                problems += 1
        except (EurLexError, FormexError) as e:
            print(f"  formex:   UNAVAILABLE — {str(e)[:160]}")
            problems += 1

    print(f"\n{len(wanted)} candidate(s) checked, {problems} needing attention.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
