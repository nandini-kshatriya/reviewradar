# ReviewRadar: turning app reviews into a roadmap you can defend

*Product case study · Nandini Kshatriya · October 2026*

> **How to read the labels.**
> - <span class="tag v">Verified</span> a published figure I read in the source itself, with its date and sample.
> - <span class="tag q">Qualitative</span> an observation or quote, not a measurement.
> - <span class="tag r">My analysis</span> a number I computed from public review data. Every one can be reproduced from `scripts/` and the app.
> - <span class="tag a">Assumption</span> my judgment, not yet tested.
> - <span class="tag s">Simulated</span> generated demo data.
>
> I did not interview or survey anyone for this project. All user evidence is secondary.

## In short

- **Problem.** PMs at growing consumer apps get thousands of store reviews a month. Most read a few, remember the angriest ones, and argue priorities from anecdotes.
- **What I built.** A browser-only workspace that tags reviews into topics, checks each release for regressions, compares complaint *rates* with a competitor fairly, and ranks what to fix with a score you can explain. Every ranked item links to the reviews behind it.
- **What the real data showed.** I ran it on **228,274 public Play Store reviews of Swiggy and Zomato written between 6 April and 20 September 2026.** <span class="tag r">My analysis</span>
  - On raw rates, Swiggy looks worse than Zomato on **14 of 16** topics in the last 12 weeks.
  - Comparing only unhappy (1 to 2 star) reviews, Swiggy is clearly behind on **5**, clearly ahead on **4**, and level on the rest. The raw view mostly reflects that Swiggy's reviewers give one star twice as often (30% vs 20%).
  - The gap that survives is **cancellations and refunds**: 19.1 mentions per 100 unhappy Swiggy reviews against 12.4 for Zomato. Customer support is Swiggy's most common complaint, but Zomato's unhappy users raise it just as often, so it is an industry problem rather than a competitive one.
  - The same check on an older 2023 dataset gave the same lesson, which tells me the method matters more than any single finding.
- **Honest positioning.** Basic review tagging is already cheap (Appbot starts at $49 a month). ReviewRadar's angle is narrower: release-linked regression checks, benchmarks that control for rating mix, and a priority score a PM can defend in a review meeting.

## 1. Problem

Store reviews are the cheapest continuous customer signal a consumer app has. They are short, unstructured, sometimes written in Hinglish, and they bunch up around releases. That creates three common failures:

1. **Regressions are noticed late**, because nobody tracks topic share by app version.
2. **Chronic problems get under-weighted**, because they never spike.
3. **Competitor comparisons are naive.** Raw counts or raw rates ignore that two apps attract differently unhappy reviewers.

**Job to be done.** "When I plan the next sprint, I want to know which customer problems are biggest, growing, or worse than a competitor's, so I can defend my priorities with evidence instead of opinion."

## 2. Research (secondary only)

### 2a. Do product teams struggle to turn feedback into priorities?

Every survey below comes from a company that sells PM or feedback software, and none publishes its sampling method. I read them as directional.

| Finding | Source | Date and sample | Label |
|---|---|---|---|
| 1 in 3 teams have no process for capturing feedback. Only 1 in 10 capture it from every source. 51% are confident their roadmap reflects user needs. | Productboard and Product Collective, *Product Excellence Report* | 2020, 700+ PMs | <span class="tag v">Verified</span> vendor survey |
| More than half say decisions follow the highest-paid person's opinion more than data. 3 in 5 say the roadmap does not reflect segment needs. | Productboard and Product Collective | 2021, 850+ respondents | <span class="tag v">Verified</span> vendor survey |
| 35% say customer feedback drove their best feature release | Pendo and Product Collective | Feb 2019, 300 North American PM leaders | <span class="tag v">Verified</span> vendor survey, old |
| "How do you go about evaluating the accuracy of the themes…?" asked on a feedback-analytics launch | Hacker News, Launch HN: Thematic | Aug 2017 | <span class="tag q">Qualitative</span> |
| Loud customers distort priorities. Segment feedback and look for recurring patterns. | Mind the Product | Feb 2025 | <span class="tag q">Qualitative</span> opinion |

### 2b. What does academic work say about reviews as a signal?

| Finding | Source | Data | Label |
|---|---|---|---|
| Feedback bunches up in the days after a release. 52% of reviews cover more than one topic. | Pagano and Maalej, RE 2013 | 1.1M iOS reviews, 1,100 hand-coded | <span class="tag v">Verified</span> |
| Only 35.1% of reviews are "informative" on average. Manual reading took about 7.4 person-hours against 0.5 with tooling. | Chen et al., AR-Miner, ICSE 2014 | 4 Android apps | <span class="tag v">Verified</span> |
| A four-class taxonomy (bug, feature request, experience, rating) reaches 88 to 92% precision | Maalej et al., *Requirements Engineering* 2016 | 4,400 labelled reviews | <span class="tag v">Verified</span> |
| 88% of apps get 20 or fewer reviews a day, so review mining helps less at low volume | McIlroy et al., CACM 2017 | 10,713 Google Play apps | <span class="tag v">Verified</span> |
| The best Hinglish sentiment system scored F1 75% | SemEval-2020 Task 9 (SentiMix) | About 20K Hinglish tweets | <span class="tag v">Verified</span> |

**What this changed in the product.** Tags are multi-label because half of reviews mix topics. There is a version table because complaints follow releases. Alerts have volume gates because small apps are noisy. And there is a tag audit, because even published classifiers make mistakes and my keyword taxonomy is simpler than theirs.

### 2c. Which data did I use, and can I trust it?

I wanted reviews from 2025 or 2026. The Play Store, Kaggle and Hugging Face were not reachable from my build environment, so I could not scrape fresh reviews myself. Instead I looked for a public dataset with a documented method and found one.

| | 2026 dataset (default) | 2023 dataset (kept for comparison) |
|---|---|---|
| Source | [ba-capstone-app-reviews](https://github.com/Adithya-Monish-Kumar-K/ba-capstone-app-reviews) on GitHub, commit 019dae4 | [tanishka-anand compilation](https://github.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence) of a Kaggle scrape |
| Collection method | `google-play-scraper`, every English review from India posted 1 Apr to 20 Sep 2026, sorted newest first. Documented in the repo's `DATA_SOURCES.md`. | Not documented |
| Raw size | 78,562 Swiggy and 159,399 Zomato reviews | 58,588 reviews across both apps |
| Used in the app | 228,274 reviews in 24 complete weeks (6 Apr to 20 Sep 2026) | 58,588 reviews in 26 weeks (23 Jan to 23 Jul 2023) |
| How I checked it | Row counts and date range match the upstream documentation exactly. Every review ID is unique. My pandas recount of average rating and one-star share matches the app. | Row counts only |
| Known problems | A Play Store feed gap from 21 Apr to 5 May 2026, when positive reviews went missing. The app shades those weeks and leaves them out of spike baselines and release checks. 68% of reviews are three words or fewer. | Swiggy's file is 65% one-star against 33% for Zomato, which points to different sampling |

I did not collect this data and I cannot re-run the scrape myself, so I cite it as a third-party dataset. No reviewer names or photos are in either file.

### 2d. What did the 2026 reviews show? <span class="tag r">My analysis</span>

Swiggy is "your app" and Zomato is the competitor. The window is the last 12 weeks (29 Jun to 20 Sep 2026) unless I say otherwise. Default taxonomy.

| Observation | Number |
|---|---|
| Reviews in window | 38,416 Swiggy and 60,484 Zomato |
| Average written-review rating | 3.55 Swiggy and 3.94 Zomato |
| One-star share | 30% Swiggy and 20% Zomato |
| Topics where Swiggy looks behind on raw rates | 14 of 16 |
| Topics where Swiggy is behind among 1 to 2 star reviews (95% interval excludes zero) | 5 of 16: cancellations and refunds, late delivery, offers and coupons, app bugs and login, payments |
| Biggest adjusted gap | Cancellations and refunds, 19.1 vs 12.4 mentions per 100 unhappy reviews (±0.9) |
| Customer support among unhappy reviews | 22.4 Swiggy vs 21.5 Zomato (±1.0), no clear gap |
| Where Swiggy is ahead among unhappy reviews | Cash on delivery, fees and pricing, food quality, membership |
| Top three priorities at default weights | Customer support (7.5% of reviews), cancellations and refunds (6.4%), late delivery (6.2%) |
| Same ranking with upvote weighting on | Top five unchanged, so a few loud reviews are not driving it |
| Release checks for Swiggy | v4.111 (first seen 17 Jun): missing or wrong items rose from 1.3% to 2.0% of reviews (z = 3.8). v4.113 (17 Jul): app bugs and login rose from 1.0% to 1.5% (z = 3.3). |
| Release checks for Zomato | Average rating fell with each version from v19.5 (4.27) to v19.8 (3.99). Customer support rose in v19.6 (2.5% to 4.0%, z = 9.1) and again in v19.8 (3.6% to 4.4%, z = 6.0). |
| Zomato volume and mood | Weekly reviews fell from about 9,700 in April to about 4,500 to 5,000 by September. The 1 to 2 star share rose from 16.1% in the first 12 weeks to 22.0% in the last 12. |
| Spikes in the last two weeks | None for Swiggy. Its complaints are steady and long-running. |
| Very short reviews | 68% are three words or fewer ("good", "nice app"). Only 20% of all reviews match any topic, so the useful text lives in about a quarter of reviews. |

**What a PM at Swiggy could take from this.** Refunds and cancellations are where Swiggy loses to Zomato among unhappy customers, and the gap is large and stable across both windows. Support is the most-mentioned issue, but fixing it would not differentiate Swiggy because Zomato has the same problem. The two release regressions are small but statistically clear, and both are cheap to investigate. <span class="tag a">Assumption</span> on what a Swiggy PM would prioritise. I have no inside data on cost or impact.

**Qualitative themes from reading reviews** <span class="tag q">Qualitative</span>
- The most-upvoted Swiggy review in the window (2,590 upvotes, Aug 2026) describes insects in food and a support reply that offered no fix. It sits at the overlap of food quality and support, which is why tags are multi-label.
- Refund complaints often mention being charged a cancellation fee after a long delay, which points at policy as much as operations.
- Forced rating prompts still appear, so the *Notifications and rating prompts* topic stays in the taxonomy.

**Hinglish.** I expected code-mixed reviews to be the headline problem. In the 2026 data, 7.1% of reviews longer than five words contain common Hinglish words such as *nahi*, *hai* or *bakwas*, and only 0.33% contain Devanagari, probably because the scrape asked for English. Hinglish keywords are supported, but I treat this as hygiene rather than the pitch. <span class="tag r">My analysis</span> using a simple word list, so this is a rough estimate.

### 2e. Does the method hold on a second dataset?

The 2023 data came from a different, undocumented collection, so I do not compare the two years directly. What I can compare is whether the raw-versus-adjusted lesson holds.

| | 2023 (Swiggy, 12 weeks) | 2026 (Swiggy, 12 weeks) |
|---|---|---|
| Behind on raw rates | 9 of 16 | 14 of 16 |
| Behind among 1 to 2 star reviews | 2 of 16 | 5 of 16 |
| One-star share, Swiggy vs Zomato | 63% vs 32% | 30% vs 20% |

In both datasets the raw view overstated the gaps by a factor of two or more. That is the finding I would bring to an interview, because it is about how a PM should read evidence, not about Swiggy.

## 3. Users

- **Primary.** A PM or APM at a Series A to C Indian consumer app who owns a surface and runs weekly prioritisation without a dedicated researcher or analyst. <span class="tag a">Assumption</span> inferred from job descriptions that ask PMs to be "the voice of the customer" and "data-driven" (Flipkart, PhonePe and Razorpay postings read in Oct 2026).
- **Secondary.** A CX lead who needs early warning after a release.
- **Not for.** Apps with only a handful of reviews a day. McIlroy et al. show most apps fall in this group, and ReviewRadar says "not enough data" instead of inventing trends.

## 4. Competitors

| Product | What it does well | Cheapest public price (Oct 2026) | Gap for my user |
|---|---|---|---|
| **Appbot** | Review topics, sentiment, competitor sources, translation | $49 a month for 1 user | Closest and cheap, but not positioned on release regressions or explainable priority |
| **AppFollow** | Review replies, ASO, workflows | Free tier, paid tiers vary (third-party tracker, not verified) | Built for reply operations |
| **Productboard Pulse** | AI topics and trends from Play and App Store reviews inside a PM suite | Not public. Business plan needs at least 5 makers. | Seat minimum and suite overhead |
| **Enterpret** | Adaptive taxonomy across every feedback source | Contact sales | Enterprise onboarding |
| **Unwrap.ai** | Customer intelligence and alerts | From $24,000 a year | Beyond an early-stage budget |
| **Thematic** | Theme discovery and dashboards | $2,000 a month (Capterra listing) | Price and setup effort |
| **SentiSum** | Support and review analytics for CX teams | From $100,000 a year | Enterprise CX buyer |
| **Canny** | Feature-request boards | Free, Pro at $79 a month | Users must post requests, so no review mining |
| **Spreadsheet and reading** | Free and flexible | None | Slow, anecdotal, no trends |

Prices come from vendor pages or listings checked in October 2026 <span class="tag v">Verified</span>.

**Market signals.** MonkeyLearn went to Medallia (2022), data.ai to Sensor Tower (2024) and Kraftful to Amplitude (2025). Review analytics keeps getting absorbed into bigger suites. Several student projects on GitHub also analyse Zomato and Swiggy reviews, so the idea alone is not new.

**Positioning.** For a PM who has outgrown reading reviews by hand but cannot justify an enterprise tool, ReviewRadar answers three questions that cheaper tools do not put first.
- Did the last release make anything worse?
- Are we really behind the competitor once rating mix is controlled for?
- What should we fix first, and which reviews prove it?

## 5. User journey

1. **Load.** Use the built-in 2026 Swiggy and Zomato data, or export your own app and a competitor with the open-source `google-play-scraper` and drop in the CSVs. Nothing is uploaded.
2. **Orient.** Overview leads with one sentence that answers "what matters most right now", then shows volume, rating, negative share, taxonomy coverage, spike alerts and plain-language insights.
3. **Check releases.** Trends compares each version's topic share with the three before it and flags only statistically clear changes.
4. **Compare fairly.** Competitors shows mentions per 100 reviews with 95% intervals and a toggle to compare only unhappy reviews.
5. **Decide.** Prioritize ranks topics by reach, severity, momentum and the adjusted competitive gap. The PM sets strategy weights and effort, reads the evidence, and adds items to Now, Next or Later.
6. **Trust-check.** Tag audit samples 25 tagged reviews. The PM marks each tag right or wrong, and precision appears per topic with an interval once there are at least 10 judgments.
7. **Share.** Copy the roadmap as Markdown with the metric and a real quote attached.

## 6. PRD (MVP)

| ID | User story | Acceptance criteria |
|---|---|---|
| R1 | As a PM, I can load reviews for my app and competitors | The built-in dataset loads in under 5 seconds on desktop broadband. CSV import accepts google-play-scraper and Kaggle column names. An `App` column splits apps. Reviewer names and images are never read. |
| R2 | As a PM, reviews are tagged into topics I control | Editable taxonomy with multi-label tags. Keywords match whole words plus common endings, and `*` marks a prefix. A coverage KPI and an Untagged filter show what the taxonomy misses. |
| R3 | As a PM, I am warned when a topic spikes | Alert when the last two weeks' share of reviews is more than 2 standard deviations above the topic's baseline with at least 4 mentions a week. Known data-gap weeks are excluded from the baseline. |
| R4 | As a PM, I can tie changes to releases | Versions grouped by major.minor with at least 40 reviews. Two-proportion z-test against the previous three versions. Only changes with \|z\| ≥ 2 are shown. |
| R5 | As a PM, I can compare with competitors fairly | Rates per 100 reviews with 95% intervals, a 1 to 2 star comparison, and an adjusted gap inside the priority score when each app has at least 50 unhappy reviews |
| R6 | As a PM, I get a ranked list I can defend | Visible formula, adjustable weights, confidence by sample size, an effort divisor, evidence quotes and optional upvote weighting |
| R7 | As a PM, I can carry decisions into planning | Now, Next and Later board with a suggested success metric per topic. The Markdown export names the data source. |
| R8 | As a PM, I know how far to trust the tags | Tag audit with per-topic precision and Wilson 95% intervals. A topic is marked "fix keywords" when its upper bound is below 80%. |

**Non-goals for the MVP.** Reply management and ASO (Appbot and AppFollow own these), support-ticket ingestion, multi-user workspaces and live store connectors.

## 7. MVP scope and trade-offs

| I chose | Over | What it costs |
|---|---|---|
| A keyword taxonomy | An LLM classifier | Misses paraphrase and sarcasm. In return it is free, instant, private and auditable, and the tag audit measures how wrong it is. |
| Share-based spike alerts | Count-based alerts | Slower to react when volume and share rise together. Zomato's weekly reviews halved between April and September 2026, and Swiggy's ranged from 1,114 (inside the feed gap) to 3,992 a week, so counts would have been mostly noise. |
| Comparing unhappy reviews with unhappy reviews | Raw rates | Smaller samples and wider intervals. It removed most of the false gaps in both datasets. |
| Running everything in the browser | A backend with accounts | No team sharing yet. Imported reviews never leave the PM's machine, which matters for a first trial. |
| A documented third-party dataset | Scraping it myself | I depend on someone else's collection. I verified it against its own documentation and kept every caveat visible in the app. |
| Leaving out a live Play Store connector | Convenience | Users must export CSVs. It avoids scraping-terms risk and maintenance until the value is proven. |

## 8. Prioritizing ReviewRadar's own features (RICE)

Reach is the number of PMs in an imagined pilot of 20. Impact (0.5 to 3), confidence and effort are my estimates <span class="tag a">Assumption</span>.

| Feature | Reach | Impact | Confidence | Effort (weeks) | RICE | Decision |
|---|---|---|---|---|---|---|
| Rating-mix-adjusted benchmark | 16 | 2 | 80% | 0.5 | 51 | MVP |
| Evidence-linked prioritisation | 20 | 3 | 80% | 1.5 | 32 | MVP |
| Tag audit | 20 | 1 | 80% | 0.5 | 32 | MVP |
| Release regression check | 20 | 2 | 70% | 1 | 28 | MVP |
| LLM topic discovery for untagged reviews | 20 | 2 | 50% | 2 | 10 | v2 |
| Weekly Slack digest | 12 | 1 | 50% | 1 | 6 | v2 |
| Live Play Store connector | 20 | 1 | 60% | 3 | 4 | v2 |

## 9. Success metrics

- **North Star.** Roadmap items per active team per month that carry linked review evidence.
- **Activation.** Share of new users who load their own CSV and open Prioritize in the first session.
- **Time to first decision.** Minutes from loading data to the first roadmap item. Target under 10 minutes <span class="tag a">Assumption</span>.
- **Trust.** Audited tag precision of at least 85% on the top five topics, with at least 30 judgments each.
- **Retention.** Share of teams that come back weekly for four weeks.
- **Guardrail.** Share of ranked items a PM marks as obviously wrong stays under 10%.

## 10. Experiment plan

None of these has been run yet. Each is small enough for one person to run with peers.

1. **Does the adjusted benchmark change decisions?** Give 10 to 20 PM peers the same Swiggy and Zomato data. Half see raw rates and half see the unhappy-review view. Primary metric is agreement with a reference list of real gaps. Hypothesis: the adjusted group names fewer and more defensible gaps.
2. **Default weights.** Test a reach-heavy default against a severity-heavy one. Metric is how often users change the weights before adding to the roadmap. Fewer changes means a better default.
3. **Answer-first summary versus charts only.** Metric is click-through from Overview to Prioritize. Guardrail is that audited precision does not drop, because moving faster is worse if it means trusting bad tags.

## 11. Launch strategy

- **Proof first.** Publish a short teardown, "What 228,274 Swiggy and Zomato reviews say, and why raw benchmarks mislead", with the method and data caveats shown.
- **Beta.** Invite 10 to 20 PMs and APMs from product communities and college PM clubs, free.
- **Launch gate.** At least 60% of beta users add an evidence-linked item in week 1, and at least 40% return in week 2 <span class="tag a">Assumption</span>.
- **Pricing hypothesis.** Free for one app, paid for competitor tracking and digests, priced below Appbot's mid tier. To be tested with willingness-to-pay questions, not assumed.

## 12. Limits

- **Keyword tags miss paraphrase and sarcasm.** I have not run a full human audit yet. The tool makes one take about 20 minutes, and until someone does it the app shows no precision figure.
- **Most reviews are too short to tag.** Two thirds are three words or fewer, so topic shares describe the reviewers who wrote something, not every reviewer.
- **Release attribution is approximate.** Reviews of a version include people who updated late.
- **Public reviews are self-selected.** Read them for direction, not as population estimates. Written-review ratings sit below the public store rating.
- **I do not own the data.** It is a third-party scrape with a reported feed gap, and I could not re-collect it.
- **The rider-apps dataset is simulated.** It exists to show the rider-side scenario that led to my second project, Kamai.

## 13. What I got wrong along the way

- **Spike alerts.** My first version, built on simulated data, counted mentions. On real data, changing review volume produced false alerts, so I switched to share of reviews.
- **The competitor view.** I first presented raw gaps as findings, then noticed the one-star mix. The adjusted view reversed the customer-support conclusion in 2023 and turned it into "no clear gap" in 2026.
- **Keyword matching.** Keywords first matched any word that *started* with them, so "late" matched "latest" and a fees complaint showed up as late-delivery evidence. Keywords now match whole words plus common endings, with `*` for deliberate prefixes. That bug is why the tag audit exists.
- **The data gap.** On first load of the 2026 data, Swiggy's rating chart showed a sudden crash in late April. It turned out to be missing positive reviews, documented upstream. I now shade those weeks and exclude them from baselines rather than let the tool report a crisis that did not happen.
- **Hinglish.** I assumed it would be the differentiator. The data did not support that, so I demoted it.

## 14. Next steps

1. Run the tag audit on 30 reviews per top topic and publish the precision table.
2. Run experiment 1 with 10 peers and report the result, whatever it is.
3. Add LLM-suggested topics for long untagged reviews, with the keyword taxonomy kept as the auditable base.

## Sources

- Productboard and Product Collective, 2020 Product Excellence Report (PDF): https://www.productboard.com/wp-content/uploads/2020/10/stateofproductexcellence.pdf
- Productboard and Product Collective, 2021 Product Excellence Report (PDF): https://info.productboard.com/rs/128-JHR-871/images/PE%20Survey%202021.pdf
- MarTech Series on Pendo's State of Product Leadership, 13 Feb 2019: https://martechseries.com/sales-marketing/pendo-releases-2nd-annual-state-product-leadership-survey-revealing-significant-shifts-traditional-product-management-roles-focus/
- Mind the Product, "Why you should ignore your loudest customers", 4 Feb 2025: https://www.mindtheproduct.com/why-you-should-ignore-your-loudest-customers/
- Launch HN: Thematic, Aug 2017: https://news.ycombinator.com/item?id=15020712
- Pagano and Maalej, RE 2013: https://ase.in.tum.de/lehrstuhl_1/images/people/pagano/RE2013PaganoMaalej.pdf
- Chen et al., AR-Miner, ICSE 2014: https://ink.library.smu.edu.sg/sis_research/2323
- Maalej et al., Requirements Engineering 2016 (annotated copy): https://cs.uwaterloo.ca/~dberry/ATRE/Slides/HairyToolsTalk/DanCommentedMaalejEtAl.pdf
- McIlroy et al., CACM, Nov 2017: https://sail.cs.queensu.ca/data/pdfs/2017_UserReviewsOfTopMobileAppsInAppleAndGoogleAppStores.pdf
- Patwa et al., SemEval-2020 Task 9: https://arxiv.org/abs/2008.04277
- Appbot plans: https://appbot.co/plans/ · Unwrap pricing: https://www.unwrap.ai/pricing · Productboard pricing: https://www.productboard.com/pricing/ · Canny pricing: https://canny.io/pricing · SentiSum pricing: https://www.sentisum.com/pricing · Thematic on Capterra: https://www.capterra.co.uk/software/159338/thematic · Enterpret pricing: https://www.enterpret.com/pricing
- Productboard Pulse launch (CIO Dive press release), 29 Oct 2024: https://www.ciodive.com/press-release/20241028-productboard-launches-ai-powered-productboard-pulse-to-integrate-voice-of-c-1/
- TechCrunch, Sensor Tower acquires data.ai, 18 Mar 2024: https://techcrunch.com/2024/03/18/app-analytics-firm-sensor-tower-acquires-rival-data-ai/
- Business Wire, Amplitude acquires Kraftful, 10 Jul 2025: https://www.businesswire.com/news/home/20250710876791/en/Amplitude-Acquires-Kraftful-to-Accelerate-AI-Strategy
- 2026 dataset and its method notes: https://github.com/Adithya-Monish-Kumar-K/ba-capstone-app-reviews (see `DATA_SOURCES.md`)
- 2023 dataset: https://github.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence (from Kaggle `saloni1712/zomato-and-swiggy-play-store-reviews`)

Full research notes, with every figure's sample size and method, are in `research/reviewradar_secondary_research.md`.
