# ReviewRadar: Secondary Research Report

**Prepared:** 10 Oct 2026 · **Method:** web search plus direct fetch of vendor pages, papers, review sites and GitHub raw files. **Scope:** five research questions (PM feedback pain, competitors, academic evidence, public discussion, datasets).

**Evidence labels used throughout**
- **[V]**: verified by fetching the primary page or file.
- **[S]**: snippet-only or second-hand (for example a README describing upstream data), unverified.
- **[Vendor]**: published by a company that sells feedback or PM software, so it may be biased.
- **[Own calc]**: my own computation on a downloaded public file.

**Access limits (affect coverage)**
- Reddit is blocked from this environment, so I could not read r/ProductManagement threads.
- GitHub search, both API and HTML, is blocked. GitHub repos were found via web search and checked through repo pages and `raw.githubusercontent.com`.
- Kaggle, Mendeley Data and Hugging Face pages returned only metadata or were blocked.
- Thematic's pricing page and Sensor Tower review-feature pages could not be fetched.

---

## 1. How product teams use feedback, and what is hard

### 1a. Verified quantitative findings

Every survey in this table was run by a vendor of PM or feedback tooling. None disclosed its sampling frame, response rate or margin of error. Treat them all as directional, not representative.

| Source | Date / sample | Key numbers [V unless noted] | Caveats |
|---|---|---|---|
| Productboard + Product Collective, *2020 Product Excellence Report* (PDF) | 2020, 700+ PMs and leaders, many industries | 1 in 3 teams have **no process** for capturing feedback, 43% have "some process", **only 1 in 10** capture feedback from all sources. 52% say ideas are mainly inspired by customer feedback. **39%** name "prioritizing the right products/features" as their top prioritization challenge. Only **51%** are confident their roadmap reflects user needs. "Gathering and synthesizing feedback" is an obstacle for 33%. | [Vendor]. The PDF's chart labels are jumbled, so some label-to-number pairings were inferred from context (flagged by the extraction). |
| Productboard + Product Collective, *2021 Product Excellence Report* (PDF) | 2021, 850+ respondents. Company size: 21% at 0–50 employees, 32% at 51–250. Roles: 34% PM. | **69%** say releases are *not* consistently well received. 43% have a process for capturing feedback relayed by colleagues. **3 in 5** say the roadmap doesn't reflect segment needs. 45% name "aligning stakeholders around prioritization decisions" as the top challenge. More than half say decisions are driven more by HiPPO (highest-paid person's opinion) than by data. 78% don't segment by location. | [Vendor]. Some figures in the PDF text are unlabeled and were excluded. |
| Productboard, *2024 Product Excellence Report* (landing page) | 2024 (4th annual), 500 PMs and leaders, with Products That Count and Product Collective | 70% of large enterprises take ≥1–2 months to make key product decisions. 29% of large enterprises say initiatives rarely or never meet timelines. The landing page has **no** feedback-specific statistics. | [Vendor]. The full report is gated. |
| ProductPlan, *2024 State of Product Management* (blog summary) | 21 Mar 2024, ">1,400 product professionals", 9th edition | 38% name economic uncertainty as the top challenge. 76% say product strategy and 58% say roadmapping are essential jobs-to-be-done for PM tools. More than 50% have identified a first AI use case. The summary has **no** customer-feedback statistics. | [Vendor]. Methodology is not described. |
| Pendo + Product Collective, *State of Product Leadership* (2nd annual), via MarTech Series | Published 13 Feb 2019, 300 North-American PM execs and managers at companies with >$25M revenue | **35%** say customer feedback was the primary driver of their best feature release, 20% say competitive launches. **77%** are evaluated on number of features shipped. | [Vendor]. The data is old, from the US only and from larger companies. |

### 1b. Qualitative observations

- The recurring theme across vendor surveys is that teams say they are customer-driven, but their feedback processes are ad hoc and roadmaps don't visibly trace to user needs. Productboard's 2020 headline findings say this directly [V].
- In Mind the Product's *"Why you should ignore your loudest customers"* (Jim Vincent, 4 Feb 2025) [V], loud customers are often big accounts or amplified by sales and CS. The author argues for segmenting feedback by ideal-customer profile and looking for recurring patterns rather than volume from a few voices. This is a B2B framing. For consumer apps, the analogue is that a few viral 1-star reviews or upvoted (`thumbsUpCount`) reviews can dominate attention.
- In the Hacker News launch thread for Thematic (YC S17, Aug 2017, 72 points, 31 comments) [V via the HN Algolia API]:
  - The founder said companies "don't have the time to sift through the responses."
  - Commenters raised manpower limits ("a ton of feedback... not enough manpower").
  - One commenter raised **trust in automated themes**: "How do you go about evaluating the accuracy of the themes and action items?"
  - Another raised **actionability**: does it give action items, not just sentiment?
- **Market signal [V]:** an HN Algolia search for "customer feedback analysis" returns about 154 stories. The 2023–2026 entries are mostly low-traction "Show HN: AI-powered customer feedback analysis" launches (Painboard, Sentient, Rereflect and others, 1–4 points each). Generic LLM feedback summarization is now a commodity.
- **Reddit:** not accessible. No claims are made about r/ProductManagement sentiment.

---

## 2. Competitor landscape (status as of Oct 2026)

### 2a. Comparison table

Prices are the cheapest **public** price found. "CS" means contact sales. "Hindi/Hinglish" records only what vendor pages state.

| Tool | Target | Key features (from vendor page) | Cheapest public price | Hindi / Hinglish | Gap for an early-stage Indian consumer-app PM |
|---|---|---|---|---|---|
| **Enterpret** [V] | "High-velocity" product orgs. Named customers include Canva, Notion, Strava, Hinge and Atlassian. | Adaptive taxonomy, customer-specific ML models, dedicated data auditors, dashboards, AI agents, MCP server, close-the-loop workflows. A free "App Review Analyzer" tool is advertised. | CS, priced by volume and integrations. Series A of $20.8M led by Canaan, with Peak XV participating (reported Dec 2024) [V]. | Not stated | Enterprise-style, sales-led onboarding. Price is unknown but positioned high. |
| **Unwrap.ai** [V] | Global CX, support, product and VoC teams (DoorDash, GitHub, Perplexity, Oura). | Customer Intelligence, Research Suite, SupportIQ, real-time alerts, PII removal. | **From $24,000/yr**, no per-seat fees, 30-day trial. | "Multilingual support," languages not named | Roughly ₹20 lakh+/yr is out of reach for a Series A PM budget. |
| **Productboard (core + Pulse)** [V] | Product orgs. Pulse is the VoC layer for product leaders. | Insights repository, feedback portals, roadmaps, prioritization, Spark AI. **Pulse** (announced in beta on 29 Oct 2024, general availability planned for Nov 2024) has AI topics, trend analytics, VoC reports and integrations including **Apple App Store and Google Play**. | No public price. Business plan is "request demo" with a minimum of **5 makers**. AI Themes are Enterprise-only. | Not stated | Seat minimum, PM-suite overhead. Capterra reviewers cite cost and complexity, e.g. "Super expensive for something that could theoretically be accomplished in a google doc" (2019). |
| **Canny** [V] | SaaS teams collecting feature requests. | Feedback boards, Autopilot AI that extracts feedback from support and sales conversations, changelog. | **Free** (25 tracked users), Pro **$79/mo** billed yearly. | Not stated | Built for request voting, not app-store review mining or competitor benchmarking. |
| **Dovetail** [V] | Research and insights teams. | Research repository, AI clustering, semantic search, AI dashboards, "opportunity tracking." Mentions "app reviews" as a theme source without saying how they are imported. AI translation into 75 languages. | **Free** (1 project, 1 channel), Enterprise is CS. | Translation listed, no Hinglish claim | Qualitative-research oriented. No release-linked spike detection or competitor review ingestion found. |
| **Thematic** [V via Capterra UK] | Organisations with 201 to 10,000+ employees. | Theme discovery, sentiment, trends, dashboards. | **Starter $2,000/mo** (Capterra listing). The vendor pricing page could not be fetched. | Capterra language list excludes Hindi | Too expensive. Setup effort ("building the code frame") is cited in reviews. |
| **SentiSum** [V] | Enterprise CX and support. | Ticket, call, chat and review analysis, custom taxonomy, Early Warning Agent for anomaly detection. | **From $100,000/yr**. | Not stated | Enterprise support-ops buyer, not a PM. |
| **Chattermill** [V] | Large enterprises (Uber, H&M, Booking.com). | Unified feedback, insights linked to quotes. | CS (demo only) | Not stated | Enterprise-only. |
| **AppFollow** [S, third-party price tracker] | Mobile app teams (review management, ASO). | AI review management, auto-replies/workflows, integrations (Slack, Zendesk, etc.), 10-day trial [V]. | The tracker lists **Free $0**, an ASO tier around $19–29/mo, and Essential about **$129/mo** annual. The tracker's change log is inconsistent, so treat these as unverified. | A review-translation help article exists, Hindi not confirmed | Focus is reply ops and ASO. G2 cons include high price for small teams, confusing UI, and an Essential plan with limited reviews visible [V, G2]. |
| **Appbot** [V] | Mobile app teams. | Sentiment (4 classes), auto topics, custom keyword topics, auto-translation (30+ languages, shown alongside original), replies, competitor tracking via "sources." | **Small $49/mo** annual ($59 monthly): 1 user, 5 sources, 300 translations/mo. Medium $99/$119. 14-day trial. | Translation is opt-in and capped. Hindi not named. Nothing on Hinglish or transliterated text. | Closest functional competitor and cheap. It does not position around release-linked root cause or an evidence-linked prioritized roadmap. No acquisition found (footer "© 2026 Appbot"). |
| **Sensor Tower (incl. data.ai)** [V for deal, S for review features] | Market intelligence for app publishers and investors. | Sensor Tower acquired data.ai (formerly App Annie), announced 18 Mar 2024 (TechCrunch). Review-analysis features could not be verified in this pass. | CS | Not verified | Market-intel suite, review analysis is not its core job. |
| **MonkeyLearn** [V] | (formerly) text-analysis API. | Acquired by **Medallia** (deal closed Feb 2022). `monkeylearn.com` now **302-redirects to medallia.com** (checked 9 Oct 2026). | n/a | n/a | No longer a standalone option. |
| **Medallia / Qualtrics** [V] | Enterprise CX/XM. | Omnichannel experience management, text and sentiment analytics. | No public price. Medallia prices by "Experience Data Record" in annual tiers. Qualtrics has no public price. | Not verified | Enterprise procurement. |
| **Kraftful** [V] | Was a PM-focused AI VoC tool covering app reviews, tickets and calls. | **Acquired by Amplitude, 10 Jul 2025.** Capabilities are being folded into Amplitude. Standalone future not stated. | n/a | Not stated | Shows the category is being absorbed into analytics suites. |
| **Zeda.io** [V via Capterra India] | Companies with 11 to 10,000+ employees. | Feedback management, roadmapping, prioritization, trend analysis. | "Starting $4,999" (period not stated), usage-based, free trial. | Not stated | Reviews mention a cluttered UI and manual data import. |
| **Zendesk QA** | Support-quality scoring | Not researched in depth. It is adjacent (scores agent conversations) rather than a competitor. | — | — | — |

### 2b. Takeaways from the landscape

- **The price structure is barbell-shaped [V].**
  - At the low end are app-review monitors: Appbot at $49/mo, AppFollow with a free tier, and Canny free.
  - At the high end are AI VoC platforms: Unwrap from $24k/yr, SentiSum from $100k/yr, and Thematic at about $2k/mo. Enterpret, Chattermill, Medallia and Qualtrics are CS-only.
  - Productboard Pulse sits in between but needs a 5-maker minimum.
- **None of the fetched vendor pages claims Hinglish or code-mixed handling.** Appbot and Dovetail offer translation. This is an absence of a claim, not proof of absence.
- **Consolidation is under way [V].** MonkeyLearn went to Medallia (2022), data.ai to Sensor Tower (2024) and Kraftful to Amplitude (2025).

---

## 3. App reviews as a signal: academic evidence

| Paper | Data | Key findings [V unless noted] | Relevance / caveat |
|---|---|---|---|
| Pagano & Maalej, "User feedback in the AppStore: an empirical study," *RE 2013* | 1,126,453 reviews, 1,100 iOS apps (550 free, 550 paid), collected Sept 2012. 1,100 reviews manually coded. | **Feedback clusters in the first few days after a release.** In the coded sample: praise 75.4%, bug reports 10.0%, feature requests 6.9%, shortcomings 13.3%. 52% of reviews cover more than one topic. Median length is 61 characters. Bug-report reviews average 1.84★. | Supports release-anchored spike detection and multi-label tagging. iOS only, 2012. |
| Chen et al., "AR-Miner," *ICSE 2014* | 4 Android apps. Labeled test sets of 2,000 reviews per app. | On average **35.1% of reviews are "informative"** (24.6%–55.4% by app). Filter F-measure is 0.76–0.88. Manual inspection of the Facebook test set took about 7.4 person-hours versus about 0.5 with AR-Miner. Rankings agreed with the SwiftKey developers' own (hit-rate 0.70). | Roughly two-thirds of reviews are noise, which justifies an "actionable" filter and quantifies time saved. Small app sample. |
| Maalej, Kurtanović, Nabil & Stanik, "On the automatic classification of app reviews," *Requirements Engineering* 21 (2016) | About 1.3M reviews collected, 4,400 manually labeled (Apple and Google). | Classes: bug report, feature request, user experience, rating. Precision reaches **88–92%** and recall **90–99%** (best configurations). The authors note "the majority of the reviews... is rather non-informative." | A 4-class taxonomy is a proven baseline. Results are on English, curated samples. |
| Guzman & Maalej, "How do users like this feature?" *RE 2014* | 7 apps (Apple and Google) | Fine-grained feature-level sentiment: precision **0.59**, recall **0.51** against manual analysis. | Feature-level extraction is much harder than review-level classification. Show confidence and keep a human in the loop. |
| McIlroy, Shang, Ali & Hassan, "User Reviews of Top Mobile Apps in Apple and Google App Stores," *CACM* 60(11), Nov 2017 | 10,713 top free Google Play apps, crawled 1 Jan – 2 Mar 2014 | **88%** of apps got ≤20 reviews/day, the median app got 0. Only 0.19% got ≥500/day. Both stores show a **review spike after releases**. Google Play reviews are shorter than App Store reviews (two extractions disagreed on the exact median, the PDF says 36 characters). The authors caution that sophisticated mining may give **limited benefit for low-volume apps**. | An important counterpoint: spike detection needs volume. It fits large Indian consumer apps but not small ones. |
| Patwa et al., "SemEval-2020 Task 9: Sentiment Analysis of Code-Mixed Tweets (SentiMix)" | About 20K Hinglish and 19K Spanglish tweets, 61 Hinglish teams | Best Hinglish **F1 = 75.0%** (Spanglish 80.6%). | Even tuned systems are about 75% F1 on Hinglish sentiment. This is tweets, not reviews. |

**Own check on real Indian review data [Own calc]**, run on the GitHub CSVs in §5:
- **Zomato and Swiggy (111,927 reviews, Jan 2022 – Jul 2023):**
  - Devanagari text appears in ≤0.1% of reviews.
  - Reviews with ≥2 common romanized-Hindi markers ("hai," "nahi," "bhai" and similar): 0.2–0.3%.
  - Median length is 17–19 words.
- **PhonePe, Paytm and CRED (2,400 newest reviews, Aug–Sep 2026):**
  - Devanagari: 0.7%. Romanized-Hindi markers: 2.2%.
  - Median **2 words**. 75.9% of reviews are ≤5 words (e.g., "nyc app").
- **Caveat:** these scrapes probably used `google-play-scraper` with `lang='en'` and/or relevance sorting, which filters out much Hindi and Hinglish content. The real share of code-mixed reviews in Indian apps is **unknown from this evidence**. Do not build the pitch on "Hinglish is X% of reviews" without a properly sampled pull.

---

## 4. Public discussion: synthesis pain, loud-customer bias, traceability

| Theme | Evidence | Strength |
|---|---|---|
| Synthesis is laborious | HN Thematic thread (2017): "not enough manpower." AR-Miner measured about 7.4 h → 0.5 h. Productboard 2020: 33% cite gathering/synthesizing feedback as an obstacle. | Moderate. Mixed sources, some vendor. |
| Trust in automated themes | HN comment: "How do you go about evaluating the accuracy of the themes...?" Guzman & Maalej's feature-level P/R of about 0.55. | Moderate |
| Loudest-customer / HiPPO bias | Mind the Product (Feb 2025). Productboard 2021: more than half say HiPPO drives decisions over data. | Moderate (opinion plus vendor survey) |
| Roadmap ↔ feedback traceability | Productboard 2020: 51% confident the roadmap reflects user needs. 2021: 3 in 5 say it doesn't reflect segment needs. A Capterra reviewer: Productboard "doesn't automatically turn insights into feature requests." | Moderate (vendor survey plus anecdote) |
| Crowded generic AI analyzers | Many 1–4-point "Show HN" AI feedback tools, 2023–2026. | Directional |
| Reddit r/ProductManagement | **Not accessed (blocked).** | n/a |

---

## 5. Public datasets of Indian app reviews

### 5a. GitHub, with raw CSV verified

| Repo | Raw URL | Rows | Date range | Columns | License / notes |
|---|---|---|---|---|---|
| `tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence` | `https://raw.githubusercontent.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence/main/data/zomato_dataset.csv` | **62,165** (17.6 MB) | 2022-01-25 → 2023-07-25 | `App, review_date, review_description, rating, thumbsUpCount, developer_response, developer_response_date, appVersion, review_month` | No license stated. Derived from Kaggle `saloni1712/zomato-and-swiggy-play-store-reviews`, whose license was not visible. 293 distinct `appVersion` values (89.8% filled). 66% have a developer reply. |
| same | `.../main/data/swiggy_dataset.csv` | **49,762** (20.1 MB) | 2022-01-25 → 2023-07-24 | same as above | 243 versions (84.7% filled). 64% are 1★ and 99.6% have a developer reply, which suggests a non-random sample. |
| same | `.../main/outputs/reviews_tagged.csv` | 301 | 2022–2023 | above plus `rating_band, half_year, ai_category, ai_reason` | A small LLM-tagged sample, usable as a seed for gold labels (quality unverified). |
| `KarishmaMekaliya/fintech-app-engagement-analytics` | `https://raw.githubusercontent.com/KarishmaMekaliya/fintech-app-engagement-analytics/main/data/fintech_app_reviews_raw.csv` | **2,400** (800 each for PhonePe, Paytm, CRED) | 2026-08-25 → 2026-09-22 | `reviewId, userName, userImage, content, score, thumbsUpCount, reviewCreatedVersion, at, replyContent, repliedAt, appVersion, app_name` | No license stated. **Contains `userName` and `userImage` (PII), drop these on import.** 97 versions. Newest-first sample. |

All row counts and dates above are [Own calc] from the downloaded files. The Zomato and Swiggy totals (111,927) match the repo README.

**Relevance:**
- The Zomato and Swiggy pair is the **best fit** for an MVP demo. It has two direct competitors, about 18 months of data, `appVersion` for release-linked spike detection, `thumbsUpCount` as a severity weight, and developer responses.
- **Licensing is unclear.** Play Store review text is user-generated and subject to Google's terms. Use it for a portfolio demo with attribution, and don't redistribute it.

### 5b. GitHub repos without committed raw data

These are useful as competitor-analysis references or pipelines.

| Repo | What it covers | Data status |
|---|---|---|
| `kaasyapv/Quick-Commerce-NPS-Benchmark-from-App-Reviews` | Blinkit, Zepto and Instamart, about 1M Play reviews (1 Jan 2025 – 30 Sep 2026). README cites Jul–Sep 2026 counts of Blinkit 695,428, Instamart 123,258 and Zepto 294,260. 21k tagged sample. MIT. | `data/` is gitignored. Only `outputs/example_quotes.csv` (20 rows) is public. A similarly named `kaasyapv/quick-commerce-nps-benchmark` currently holds an unrelated turbofan project. |
| `dhruv-deepak/qcommerce-voice-of-customer` | Blinkit, Zepto, Instamart and bigbasket, 128,229 reviews (27 Jul – 25 Sep 2026), 2,000 LLM-labeled reviews. | `data/` is gitignored. Only `outputs/classifier_report.csv`. |
| `AnanyaGeete/quick-commerce-customer-voice` | Blinkit vs Zepto, 22,651 cleaned reviews (2026). | Only `results_summary_tables.xlsx`. No raw text. |
| `sagarmaharana95/digital-friction-project` | PhonePe, GPay, Paytm, Amazon, Flipkart, DigiLocker, mAadhaar, about 4,400 reviews. | README lists CSVs, but the raw paths return **404**. |
| `saniaaa834/Swiggy_Sentiment-Analysis` | 3,000 Swiggy reviews (23–30 Sep 2026), MIT. | CSVs are gitignored. |
| `udaykiran108/UPI-App-Complaint-Intelligence`, `Gaurangityagi/fintech-review-engine` | PhonePe, GPay, Paytm | No data files visible. |
| `Goutam1607/RivalSense-AI` | "Turns public reviews of competing apps into evidence-backed competitive intelligence" for Indian quick-commerce (Next.js plus a Python pipeline). | Synthetic seed data. **Note: this is a near-identical concept to ReviewRadar.** |

**Delivery-partner / rider apps:** no public dataset of Swiggy, Zomato or Zepto partner-app reviews was found on GitHub, Kaggle or Mendeley. To demo the rider-app use case, scrape it yourself (e.g., `in.swiggy.deliveryapp`, `com.zomato.delivery`) and document the method.

### 5c. Not downloadable here (Kaggle / Mendeley / HF), listed for reference [S]

- Kaggle `saloni1712/zomato-and-swiggy-play-store-reviews`: the upstream source. A downstream README says it holds 465,660 reviews from Sep 2018 to Jul 2023.
- Kaggle `mannacharya/blinkit-vs-zepto-vs-instamart-reviews` and `vivekattri/indias-fast-delivery-agents-reviews-and-ratings`: titles only, content unverified.
- Mendeley Data `456vvdfmxj` v1, "Google Playstore_PhonePe Reviews_2016-2026" (R. Joshi, Medi-Caps University, 26 May 2026): row count and license not stated [V metadata].
- Hugging Face `Amiri/Google-Play-Reviews-for-Sentiment-Analysis`: not India-specific.

---

## 6. Is ReviewRadar differentiated or a clone?

**An honest verdict: as a generic "AI tags your app reviews" tool, it is a clone.**
- Appbot ($49/mo) already does topics, sentiment, competitor sources and translation.
- Productboard Pulse ingests Play and App Store reviews.
- Enterpret offers a free App Review Analyzer.
- Dozens of "Show HN" tools and at least one public GitHub project (RivalSense-AI) do near-identical things for Indian quick-commerce.
- Students and PM-portfolio builders have repeatedly built "Zomato vs Swiggy review intelligence" projects (§5).

**A defensible wedge, if it is narrowly scoped, sits in the price and trust gap the market leaves open.**
1. **Release-anchored root cause.** Tie spikes to `appVersion` and release dates. Pagano & Maalej and McIlroy et al. both show reviews spike right after releases. Vendor pages for low-end tools don't position on this. The output should read: "complaint rate for *payments-failed* rose from X% to Y% in v4.12 vs the previous 3 versions."
2. **Normalized competitor benchmarking.** Show complaint *rate* per topic per 1,000 reviews against named competitors, with confidence intervals, rather than raw counts.
3. **Evidence-linked, explainable priority.** Every roadmap item should link to the review IDs behind it, with a transparent score (reach × severity × trend × competitive gap). This answers the "trust the themes?" objection on HN and the roadmap-traceability gap in Productboard's surveys.
4. **India-specific taxonomy and code-mixed robustness** (UPI failures, refunds, delivery ETA, rider behaviour, COD). Treat this as a hygiene requirement, not the headline: my data check could not confirm Hinglish prevalence.
5. **Price and setup.** Self-serve, CSV-first, no 5-seat minimum, priced well below Appbot Medium. Target the Series A PM who today uses a spreadsheet.

The portfolio story should state these gaps explicitly and **name the existing tools**, rather than claim novelty.

---

## 7. Product implications for the ReviewRadar MVP

1. **Filter "actionable" reviews first.** AR-Miner found only about 35% of reviews informative, and in fintech data 76% of reviews are ≤5 words. Make an informative/non-informative filter step one, and show what was filtered out.
2. **Start with a small, proven taxonomy.** Use bug, feature request, UX/experience, praise/rating (Maalej et al. 2016, about 88–92% precision), plus multi-label tagging, since 52% of reviews hold more than one topic. Layer domain topics (payments, delivery, refunds, rider) on top.
3. **Make `appVersion` and release date first-class.** Spike detection should compare a version's topic rate against a baseline window. Use the Zomato/Swiggy dataset (243–293 versions) for the demo.
4. **Gate spike alerts on volume.** McIlroy et al. show most apps get ≤20 reviews/day. Show "insufficient data" instead of noisy alerts, and report confidence intervals.
5. **Benchmark rates, not counts.** Normalize per 1,000 reviews and per rating band, because competitor datasets differ in sampling (the Swiggy file is 64% 1★, which suggests skew).
6. **Make every insight explainable.** Each priority item shows the formula inputs and links to representative review IDs and quotes. Weight by `thumbsUpCount` to counter the "loudest single reviewer" effect while still surfacing widely agreed complaints.
7. **Keep a human in the loop on tags.** Feature-level sentiment hits only about 0.55 P/R and Hinglish sentiment tops out around 75% F1. Let PMs correct tags, track agreement, and publish a small gold-set accuracy figure. That is a credibility asset for the portfolio.
8. **Handle code-mixing without overclaiming.** Support Devanagari and romanized-Hindi keyword lists in topic rules. Measure prevalence on a properly sampled (`lang` unrestricted) pull before marketing Hinglish as a differentiator.
9. **Strip PII on import** (`userName`, `userImage`) and add a data-source and terms note. Do not redistribute review text.
10. **Leave out reply management, ASO and support-ticket ingestion in the MVP.** Appbot and AppFollow own those. The roadmap-evidence output is the product.

---

## 8. Source list

**Surveys / reports**
- Productboard, 2020 Product Excellence Report (PDF), 2020: https://www.productboard.com/wp-content/uploads/2020/10/stateofproductexcellence.pdf
- Productboard, 2020 report blog: https://www.productboard.com/blog/2020-state-of-product-excellence-survey
- Productboard, 2021 Product Excellence Report (PDF), 2021: https://info.productboard.com/rs/128-JHR-871/images/PE%20Survey%202021.pdf
- Productboard, 2024 Product Excellence Report landing page: https://productboard.com/ebook/2024-product-excellence-report
- ProductPlan, "Busy PM's Guide to the 2024 State of Product Management Report," 21 Mar 2024: https://www.productplan.com/blog/the-busy-product-managers-guide-to-the-state-of-product-2024
- MarTech Series on Pendo's 2nd State of Product Leadership, 13 Feb 2019: https://martechseries.com/sales-marketing/pendo-releases-2nd-annual-state-product-leadership-survey-revealing-significant-shifts-traditional-product-management-roles-focus/

**Competitors**
- Enterpret pricing: https://www.enterpret.com/pricing
- Enterpret home: https://www.enterpret.com/
- Enterpret Series A (Pulse 2.0), 5 Dec 2024: https://pulse2.com/enterpret-ai-based-customer-feedback-intelligence-company-raises-20-8-million-series-a
- Unwrap pricing: https://www.unwrap.ai/pricing
- Productboard pricing: https://www.productboard.com/pricing/
- Productboard Pulse pricing: https://productboard.com/pricing/pulse
- Productboard Pulse launch (CIO Dive press release), 29 Oct 2024: https://www.ciodive.com/press-release/20241028-productboard-launches-ai-powered-productboard-pulse-to-integrate-voice-of-c-1/
- Productboard Capterra reviews: https://www.capterra.com/p/160651/productboard/reviews/?page=6
- Canny pricing: https://canny.io/pricing
- Dovetail pricing: https://dovetail.com/pricing/
- Thematic on Capterra UK: https://www.capterra.co.uk/software/159338/thematic
- SentiSum pricing: https://www.sentisum.com/pricing
- Chattermill pricing: https://chattermill.com/pricing
- AppFollow pricing: https://appfollow.io/pricing
- PricingSaaS tracker for AppFollow (last seen 4 Jul 2026): https://pricingsaas.com/companies/appfollow
- AppFollow on G2: https://www.g2.com/products/appfollow/reviews
- Appbot plans: https://appbot.co/plans/
- Appbot pricing: https://appbot.co/pricing
- Appbot non-English reviews help article: https://support.appbot.co/help-docs/how-does-appbot-handle-non-english-reviews/
- TechCrunch, Sensor Tower acquires data.ai, 18 Mar 2024: https://techcrunch.com/2024/03/18/app-analytics-firm-sensor-tower-acquires-rival-data-ai/
- Bloomberg Línea, Medallia acquires MonkeyLearn, 6 May 2022: https://www.bloomberglinea.com/2022/05/06/startup-uruguaya-de-machine-learning-fue-adquirida-por-norteamericana-medallia/
- monkeylearn.com (302 redirect to medallia.com, checked 9 Oct 2026): https://monkeylearn.com/
- Medallia pricing: https://www.medallia.com/pricing/
- Qualtrics pricing: https://www.qualtrics.com/pricing/
- Business Wire, Amplitude acquires Kraftful, 10 Jul 2025: https://www.businesswire.com/news/home/20250710876791/en/Amplitude-Acquires-Kraftful-to-Accelerate-AI-Strategy
- Zeda.io on Capterra India: https://www.capterra.in/software/1017874/zedaio

**Academic**
- Pagano & Maalej, RE 2013: https://ase.in.tum.de/lehrstuhl_1/images/people/pagano/RE2013PaganoMaalej.pdf
- Chen et al., AR-Miner, ICSE 2014 (record): https://ink.library.smu.edu.sg/sis_research/2323
- Chen et al., AR-Miner (PDF): https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=3323&context=sis_research
- Maalej et al., Requirements Engineering 2016 (annotated copy): https://cs.uwaterloo.ca/~dberry/ATRE/Slides/HairyToolsTalk/DanCommentedMaalejEtAl.pdf
- Guzman & Maalej, RE 2014: https://research.vu.nl/en/publications/how-do-users-like-this-feature-a-fine-grained-sentiment-analysis-/
- McIlroy et al., CACM, Nov 2017: https://sail.cs.queensu.ca/data/pdfs/2017_UserReviewsOfTopMobileAppsInAppleAndGoogleAppStores.pdf
- Patwa et al., SemEval-2020 Task 9 (SentiMix): https://arxiv.org/abs/2008.04277

**Discussion**
- Mind the Product, "Why you should ignore your loudest customers," 4 Feb 2025: https://www.mindtheproduct.com/why-you-should-ignore-your-loudest-customers/
- Launch HN: Thematic, Aug 2017: https://news.ycombinator.com/item?id=15020712 (read via https://hn.algolia.com/api/v1/items/15020712)
- HN Algolia search for "customer feedback analysis": https://hn.algolia.com/api/v1/search?query=customer%20feedback%20analysis&tags=story

**Datasets**
- https://github.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence
- https://github.com/KarishmaMekaliya/fintech-app-engagement-analytics
- https://github.com/kaasyapv/Quick-Commerce-NPS-Benchmark-from-App-Reviews
- https://github.com/dhruv-deepak/qcommerce-voice-of-customer
- https://github.com/AnanyaGeete/quick-commerce-customer-voice
- https://github.com/sagarmaharana95/digital-friction-project
- https://github.com/saniaaa834/Swiggy_Sentiment-Analysis
- https://github.com/udaykiran108/UPI-App-Complaint-Intelligence
- https://github.com/Gaurangityagi/fintech-review-engine
- https://github.com/Goutam1607/RivalSense-AI
- https://www.kaggle.com/datasets/saloni1712/zomato-and-swiggy-play-store-reviews
- https://www.kaggle.com/datasets/mannacharya/blinkit-vs-zepto-vs-instamart-reviews
- https://data.mendeley.com/datasets/456vvdfmxj/1
