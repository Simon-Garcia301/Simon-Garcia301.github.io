# Engineering Projects update

October 1, 2026. Review branch: `codex/engineering-projects-source-audit`.

The three existing project entries retain their collection paths and navigation destinations. New research entries remain private drafts outside this repository because publication clearance is outstanding. No new research measurements, figures, or source documents were added to the public site.

## Changes

- **Drag analysis:** renamed around the actual window-configuration CFD experiment; identified imported geometry and Simon's edits; qualified the frontal-area approximation and numerical checks; added methods, limitations, descriptive media captions, and numbered references. Retained the already-present power/energy results with the correct comparison.
- **Laboratory software:** distinguished implemented features from measured performance; credited co-development of line-width analysis; described the intensity statistic accurately; identified the existing graphics as illustrations; cited implementation files.
- **Desk illumination:** preserved the entry, URL, heatmap, and relevant geometry illustrations while clearly describing the missing primary report and incomplete measurement provenance.
- **Presentation:** added explicit ordering, an Engineering Projects heading, descriptive alt text, captioned figures, reliable source-relative asset paths, project focus indicators, responsive grid sizing, and improved project-link/skill contrast. Removed the nested button inside each card link.
- **Build:** replaced invalid/unavailable GitHub Pages dependency syntax with the published version 232. Review documentation and unrelated template instructions are excluded from generated site content. No front-end dependency was added.

## Removed or qualified content

Nothing was deleted from the supplied source folder. Existing image files and laboratory software code remain unchanged.

| Previous content | Treatment and reason |
|---|---|
| Drag-page title and conclusion comparing windows with air conditioning | Replaced: the experiment did not measure AC power or fuel consumption |
| Claimed average drag coefficients and derived percentage | Omitted: the report's averages do not reconcile with its per-speed table |
| Drag-coefficient plot | Removed from the page but retained as an asset: displayed values also differ from the report's coefficients |
| Generic CFD claims of “settling” fuel economy and negligible city-speed effects | Removed as unsupported conclusions |
| DIW “real lab workflow” sample numbers and time savings | Removed: an illustrative documentation scenario was presented as measured performance |
| Software novelty, compliance, deployment-readiness, and broad compatibility claims | Removed: not established by the supplied implementation |
| “Surface roughness” as a calibrated physical measurement | Replaced with precise image-intensity variation terminology; original UI label explained |
| Software installation/build snippets | Removed from the portfolio entry: packaged imports/assets are unresolved; source references remain available |
| Desk sample count, grid spacing, meter precision, model confirmation, and illumination-efficiency claims | Withheld pending primary report/data reconciliation |
| Desk equations and incomplete Python dataset example | Removed from the page pending review of model geometry and complete measurement provenance |
| Desk sphere/inverse-square illustrations | Removed from the page but retained as assets; origin and model applicability are unresolved |
| Duplicate opening overview sections | Consolidated into the existing summary and context structure |
| Template README and Reference folder in generated output | Excluded from the build; both remain in the repository |

## Reference coverage

All 2,168 supplied files and 82 original website files are recorded in the private coverage register. Every row has a use or exclusion reason and an honest review status. The register, source extracts, raw research files, and drafts are stored outside this repository and cannot be copied into the public output by Jekyll.

| Public entry | References actually used |
|---|---|
| Drag analysis | Supplied Physics IA report; résumé ver. 6; retained CFD/geometry/force images checked against the report |
| DIW laboratory software | G-code, line-width, and intensity engines; launcher, three GUI modules, shared UI, and build specification; illustration-generation script; résumé ver. 6 |
| Desk illumination | Original portfolio entry at snapshot `07bd891`; preserved heatmap and geometry images, explicitly identified as incomplete archival evidence |

The private print-optimization draft cites the primary Trial 6 export, RSM narrative report, preliminary experiment workbook, and résumé. The private electrical-characterization draft cites the analysis script, per-line/summary CSVs, revision report, captions, and résumé. These references and their values are not published by this change.

## Open Questions

- Which Lee Research Group descriptions, results, figures, calibration details, and code links are cleared for public use?
- Are porous piezoelectric vascular sensors a separate project from the conductive PDMS/CNT work? Their results must remain distinct.
- Who is the line-width co-developer, and which modules/experiments did each contributor perform?
- Which RSM and conductivity workbook versions are authoritative, and how should concentration coding and measurement exclusions be reconciled?
- Where are the original desk report, instrument information, and full measurement records?
- Which raw CFD calculations support the report's coefficient summaries and plotted values?
- Which fixtures did Simon design, adapt, or only fabricate, and what are the source-model licenses?
- Does the packaged tool-suite executable match the supplied source and required assets?
- Are the listed next steps still planned, or have documented confirmation experiments been completed?

## Verification record

See `verification.md` in this excluded documentation folder for actual build/check outcomes. A successful build is required before presenting the branch as locally verified. Source-review limitations and outstanding publication decisions remain in the private final report.
