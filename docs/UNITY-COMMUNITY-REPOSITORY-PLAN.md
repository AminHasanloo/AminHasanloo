# Unity Community Repository Plan

**Owner:** Amin Hasanloo

**Audience:** Game studios, Unity engineering teams, open-source contributors, and technical recruiters

**Snapshot date:** 2026-09-09

**Primary direction:** Unity 2D/3D, mobile publishing and monetization, game AI, VR/AR, and production tooling

## 1. Objective

Build a small, credible open-source portfolio that proves engineering depth instead of creating many shallow repositories.

The portfolio should demonstrate four things within two minutes:

1. Amin can design maintainable Unity systems.
2. Amin can ship across 2D, 3D, Android, VR, and AR contexts.
3. Amin understands real production concerns such as SDK isolation, consent, billing verification, testing, profiling, and release safety.
4. External developers can install, run, understand, and contribute to the work.

GitHub recommends highlighting roughly three to five job-relevant projects and making each one fast to understand. The team should treat the first screen, demo, Quick Start, and tested compatibility table as product features, not optional documentation.

Reference: [Using your GitHub profile to enhance your resume](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume)

## 2. Current Profile Audit

### Strong signals

- The profile README now has a distinct Unity/game identity and a consistent pixel-arcade visual system.
- `Unity-AI-Vehicle-System` already has the strongest public traction, an English README, screenshots, a video, an MIT license, 8 stars, and 2 forks.
- `UnityMonetizationFramework` addresses a valuable niche: one Unity-facing architecture for global and Iranian stores/ad networks.
- `Unity-Analytics-Lite` demonstrates offline-first event delivery and consent-aware design.
- The profile has automated visual refresh, link health checks, a rolling work queue, and Dependabot maintenance.

### High-priority gaps

| Priority | Finding | Required action |
|---|---|---|
| P0 | The public bio still says `Full Stack Web Developer & Web3 Game Creator` | Change it to `Senior Unity Game Developer | Gameplay, Game AI, Mobile & XR | C#` |
| P0 | Public profile identity is split between `Amin Hasanloo` and `Mohammad Amin Hasanloo` | Select one professional display name and use it consistently across GitHub, LinkedIn, CV, releases, and package metadata |
| P0 | The best Unity repositories have no recent public release cadence | Publish tested semantic releases only after compatibility and demo validation |
| P0 | Two important Unity READMEs are Persian-first | Make English the primary README language; keep Persian as `README.fa.md` |
| P0 | Several repositories have no license or contributor/security guidance | Add an appropriate license and community health files; do not assume code is reusable without a license |
| P1 | Some featured/familiar repositories are forks | Do not present a fork as an owned product; feature it only when Amin's upstream contributions are clear and linked |
| P1 | Current projects do not consistently state tested Unity/package versions | Add a compatibility matrix backed by actual compile and Play Mode evidence |
| P1 | Architecture and test evidence are inconsistent | Add a small architecture diagram, deterministic tests, demo proof, limitations, and a troubleshooting section |
| P2 | Older Telegram/Web3 repositories dilute the Unity positioning | Keep them public if useful, but do not pin them for game-studio applications |

### Recommended public profile metadata

Use the following copy when the account settings are updated manually:

```text
Name: Mohammad Amin Hasanloo
Bio: Senior Unity Game Developer | Gameplay, Game AI, Mobile & XR | C#
```

Only add a company, website, or location when it is accurate and intended to be public. Add one working portfolio/demo URL rather than several unfinished links.

### Recommended pins

The public profile snapshot currently shows only two pinned repositories: `UnityMonetizationFramework` and `Unity-AI-Vehicle-System`.

Pin four owned repositories first:

1. `Unity-AI-Vehicle-System`
2. `UnityMonetizationFramework`
3. `Unity-Analytics-Lite`
4. `UnityExportPackageComplete`

Use the fifth and sixth slots only after a new repository reaches the release-ready definition in this document. Do not pin `quickstart-unity` as portfolio proof because it is a fork. Do not pin `spine-animation-ai` as an owned project unless Amin's contribution and upstream relationship are explained clearly.

GitHub allows up to six pinned items, but relevance is more important than filling every slot: [Pinning items to your profile](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile).

## 3. Update Existing Repositories Before Creating New Ones

### P0 — UnityMonetizationFramework v2

**Why first:** It is the most differentiated portfolio asset and directly represents Google Play, Café Bazaar, Myket, AdMob, and Tapsell experience.

**Required scope:**

- Publish an English `README.md` and move the current Persian documentation to `README.fa.md`.
- Separate contracts from vendor implementations:
  - `IIapProvider`
  - `IAdsProvider`
  - `IConsentProvider`
  - `IReceiptVerifier`
  - provider-neutral result and error models
- Create independent provider packages or assemblies for Google Play, Café Bazaar, Myket, AdMob, Tapsell, and LevelPlay.
- Add fake providers so the sample can run in Play Mode without live accounts, keys, or ad requests.
- Add initialization state, cancellation, timeout, retry, main-thread callback, and lifecycle tests.
- Document which purchase verification steps must happen on a trusted backend.
- Add a provider/version compatibility matrix and migration notes.
- Never commit real app IDs, ad unit IDs, store public keys, receipts, credentials, keystores, or service-account files.
- Do not redistribute third-party SDK binaries unless their license explicitly permits it.

**Required proof:**

- One 30–45 second demo showing fake purchase success, cancellation, pending purchase, rewarded ad success, and provider failure.
- EditMode tests for domain rules and Play Mode tests for orchestration.
- One tagged preview release and one stable release after real-device verification.

**Authoritative integration references:**

- [Google Mobile Ads Unity quick start](https://developers.google.com/admob/unity/quick-start)
- [Google Mobile Ads test ads](https://developers.google.com/admob/unity/test-ads)
- [Google Play Billing architecture and backend guidance](https://developer.android.com/google/play/billing)
- [Myket Billing Unity](https://github.com/myketstore/myket-billing-unity)
- [Myket Billing Unity Sample](https://github.com/myketstore/myket-billing-unity-sample)
- [Tapsell Plus Unity Plugin](https://github.com/tapsellorg/TapsellPlusSDK-UnityPlugin)
- [Tapsell Mediation Unity Sample](https://github.com/tapsellorg/TapsellMediation-UnitySample)
- [Café Bazaar Unity IAP](https://github.com/cafebazaar/UnityIAP) — treat this older repository as a legacy reference and confirm current requirements in the Bazaar developer dashboard before implementation.

### P0 — Unity-AI-Vehicle-System

**Required scope:**

- Convert the code into an installable UPM package with `Runtime`, `Editor`, `Samples~`, and `Tests` boundaries.
- Split sensing, path intent, steering, speed planning, obstacle response, overtaking, reversing, and recovery into focused components.
- Keep decision logic testable outside `MonoBehaviour` where practical.
- Add a deterministic test track with recorded scenarios and clear pass criteria.
- Add profiler captures for CPU, GC allocations, and vehicle-count scaling.
- Document limitations for NavMesh, wheel physics, traffic rules, and multiplayer authority.
- Add a small architecture diagram and a five-minute Quick Start.

**Required proof:**

- One short demo reel with overlays naming the active AI state.
- Automated tests for stuck detection, target switching, braking decisions, and recovery cooldown.
- A performance table for 10, 25, 50, and 100 vehicles on a declared test machine.

### P0 — Unity-Analytics-Lite

**Required scope:**

- Publish English-first documentation and retain Persian translation separately.
- Version the event envelope and document migrations.
- Add bounded disk storage, atomic queue writes, backoff, cancellation, retry, and corrupted-record recovery.
- Separate event collection, persistence, batching, transport, identity, time, and consent behind focused contracts.
- Add a minimal collector sample with an OpenAPI definition and local Docker option.
- Document privacy boundaries without making legal-compliance claims.

**Required proof:**

- Tests for offline restart, queue truncation, duplicate prevention, invalid payloads, consent changes, and server failures.
- A demo showing events captured offline and flushed after connectivity returns.

### P1 — UnityExportPackageComplete

**Required scope:**

- Remove hard-coded repository paths and direct upload assumptions.
- Keep the tool focused on deterministic package export and manifest generation.
- Convert it into a UPM-compatible Editor package.
- Add validation for selected paths, missing `.meta` files, excluded generated folders, and unsafe output locations.
- Put optional publishing behind a separate interface or GitHub workflow.

**Required proof:**

- EditMode tests for selection, dependency inclusion, file naming, and manifest content.
- A short editor GIF plus a sample release artifact.

### P1 — Helicopter AI Controller

Do not feature this repository until it has a license, a non-duplicated README, an executable sample scene, and a modular refactor. Split flight state, waypoint selection, movement control, rotor presentation, audio, and UnityEvents. Add tests for state transitions and altitude constraints.

## 4. New Community Repositories

Create these only after the first three existing repositories reach a documented release milestone.

| Priority | Repository | Community value | Portfolio coverage |
|---|---|---|---|
| P0 | `unity-mobile-monetization-sandbox` | A runnable reference game for safe IAP/ad integration | 2D, Android, stores, ads |
| P0 | `unity-android-store-pipeline` | Repeatable build variants for Google Play, Bazaar, and Myket | CI/CD, Android publishing |
| P1 | `unity-game-ai-core` | Deterministic FSM, Utility AI, blackboard, and decision tracing | 2D/3D, AI, architecture |
| P1 | `unity-xr-training-kit` | Reusable training tasks, scoring, reset, and evidence capture | VR/MR, serious games |
| P1 | `unity-ar-placement-kit` | Cross-platform placement, anchors, session recovery, and simulation | Mobile AR |
| P1 | `unity-save-migration-kit` | Versioned save DTOs, migrations, backup, and corruption recovery | Production reliability |
| P2 | `unity-rtl-localization-toolkit` | Persian/Arabic UI samples, mixed text, fonts, and layout verification | Regional expertise, UI |
| P2 | `unity-mobile-consent-gateway` | Provider-neutral gating for ads and analytics initialization | Privacy architecture |
| P2 | `unity-performance-lab` | Reproducible pooling, UI, physics, and GC benchmarks | Optimization |
| P2 | `unity-serious-game-assessment-kit` | Scenario objectives, scoring, attempts, evidence, and reports | Simulation, training |

### 4.1 `unity-mobile-monetization-sandbox`

Build a small 2D game loop that demonstrates fake purchases and ads in Play Mode, then optional real provider adapters on Android. Keep it separate from the framework so newcomers can clone and learn without reading package internals.

**MVP:** shop, consumable/non-consumable/subscription examples, rewarded/interstitial/banner examples, consent gate, fake provider console, error simulator, and receipt-verification boundary.

**Important:** Google explicitly provides test ad units and warns against clicking live ads during development. All public samples must default to test mode.

### 4.2 `unity-android-store-pipeline`

Provide reusable scripts and GitHub Actions examples for store-specific product flavors without shipping any secret.

**MVP:** package-name suffixes, store symbols, Gradle/template validation, artifact naming, version-code strategy, environment validation, and local dry run.

**Out of scope:** automatic publishing to real store accounts in the first release. Signing and store uploads require owner-controlled secrets and separate approval.

### 4.3 `unity-game-ai-core`

Create a pure C# decision layer shared by one 2D enemy sample and one 3D agent sample.

**MVP:** FSM, Utility AI scorers, blackboard, time/random abstractions, decision trace, deterministic replay, and Unity presentation adapters.

**Proof:** unit tests for decisions, visual state overlay, comparison scene, and zero-allocation hot-path measurements where claimed.

### 4.4 `unity-xr-training-kit`

Build a modular training framework on OpenXR and XR Interaction Toolkit rather than a headset-specific architecture.

**MVP:** task graph, interactable objectives, hints, scoring, reset, attempt log, comfort settings, desktop simulator path, and one equipment-inspection sample.

**Reference:** [Unity XR documentation](https://docs.unity3d.com/6000.1/Documentation/Manual/XR.html) and [XR Interaction Toolkit](https://docs.unity3d.com/current/Manual/com.unity.xr.interaction.toolkit.html).

### 4.5 `unity-ar-placement-kit`

Build an AR Foundation sample around plane detection, raycasts, anchors, placement state, object manipulation, session reset, tracking loss, and provider capability checks.

**MVP:** XR Simulation scene for editor iteration plus clearly separated ARCore/ARKit provider instructions.

**Reference:** [AR Foundation documentation](https://docs.unity.cn/Packages/com.unity.xr.arfoundation%406.0/manual/index.html).

### 4.6 `unity-save-migration-kit`

Provide a small package for versioned save DTOs, ordered migrations, stable IDs, checksums, atomic replacement, backup recovery, and deterministic tests.

This repository is not visually dramatic, but it is strong evidence for senior production engineering.

### 4.7 `unity-rtl-localization-toolkit`

Demonstrate Persian/Arabic menus, mixed RTL/LTR text, numeric fields, dynamic font fallback, mirrored layouts, controller navigation, and screenshot-based UI tests. Do not bundle fonts without redistribution permission.

### 4.8 `unity-mobile-consent-gateway`

Expose a small consent state machine that prevents ad and analytics providers from initializing before the application has the required state. Keep region policy configurable and explicitly state that the package is an engineering tool, not legal advice.

### 4.9 `unity-performance-lab`

Publish reproducible benchmark scenes for object pooling, physics queries, UI canvas rebuilds, addressable loading, particle budgets, and GC allocations. Every chart must include hardware, Unity version, render pipeline, build mode, and profiler method.

### 4.10 `unity-serious-game-assessment-kit`

Provide a domain-first system for scenario objectives, timed attempts, scoring rubrics, evidence events, replay summaries, and exportable reports. Include one desktop sample and leave XR as a presentation adapter.

## 5. Coverage Matrix

| Capability | Existing proof | Planned proof |
|---|---|---|
| Unity 2D | Monetization/analytics samples | Monetization Sandbox, Game AI 2D sample, RTL Toolkit |
| Unity 3D | Vehicle AI, Helicopter AI | Game AI 3D sample, Performance Lab |
| Google Play | Monetization Framework | Store Pipeline, real-device compatibility matrix |
| Café Bazaar | Monetization Framework | Store Pipeline, fake and sandbox test paths |
| Myket | Monetization Framework | Current Myket provider, sample, compatibility matrix |
| AdMob | Monetization Framework | Test-ad sandbox, consent gating, lifecycle tests |
| Tapsell | Monetization Framework | Current adapter and maintained sample validation |
| VR/MR | Profile claims only | XR Training Kit |
| AR | Profile claims only | AR Placement Kit |
| Serious games | Awards and profile narrative | Assessment Kit + XR Training sample |
| Production reliability | Analytics offline queue | Save Migration Kit, CI, tests, releases |

## 6. Standard Repository Architecture

Use the smallest version of this structure that fits the project:

```text
Repository/
├─ README.md
├─ README.fa.md                  # only when a Persian translation adds value
├─ LICENSE
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ CODE_OF_CONDUCT.md
├─ package.json                  # for UPM packages
├─ Runtime/
│  ├─ Domain/
│  ├─ Application/
│  ├─ Infrastructure/
│  └─ Presentation/
├─ Editor/
├─ Samples~/
├─ Tests/
│  ├─ EditMode/
│  └─ PlayMode/
├─ Documentation~/
└─ .github/
   ├─ ISSUE_TEMPLATE/
   ├─ workflows/
   └─ pull_request_template.md
```

Rules:

- Use assembly definitions for meaningful module boundaries.
- Keep domain rules as independent from `UnityEngine` as practical.
- Keep vendor SDK calls behind project-owned interfaces.
- Use `[SerializeField] private` for inspector references and validate mandatory dependencies.
- Do not use scene searches as normal dependency resolution.
- Use Conventional Commits and one logical change per pull request.
- Preserve Unity `.meta` files and never commit `Library`, `Temp`, `Logs`, build outputs, credentials, receipts, or keystores.
- New abstractions must solve a current problem; avoid framework ceremony.

## 7. README Contract for Every Featured Repository

The first screen must contain:

1. One-sentence problem and value statement.
2. One screenshot or a short compressed GIF/video.
3. Current status: experimental, preview, or stable.
4. Tested Unity and package versions.
5. A five-minute Quick Start.

The full README must also include:

- Features and explicit non-goals
- Architecture diagram
- Installation and removal
- Sample scene path
- API example
- Compatibility matrix
- Test instructions and latest evidence
- Performance notes only when measured
- Known limitations and troubleshooting
- Roadmap and contribution entry points
- License, security, and third-party SDK notices

GitHub's community profile checks for files such as README, LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, and SECURITY: [About community profiles](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories).

## 8. Definition of Release-Ready

A repository can be pinned or announced only when:

- The sample works in the documented Unity editor version.
- Relevant EditMode and Play Mode tests pass deterministically.
- There are no new relevant compiler errors or warnings.
- The README Quick Start was followed from a clean clone.
- Required `.meta` files, package metadata, and assembly references are valid.
- The demo accurately represents current code.
- Secrets and generated Unity folders are not tracked.
- The license and third-party notices are correct.
- The Git diff was reviewed and the release notes are factual.
- Known gaps are stated instead of hidden.

Editor Play Mode is the default development acceptance path. Final store exports, signed Android builds, real ad traffic, and real purchase tests are separate release gates and require the owner's explicit approval.

## 9. Twelve-Week Team Sequence

### Weeks 1–2 — Positioning and proof

- Update public GitHub bio and professional name manually.
- Pin only the four owned Unity repositories.
- Convert Monetization and Analytics documentation to English-first.
- Add status, compatibility, limitations, and contribution files.

### Weeks 3–5 — Existing repository releases

- Refactor and test Monetization provider boundaries.
- Package and test Vehicle AI.
- Stabilize Analytics queue and collector sample.
- Capture one short demo for each repository.

### Weeks 6–7 — Mobile showcase

- Build `unity-mobile-monetization-sandbox` using fake providers first.
- Build the dry-run foundation for `unity-android-store-pipeline`.

### Weeks 8–10 — Game AI and XR

- Build `unity-game-ai-core` with 2D and 3D samples.
- Build the first desktop-testable slice of `unity-xr-training-kit`.

### Weeks 11–12 — AR and release polish

- Build the AR placement MVP with XR Simulation.
- Review all READMEs from a clean clone.
- Publish only the repositories with complete evidence.
- Replace weak pinned items with the strongest new releases.

## 10. Team Work Packages

Each work package should produce a focused pull request:

1. **Repository audit:** inventory code, Unity version, dependencies, licenses, scenes, and current failures.
2. **Architecture boundary:** document existing dependencies before refactoring.
3. **Package structure:** create runtime/editor/test boundaries without changing behavior.
4. **Test evidence:** add deterministic tests for the most valuable failure paths.
5. **Demo:** produce a small executable scene early and capture honest visual proof.
6. **Documentation:** write Quick Start, compatibility, limitations, and troubleshooting in English.
7. **Release:** verify clean clone, tests, demo, Git status, tag, and release notes.

Do not mix a large refactor, formatting pass, visual redesign, and release packaging in one pull request.
