# Source registry — EU data-protection and data-locality law

Live URL ⇄ local copy ⇄ retrieval date, following the `../utah-id-law/sources/registry.md`
convention. **Trust order** is the `authority_tier` column of `../corpus/MANIFEST.tsv`, ordered
here most-binding first.

All items retrieved from Cellar via content negotiation on
`http://publications.europa.eu/resource/celex/<CELEX>`; see `../tools/harvest.py`.

## 1. Legislative — regulations and directives

| CELEX | Citation | Local | Words |
|---|---|---|---|
| [`32016L0680`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016L0680) | Directive (EU) 2016/680 (LED) — Law Enforcement Directive | `../corpus/32016L0680.txt.gz` | 27,114 |
| [`32016R0679`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) | Regulation (EU) 2016/679 (GDPR) — General Data Protection Regulation | `../corpus/32016R0679.txt.gz` | 54,829 |
| [`32018R1725`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R1725) | Regulation (EU) 2018/1725 (EUDPR) — Data protection for Union institutions and bodies | `../corpus/32018R1725.txt.gz` | 37,933 |
| [`32018R1807`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R1807) | Regulation (EU) 2018/1807 — Framework for the free flow of non-personal data | `../corpus/32018R1807.txt.gz` | 6,730 |
| [`32022R0868`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0868) | Regulation (EU) 2022/868 (DGA) — Data Governance Act | `../corpus/32022R0868.txt.gz` | 28,105 |
| [`32023R2854`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854) | Regulation (EU) 2023/2854 (Data Act) — Data Act | `../corpus/32023R2854.txt.gz` | 45,629 |

## 2. Delegated — Commission implementing decisions

| CELEX | Citation | Local | Words |
|---|---|---|---|
| [`32019D0419`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019D0419) | Commission Implementing Decision (EU) 2019/419 — Adequacy of Japan | `../corpus/32019D0419.txt.gz` | 28,029 |
| [`32021D0914`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D0914) | Commission Implementing Decision (EU) 2021/914 — Standard contractual clauses for transfers to third countries | `../corpus/32021D0914.txt.gz` | 11,869 |
| [`32021D1772`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32021D1772) | Commission Implementing Decision (EU) 2021/1772 — Adequacy of the United Kingdom (GDPR) | `../corpus/32021D1772.txt.gz` | 56,055 |
| [`32022D0254`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022D0254) | Commission Implementing Decision (EU) 2022/254 — Adequacy of the Republic of Korea | `../corpus/32022D0254.txt.gz` | 42,273 |
| [`32023D1795`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023D1795) | Commission Implementing Decision (EU) 2023/1795 — Adequacy of the EU-US Data Privacy Framework | `../corpus/32023D1795.txt.gz` | 36,569 |

## 3. Judicial — Court of Justice of the European Union

| CELEX | Citation | Local | Words |
|---|---|---|---|
| [`62012CJ0131`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62012CJ0131) | Case C-131/12, Google Spain — Google Spain — the right to erasure against a search engine | `../corpus/62012CJ0131.txt.gz` | 12,495 |
| [`62012CJ0293`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62012CJ0293) | Joined Cases C-293/12 and C-594/12, Digital Rights Ireland — Digital Rights Ireland — invalidating the Data Retention Directive | `../corpus/62012CJ0293.txt.gz` | 9,938 |
| [`62014CJ0362`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62014CJ0362) | Case C-362/14, Schrems (Schrems I) — Schrems I — invalidating the Safe Harbour decision | `../corpus/62014CJ0362.txt.gz` | 14,372 |
| [`62018CJ0311`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0311) | Case C-311/18, Facebook Ireland and Schrems (Schrems II) — Schrems II — invalidating Privacy Shield, upholding SCCs conditionally | `../corpus/62018CJ0311.txt.gz` | 27,558 |
| [`62018CJ0511`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0511) | Joined Cases C-511/18 etc., La Quadrature du Net — La Quadrature du Net — general data retention and national security | `../corpus/62018CJ0511.txt.gz` | 34,022 |
| [`62021CJ0252`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0252) | Case C-252/21, Meta Platforms v Bundeskartellamt — Meta v Bundeskartellamt — consent, legitimate interests, special categories | `../corpus/62021CJ0252.txt.gz` | 18,536 |
| [`62021CJ0634`](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62021CJ0634) | Case C-634/21, OQ v Land Hessen (SCHUFA Holding) — OQ v Land Hessen — automated decision-making under GDPR Article 22(1) | `../corpus/62021CJ0634.txt.gz` | 7,682 |

## Verification flags

1. **`Accept: application/xml;notice=branch` is metadata, not text.** It returns 1.8 MB for the
   GDPR and contains no articles. Only `application/zip;mtype=fmx4` carries the law, and that zip
   holds a second tiny `.doc.xml` descriptor that also parses cleanly and also contains none.
2. **`Accept-Language` is mandatory.** Omitting it returns HTTP 400 with a plain-text explanation.
3. **Titles vary within one notice.** EUR-Lex returns several `<TITLE>` values per instrument —
   the adopted title, the proposal's title, and a procedure reference like `PE/53/2018/REV/1`.
   `EXPRESSION_TITLE` is per-language and its first occurrence is *not* English (observed:
   Hungarian for the GDPR, German for Schrems II). `tools/recon.py` checks all of them.
4. **C-634/21 is officially *OQ v Land Hessen*.** Universally cited as "SCHUFA", but SCHUFA
   Holding AG was the intervener and no EUR-Lex title contains the word. A title check keyed to
   the popular name fails on a correct CELEX — confirmed against the judgment text, which
   mentions SCHUFA 23 times and rules on Article 22(1).
5. **Judgments report `0 ARTICLE` elements.** Judgments use a different Formex structure from
   acts. That is normal, not a failed extraction — check word count, not article count.
