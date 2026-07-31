# eu-data-law — GDPR and the EU data-locality stack

**This is a share of primary sources and the tooling to quote them. Nothing more.**

Offered **without warranty** and **without any claim of legal gravitas**. It was assembled by
non-lawyers doing textual research with substantial AI assistance. It is not legal advice, not an
authoritative statement of EU law, and not a substitute for a lawyer. Every claim is tied to a
citation you can check yourself — check it.

## What is here

A local, hash-manifested copy of 18 instruments: the EU data-protection core, the data-locality
regulations, the Chapter V transfer machinery, and the CJEU line that governs how they are read.
About **511,000 words**, retrieved 2026-07-31.

| Layer | Items | Words |
|---|---|---|
| **Legislative** — GDPR, LED, EUDPR, 2018/1807, DGA, Data Act | 6 | 200,340 |
| **Delegated** — SCCs and four adequacy decisions | 5 | 174,795 |
| **Judicial** — the CJEU line from Digital Rights Ireland to SCHUFA | 7 | 135,603 |

```
corpus/*.txt.gz        one file per instrument, gzipped, searchable with rg -z
corpus/MANIFEST.tsv    citation, authority tier, validity, version, URL, date, bytes, SHA-256
tools/candidates.py    the instrument list — this file IS the scope boundary
tools/recon.py         verify a CELEX list against EUR-Lex before harvesting it
tools/harvest.py       fetch, extract, store, manifest
sources/registry.md    live URL ⇄ local copy ⇄ retrieval date
```

## Using it

Tooling lives in the sibling [`id-law-kit`](https://github.com/bakobo/id-law-kit) repo:

```sh
python3 -m venv .venv && .venv/bin/pip install -e ../id-law-kit

.venv/bin/lawcite --corpus corpus 32016R0679             # quote the GDPR
.venv/bin/lawcite --corpus corpus 'Case C-311/18, Facebook Ireland and Schrems (Schrems II)'
.venv/bin/lawcite --corpus corpus --grep 'reasonable doubts concerning the identity'
.venv/bin/lawcite --corpus corpus --grep 'Article 22\(1\)' --in-force-only

rg -z 'adequate level of protection' corpus/             # raw search
```

Every quote prints a **validity banner** first. That is not decoration: published text is not
necessarily current law, and this corpus holds decisions the Court has invalidated.

## Scope, and where its edges are

"European data locality regulations" has no natural boundary — it could run through NIS2, DORA,
EHDS, the EUCS cloud scheme, and national regimes like SecNumCloud and BSI C5. So the boundary is
written down rather than discovered: **[`tools/candidates.py`](tools/candidates.py) is the scope.**
Nothing enters the corpus without an entry there.

**Included:** GDPR · Law Enforcement Directive · EUDPR · Regulation 2018/1807 (free flow of
non-personal data — the actual anti-localization instrument) · Data Governance Act · Data Act ·
the SCCs · adequacy decisions for the US, UK, Japan and Korea · Schrems I and II, Digital Rights
Ireland, Google Spain, La Quadrature du Net, Meta v Bundeskartellamt, OQ v Land Hessen.

## Known gaps

No claim of the form "EU law nowhere requires X" is complete without these.

1. **National transposition and derogations.** The GDPR's opening clauses let member states diverge,
   and the LED is a *directive* — its operative form is 27 national laws. None are held here. This
   is the same error `utah-id-law` made twice by reading statute without the rules layer.
2. **EDPB guidelines and opinions.** ~80 documents that carry much of the operative interpretation.
   Not yet retrieved; they are HTML scraping rather than a clean API.
3. **Sectoral and infrastructure regimes.** NIS2, DORA, EHDS, ePrivacy, the AI Act, the EUCS cloud
   scheme, Gaia-X, SecNumCloud, BSI C5. Deliberately out of scope as of 2026-07-31.
4. **National supervisory authority decisions and fines.** Where "reasonable" acquires meaning in
   practice. Absent.
5. **English only.** All 24 language versions are equally authentic and the CJEU resolves ambiguity
   by comparing them. Any finding that turns on a term of art is weaker than it looks. See
   `this.i` @om6zsj.
6. **Adequacy decisions are a moving target.** They are reviewed periodically and can be annulled —
   which is precisely what happened to the two that preceded the current US decision.

## Provenance and currency

The manifest records URL, retrieval date, byte count, and SHA-256 per item, so a refetch diffs
cleanly. **Everything here was retrieved 2026-07-31** — refetch before relying on it.

Two things a careful reader should know about how the text was produced:

- **Consolidated vs. original.** `32016R0679` is the GDPR *as published in 2016*. Instruments
  amended since publication have consolidated versions under a different CELEX
  (`02016R0679-<date>`). The `version_id` column records exactly which text is stored. See
  `this.i` @bqbgl6.
- **The stored text is our extraction, not the EU's bytes.** Formex XML is rendered to text, and
  layout-only characters are normalised — EU documents put U+00A0 inside "Article 22" and U+2011
  inside case numbers, so a search for `Article 22` or `C-311/18` would otherwise return nothing
  while looking correct. The SHA-256 attests to our extraction. Rationale and the cost accepted:
  `id-law-kit` `this.i` @f5mvj6.

## Licence

The **original work** — the candidate list, tooling, registry, and any findings — is
**[CC BY 4.0](LICENSE)**. Attribution: Bakobo, *eu-data-law*.

The **corpus under `corpus/` is not ours to license.** It is the text of EU legal instruments,
© European Union, 1998–2026, reproduced under the terms of
[Commission Decision 2011/833/EU](http://eur-lex.europa.eu/eli/dec/2011/833/oj) on the reuse of
Commission documents, which permits reuse with acknowledgement of source. **Only the text published
in the printed Official Journal of the European Union is authentic.** The authoritative source
remains [eur-lex.europa.eu](https://eur-lex.europa.eu).

Note that this basis differs from the one `utah-id-law` relies on. "Edicts of government carry no
copyright" is US doctrine and does not transfer to the EU.
