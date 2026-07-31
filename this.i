# eu-data-law — Intent Tree (this.i)

A checkable corpus of EU data-protection and data-locality law = goal:
  id: onlznv
  why: >
    Harvest the primary text of the EU regime governing what may be done with personal data and
    where data may sit, with provenance strong enough that a later AI analysis can quote it without
    repeating the online research. Rejected the obvious alternative of writing findings first and
    citing live URLs, which is how most such research is done and which decays the moment EUR-Lex
    reconsolidates an instrument. Driving constraint inherited from utah-id-law: language models
    fabricate legal citations fluently, so a claim is admissible only if a verbatim quote can be
    retrieved from a local file. Tradeoff accepted: substantial up-front harvesting cost and a
    corpus that must be refetched to stay current, in exchange for findings that can be audited
    mechanically rather than trusted.
  children:
    Scope is fixed to a named instrument list before the first fetch = decision:
      id: ytpyhw
      why: >
        "European data locality regulations" has no natural edge — it could stop at GDPR Chapter V
        or extend through NIS2, DORA, EHDS, the EUCS cloud scheme, and national schemes such as
        SecNumCloud and BSI C5, which is a multi-month corpus. Chose a narrow, coherent set:
        GDPR in full, the Chapter V transfer machinery (adequacy decisions, SCCs, the Schrems
        line), Regulation 2018/1807 on the free flow of non-personal data, the Data Act
        (2023/2854), and the Data Governance Act (2022/868). 2018/1807 is included even though it
        was not in the original sketch, because it is the actual anti-localization instrument —
        omitting it would leave the repo unable to answer its own headline question. Everything
        else is a dated "not yet" in the README's Known Gaps rather than an unstated omission.
        Tradeoff: sector-specific localization rules are out of scope, so no claim here may be
        stated as "EU law nowhere requires localization" without that caveat attached.

    The corpus pins a consolidation date, not just a CELEX number = decision:
      id: bqbgl6
      why: >
        EUR-Lex serves both the text as originally published (CELEX 32016R0679) and consolidated
        versions incorporating later amendments (02016R0679-20160504). For a heavily amended
        instrument, quoting the original is simply wrong. Chose to treat the consolidation date as
        part of the citation — the direct analogue of utah-id-law's version stamps, which encode an
        effective-date range so a citation pins a *version* rather than a section. Rejected storing
        only the latest consolidated text, because a finding written in 2026 must remain checkable
        after the next amendment lands. Tradeoff: the corpus stores more than one version of some
        instruments, and cite.py must be told which one a finding meant.

    National transposition is a corpus layer, not a footnote = decision:
      id: g2sb6p
      why: >
        utah-id-law learned twice that checking one layer is not enough — the fishing-licence
        requirement existed only in the administrative rules, and the court-filing question was
        unanswerable until the court rules were added. The EU analogue is national implementing
        measures: for anything directive-based or resting on a GDPR opening clause, "EU law
        requires X" without the member-state layer repeats that exact error. EUR-Lex links the
        transposition notices, so the cost is bounded. Tradeoff accepted: 27 member states is far
        beyond what we can archive in full, so the layer is sampled rather than complete, and every
        finding that depends on it must say which states were checked.
