# Local verification

Verified October 1, 2026, on `codex/engineering-projects-source-audit`.

| Check | Result |
|---|---|
| GitHub Pages/Jekyll production build | Passed with `github-pages` 232 / Jekyll 3.10 |
| Generated local links and fragment targets | 252 checked; zero missing targets |
| Generated image sources and nonempty alt text | 27 image occurrences across nine HTML files; passed |
| Public project reference lists | Three entries; all numbered references cited and all citation fragments resolve |
| Responsive layout | Listing and three entries at 320, 390, 768, and 1440 px; no horizontal document overflow |
| Keyboard focus | Project links keyboard reachable; visible focus outline checked |
| Research isolation | Drafts, extraction archive and coverage CSV outside repository; review docs excluded from output |
| Patch whitespace | `git diff --check` passed |

Browser checks covered 16 page/width combinations. Existing image files were preserved; captions distinguish source figures, archival evidence, and software illustrations. Lazy gallery images on the drag page loaded after scrolling. Screenshot files and DOM check records are in the private review archive.

The validator checks local generated targets, semantic project heading count, numbered citations, alt text, unprocessed template markup, and nested controls. It does not establish the factual correctness of uncleared research, validate the packaged laboratory executable, check every external URL, or certify full accessibility compliance.

## Reproducing the build

With Ruby and Bundler installed, install the existing Gemfile dependencies using `bundle install`, then run `bundle exec jekyll build`. Run `python scripts/check_project_site.py` against the generated `_site` folder. A custom output directory can be supplied as the validator's first argument.

The original Gemfile referred to unavailable GitHub Pages version 257 using invalid constraint syntax. The dependency is pinned to version 232, as listed in the [official GitHub Pages dependency versions](https://pages.github.com/versions/). No front-end library was added. Review used a portable official RubyInstaller runtime and its gems outside the repository, with the existing MSYS compiler and official `make` package.
