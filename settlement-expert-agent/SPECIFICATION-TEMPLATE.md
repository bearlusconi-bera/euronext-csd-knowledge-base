# Specification template — settlement functional / technical specification

Every row or bullet carries one label: **Documented requirement** (cite `[[section-id]]` + locator + review date + qualifications), **Reasoned inference** (say from what), **Proposed design choice** (an implementation decision, not an infrastructure rule) or **Unresolved requirement** (name the missing source, the gap id and the access route). Field-level content appears only where the retrieved usage specification, schema and local mapping support it.

## 0. Scope block

| Item | Value |
|---|---|
| CSD / legal entity and jurisdiction | |
| Service and settlement route (intra-CSD, cross-CSD in T2S, external CSD) | |
| Participants and roles (instructing party, counterparty, cash agent, CSDs, T2S) | |
| Instrument, link and account assumptions (ISIN eligibility, issuer/investor CSD per issue, omnibus/mirror accounts) | |
| Platform release (deployed) and any published future release | |
| Currency and payment type (DVP, FOP, DWP, PFOD) | |
| Access model (ICP via local interface / DCP) and link model | |
| Evidence review date(s) used | |
| Intended business date (actual) or nominal baseline | |
| Known quarantines and inapplicable sources | |

## 1. Preconditions, permissions, eligibility and static data

Participation category and admission, securities account and cash account (DCA / agent bank) responsibilities, static data (LEI, BICs, account links, Party 1/Party 2), entitlements and tests, connectivity.

## 2. Business sequence and observable states

Numbered steps from instruction creation to finality: local validation/enrichment, submission, T2S validation (SF1 where defined), matching (SF2 where defined), allegement, hold/release, realignment generation, eligibility and provision checks, partial settlement, booking (SF3 where defined), status reporting, recycling and automatic cancellation. State the observable status after each step and who sees it.

## 3. Message table

Separate three layers: (A) client to CSD (local interface), (B) CSD to T2S (native), (C) T2S internal processing and T2S outbound.

| # | Layer | Sender | Receiver | Interface / network | Message and version | Trigger | Relevant fields / identifiers | Conditions | Response / status | Source locator | Label |
|---|---|---|---|---|---|---|---|---|---|---|---|

## 4. Timing

Trade date, intended settlement date, business-day counting and calendar, civil-day versus T2S business-day boundary (SOD the previous evening), time zone convention (CET; local WET/CET notes), nominal cut-offs and windows, dated changes (event overlays) for the intended business date, and the statement that submission, matching and settlement times are not guaranteed appointments.

## 5. Exceptions and controls

Rejections and retries; idempotency and references (T2S Actor reference, T2S reference, matching reference); hold/release and partial release; cancellation (unilateral, bilateral, system, CoSD); insufficient securities or cash (recycling, partial settlement, auto-collateralisation where applicable); realignment failures; reconciliation and reporting; corporate actions on flow (market claims, transformations) where relevant. Mark implementation decisions separately from infrastructure rules.

## 6. Finality and cancellation boundaries

Moments of entry, irrevocability and finality with their legal qualifications (system rules, national law, governing language, approval reservations), and how cancellation interacts with them.

## 7. Acceptance criteria

Each criterion tied to a cited requirement (`[[section-id]]`, locator) and testable against observable statuses or messages.

## 8. Open dependencies blocking a production specification

Table of missing documents or data (exact title/version if known), gap id, affected rows, access route (public hub, client platform, CSD documentation service, standards body), acquisition status.
