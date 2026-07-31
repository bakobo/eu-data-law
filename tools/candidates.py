"""The instrument list for this repo, and the scope decision made visible.

Scope is fixed here rather than discovered as we go — see `this.i` @ytpyhw. "European data
locality regulations" has no natural edge, so this file *is* the edge. Anything not listed is out
of scope until it is added here deliberately, and the README's Known Gaps says what was left out.

Every entry carries `expect_in_title`: a phrase that must appear in the title EUR-Lex actually
returns. That is the check against a remembered-but-wrong CELEX number, which is the single most
likely way for this corpus to be quietly built on sand.

`validity` is the *initial* claim and must be confirmed against the instrument itself before a
finding rests on it. `in-force` here means "believed in force at harvest"; the harvester records
it, and the burden of keeping it honest sits with whoever refetches.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate:
    celex: str
    citation: str
    title: str
    authority_tier: str
    validity: str
    expect_in_title: str
    validity_note: str = ""
    version_id: str = ""


CANDIDATES = [
    # ---- The data-protection core -------------------------------------------------------
    Candidate(
        celex="32016R0679",
        citation="Regulation (EU) 2016/679 (GDPR)",
        title="General Data Protection Regulation",
        authority_tier="legislative",
        validity="in-force",
        expect_in_title="protection of natural persons with regard to the processing of personal data",
    ),
    Candidate(
        celex="32016L0680",
        citation="Directive (EU) 2016/680 (LED)",
        title="Law Enforcement Directive",
        authority_tier="legislative",
        validity="in-force",
        expect_in_title="competent authorities for the purposes of the prevention",
    ),
    Candidate(
        celex="32018R1725",
        citation="Regulation (EU) 2018/1725 (EUDPR)",
        title="Data protection for Union institutions and bodies",
        authority_tier="legislative",
        validity="in-force",
        expect_in_title="Union institutions",
    ),
    # ---- Data locality / free movement --------------------------------------------------
    Candidate(
        celex="32018R1807",
        citation="Regulation (EU) 2018/1807",
        title="Framework for the free flow of non-personal data",
        authority_tier="legislative",
        validity="in-force",
        expect_in_title="free flow of non-personal data",
    ),
    Candidate(
        celex="32022R0868",
        citation="Regulation (EU) 2022/868 (DGA)",
        title="Data Governance Act",
        authority_tier="legislative",
        validity="in-force",
        expect_in_title="European data governance",
    ),
    Candidate(
        celex="32023R2854",
        citation="Regulation (EU) 2023/2854 (Data Act)",
        title="Data Act",
        authority_tier="legislative",
        validity="in-force",
        expect_in_title="harmonised rules on fair access to and use of data",
    ),
    # ---- Chapter V transfer machinery ---------------------------------------------------
    Candidate(
        celex="32021D0914",
        citation="Commission Implementing Decision (EU) 2021/914",
        title="Standard contractual clauses for transfers to third countries",
        authority_tier="delegated",
        validity="in-force",
        expect_in_title="standard contractual clauses",
    ),
    Candidate(
        celex="32023D1795",
        citation="Commission Implementing Decision (EU) 2023/1795",
        title="Adequacy of the EU-US Data Privacy Framework",
        authority_tier="delegated",
        validity="in-force",
        expect_in_title="Data Privacy Framework",
    ),
    Candidate(
        celex="32021D1772",
        citation="Commission Implementing Decision (EU) 2021/1772",
        title="Adequacy of the United Kingdom (GDPR)",
        authority_tier="delegated",
        validity="in-force",
        expect_in_title="United Kingdom",
    ),
    Candidate(
        celex="32019D0419",
        citation="Commission Implementing Decision (EU) 2019/419",
        title="Adequacy of Japan",
        authority_tier="delegated",
        validity="in-force",
        expect_in_title="Japan",
    ),
    Candidate(
        celex="32022D0254",
        citation="Commission Implementing Decision (EU) 2022/254",
        title="Adequacy of the Republic of Korea",
        authority_tier="delegated",
        validity="in-force",
        expect_in_title="Korea",
    ),
    # ---- The CJEU line ------------------------------------------------------------------
    # Case law is load-bearing for this regime in a way it is not for Utah: Schrems II did not
    # interpret Chapter V so much as invalidate the arrangement built under it.
    Candidate(
        celex="62014CJ0362",
        citation="Case C-362/14, Schrems (Schrems I)",
        title="Schrems I — invalidating the Safe Harbour decision",
        authority_tier="judicial",
        validity="in-force",
        expect_in_title="Schrems",
    ),
    Candidate(
        celex="62018CJ0311",
        citation="Case C-311/18, Facebook Ireland and Schrems (Schrems II)",
        title="Schrems II — invalidating Privacy Shield, upholding SCCs conditionally",
        authority_tier="judicial",
        validity="in-force",
        expect_in_title="Schrems",
    ),
    Candidate(
        celex="62012CJ0293",
        citation="Joined Cases C-293/12 and C-594/12, Digital Rights Ireland",
        title="Digital Rights Ireland — invalidating the Data Retention Directive",
        authority_tier="judicial",
        validity="in-force",
        expect_in_title="Digital Rights",
    ),
    Candidate(
        celex="62012CJ0131",
        citation="Case C-131/12, Google Spain",
        title="Google Spain — the right to erasure against a search engine",
        authority_tier="judicial",
        validity="in-force",
        expect_in_title="Google Spain",
    ),
    Candidate(
        celex="62018CJ0511",
        citation="Joined Cases C-511/18 etc., La Quadrature du Net",
        title="La Quadrature du Net — general data retention and national security",
        authority_tier="judicial",
        validity="in-force",
        expect_in_title="Quadrature",
    ),
    Candidate(
        celex="62021CJ0252",
        citation="Case C-252/21, Meta Platforms v Bundeskartellamt",
        title="Meta v Bundeskartellamt — consent, legitimate interests, special categories",
        authority_tier="judicial",
        validity="in-force",
        expect_in_title="Meta Platforms",
    ),
    Candidate(
        celex="62021CJ0634",
        citation="Case C-634/21, OQ v Land Hessen (SCHUFA Holding)",
        # Universally cited as "SCHUFA", but SCHUFA Holding AG was the intervener: the official
        # party name is OQ v Land Hessen, and no EUR-Lex title contains the word SCHUFA. Verified
        # from the judgment text, which mentions SCHUFA 23 times and rules on Article 22(1).
        title="OQ v Land Hessen — automated decision-making under GDPR Article 22(1)",
        authority_tier="judicial",
        validity="in-force",
        expect_in_title="Land Hessen",
    ),
]
