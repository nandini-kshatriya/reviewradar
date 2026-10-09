# ReviewRadar

ReviewRadar turns public app-store reviews into a product roadmap a PM can defend. It tags reviews into topics, checks each release for regressions, compares complaint rates with a competitor fairly, and ranks what to fix with a score you can explain. Every ranked item links back to the real reviews behind it.

It ships with **228,274 real Google Play reviews of Swiggy and Zomato written between 6 April and 20 September 2026**, plus an older 2023 dataset and a simulated rider-app dataset.

Portfolio project by Nandini Kshatriya, built while preparing for Associate Product Manager roles.

- **Live demo:** see the link in the repository description (hosted as a static page)
- **Product case study:** [`docs/case-study.md`](docs/case-study.md), also inside the app under *Case study*
- **Research notes:** [`research/`](research)

![Overview](docs/screenshots/desktop-overview.png)

## What it does

| View | What a PM gets |
|---|---|
| Overview | One sentence that answers "what matters most right now", then volume, rating, negative share, taxonomy coverage, spike alerts and generated insights |
| Feedback | Search and filter every review by topic, rating and sentiment, with matched keywords highlighted |
| Trends and releases | Weekly topic trends, share-based spike detection, and a release check that compares each app version with the three before it |
| Competitors | Mentions per 100 reviews with 95% confidence intervals, defaulting to a comparison of unhappy (1 to 2 star) reviews only |
| Prioritize | A transparent score built from reach, severity, momentum and competitive gap, with adjustable weights, effort sizing and evidence quotes |
| Roadmap | A Now, Next and Later board where each item keeps its score, evidence count, a real quote and a suggested success metric. Exports to Markdown. |
| Tag audit | Judge a random sample of tags and get precision per topic with Wilson 95% intervals |
| Case study | The full APM write-up: problem, research, PRD, trade-offs, metrics, experiments and limits |

## Key finding from the 2026 data

On raw complaint rates, Swiggy looks worse than Zomato on 14 of 16 topics over the last 12 weeks. Comparing only unhappy reviews, it is clearly behind on 5, clearly ahead on 4, and level on the rest. The biggest real gap is cancellations and refunds (19.1 vs 12.4 mentions per 100 unhappy reviews). The full analysis, with its caveats, is in the case study.

## Tech stack

| Layer | What is used |
|---|---|
| Frontend | A single `index.html` with vanilla JavaScript (no framework), hand-written CSS with light and dark themes |
| Charts | Chart.js 4.4.1, vendored in `vendor/` |
| CSV import | PapaParse 5.4.1, vendored in `vendor/` |
| Fonts | Geist and Geist Mono, self-hosted in `fonts/` (SIL Open Font License) |
| Data | Precomputed JSON in `data/`, built offline with Python 3 and pandas |
| Backend and database | None. Everything runs in the browser. Saved tags, weights and roadmap items live in the browser's `localStorage`. Imported files are never uploaded. |
| Hosting | Any static host (GitHub Pages, Netlify, Vercel, Cloudflare Pages) |

## Run it locally

The app fetches its dataset with `fetch()`, so open it through a local web server rather than double-clicking the file.

```bash
git clone <this repository>
cd reviewradar
python3 -m http.server 8000
# open http://localhost:8000
```

No build step and no install is needed to run the app.

## Rebuild the dataset (optional)

```bash
pip install pandas
# download data/raw/swiggy.csv.gz and data/raw/zomato.csv.gz from
# https://github.com/Adithya-Monish-Kumar-K/ba-capstone-app-reviews (commit 019dae4)
python3 scripts/prepare_data_2026.py swiggy.csv.gz zomato.csv.gz data/zomato_swiggy_2026.json
```

`scripts/prepare_data.py` rebuilds the 2023 file. `scripts/build_case.py` renders `docs/case-study.md` into the app's Case study view (it needs the `marked` CLI from npm).

## Use your own reviews

Click **Import reviews** and drop in one CSV per app. ReviewRadar reads the columns that the open-source `google-play-scraper` Python package exports (`content`, `score`, `at`, `reviewCreatedVersion`) as well as Kaggle-style names. The import dialog shows a short script to export reviews for any app.

## Environment variables

None are needed. The app is static and has no server, API keys or secrets. A [`.env.example`](.env.example) file is included to make that explicit.

## Deploy

1. Push this folder to a GitHub repository.
2. In the repository settings, open **Pages**, choose **Deploy from a branch**, and pick `main` with the root folder.
3. The site appears at `https://<username>.github.io/reviewradar/` within a few minutes.

The 2026 data file is about 14 MB, which is within GitHub's 100 MB file limit and loads in a few seconds on broadband.

## Data sources and honesty notes

| Dataset | Source | Collection method | Caveats |
|---|---|---|---|
| Swiggy and Zomato, Apr to Sep 2026 (default) | [ba-capstone-app-reviews](https://github.com/Adithya-Monish-Kumar-K/ba-capstone-app-reviews), commit 019dae4 | `google-play-scraper`, every English review from India, newest first, 1 Apr to 20 Sep 2026, documented in the source's `DATA_SOURCES.md` | Feed gap from 21 Apr to 5 May 2026 when positive reviews went missing (shaded in charts and excluded from baselines). 68% of reviews are three words or fewer. No license is stated upstream, so it is used for a non-commercial demo with attribution. |
| Swiggy and Zomato, Jan to Jul 2023 | [tanishka-anand compilation](https://github.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence) of a Kaggle scrape | Not documented upstream | Swiggy's file is far more one-star heavy than Zomato's, which suggests different sampling |
| Rider apps | Generated in the browser from hand-written templates | Seeded random generator | **Simulated.** No real users or reviews. |

I verified that the 2026 row counts and date range match the upstream documentation and recomputed headline numbers independently in pandas. I did not collect the reviews myself. No reviewer names or images are stored.

The app never shows an accuracy figure for its tags until a person has judged at least 10 of them in Tag audit.

## Project structure

```
index.html                 the whole app (markup, styles, logic)
data/                      review datasets as compact JSON
docs/case-study.md         APM case study (source of the in-app Case study view)
docs/screenshots/          screenshots used in this README
research/                  secondary research notes with sources, dates and sample sizes
scripts/                   data preparation and case-study build scripts
vendor/                    Chart.js and PapaParse with their licenses
fonts/                     self-hosted fonts with their license
```

## Screenshots

| | |
|---|---|
| ![Prioritize](docs/screenshots/desktop-prioritize.png) | ![Trends](docs/screenshots/desktop-trends.png) |
| ![Competitors](docs/screenshots/desktop-competitors.png) | ![Roadmap](docs/screenshots/desktop-roadmap.png) |
| ![Tag audit](docs/screenshots/desktop-audit.png) | ![Dark mode](docs/screenshots/dark-overview.png) |

<img src="docs/screenshots/phone-overview.png" width="260" alt="Overview on a phone"> <img src="docs/screenshots/phone-prioritize.png" width="260" alt="Prioritize on a phone">

## Limits

- Keyword tags miss paraphrase and sarcasm. Precision is unmeasured until someone runs the tag audit.
- Release attribution is approximate because some reviewers update late.
- Public reviews are self-selected. Read them for direction, not as population estimates.
- No user research was run for this project. All user evidence is secondary and labelled in the case study.
