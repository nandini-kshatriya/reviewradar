# ReviewRadar: turning app reviews into a roadmap you can defend

*Product case study · Nandini Kshatriya · October 2026 · about a 6-minute read*

> **How to read the labels.**
> - <span class="tag v">Verified</span> a published figure I read in the source itself.
> - <span class="tag r">My analysis</span> a number I computed from public review data. Each one can be reproduced in the app or from `scripts/`.
> - <span class="tag q">Qualitative</span> a quote or observation, not a measurement.
> - <span class="tag a">Assumption</span> my judgment, not yet tested.
>
> I did not interview or survey anyone, and I have not run the experiment proposed here. All user evidence comes from public app reviews and published research.

## Summary

| | |
|---|---|
| **Question** | If I were a PM at Swiggy, which customer problem should I fix first, and could I defend that choice with evidence? |
| **What I built** | ReviewRadar, a browser-based tool that tags app reviews into topics, compares complaint rates with a competitor fairly, checks releases for regressions and ranks problems with an explainable score |
| **Evidence** | 228,274 public Google Play reviews of Swiggy and Zomato, 6 April to 20 September 2026 |
| **Key insight** | Swiggy looks worse than Zomato on 14 of 16 topics at first glance. On a fair comparison only 4 gaps are real. The largest, **cancellations and refunds**, survives every robustness check, and about a third of it is complaints about cancellation charges. |
| **Recommendation** | A short free-cancellation window right after an order is placed, with the exact charge shown before any later cancellation |
| **How to measure it** | Cancellation-charge complaints per 1,000 cancelled orders, tested in a three-arm A/B test (planned, not run) |

## 1. Problem and user

**The problem.** Consumer apps like Swiggy receive thousands of store reviews a week. They are the cheapest continuous signal of customer pain, but they are short, messy and loudest when people are angry. So teams read a few, remember the worst, and argue priorities from anecdotes. In Productboard's 2021 survey of 850+ respondents, more than half said decisions follow the highest-paid person's opinion more than data <span class="tag v">Verified</span> (a vendor survey, so directional).

**The user.** A PM or APM at a growing Indian consumer app who prioritises weekly without a dedicated analyst <span class="tag a">Assumption</span>, based on PM job descriptions, not interviews. *"When I plan the next sprint, I want to know which customer problems are biggest, growing, or worse than a competitor's, so I can defend my priorities with evidence."*

**Why naive analysis fails.** Three traps appear in real review data, and each one shaped the tool:

| Trap | What goes wrong | What ReviewRadar does |
|---|---|---|
| Raw competitor comparison | The app with harsher reviewers looks worse on everything | Compares unhappy (1 to 2 star) reviews with unhappy reviews, corrected for testing many topics |
| Counting mentions over time | Volume swings. Zomato's halved between April and September 2026. | Tracks each topic's share of reviews |
| Blaming the latest release | Mood drifts over months, so newer versions look worse | Compares versions only within the same weeks |

## 2. Research and insights

**The data.** A documented public scrape of every English Google Play review from India for Swiggy and Zomato, 1 April to 20 September 2026. I rebuilt it from the raw files and matched it to the collectors' documentation. Of 237,961 raw reviews, I use 228,274, dropping only a partial first week (1 to 5 April). A reported feed gap from 21 April to 5 May, when positive reviews went missing, is left out of every comparison. 68% of reviews are three words or fewer, so only about 20% mention a specific topic.

Swiggy is "my app" and Zomato the competitor. Figures cover the last 12 weeks (29 June to 20 September 2026) <span class="tag r">My analysis</span>.

| | Swiggy | Zomato |
|---|---|---|
| Reviews | 38,416 | 60,484 |
| Average written-review rating | 3.55 | 3.94 |
| One-star share | 30% | 20% |
| Unhappy (1 to 2 star) reviews | 12,486 (32.5%) | 13,322 (22.0%) |

### Insight 1: Most of Swiggy's apparent gaps disappear on a fair comparison

On raw rates, Swiggy looks worse on **14 of 16** topics. But more of its reviewers are unhappy to begin with. Comparing unhappy reviews only, and correcting for testing 16 topics at once, Swiggy is clearly behind on **4** topics and clearly ahead on **2** (cash on delivery and membership) <span class="tag r">My analysis</span>. A separately collected 2023 dataset showed the same pattern, with Swiggy's "behind" topics falling from 9 to 1.

### Insight 2: Cancellations and refunds is the largest gap that holds up

I re-tested each gap on longer reviews only, since Swiggy's unhappy reviews are longer (median 14 words against 10) and longer reviews match more keywords, and on the earlier 12 weeks.

Mentions per 100 unhappy reviews, Swiggy vs Zomato <span class="tag r">My analysis</span>:

| Topic | Last 12 weeks | Longer reviews only | Earlier 12 weeks | Verdict |
|---|---|---|---|---|
| **Cancellations and refunds** | **19.1 vs 12.4** | **26.8 vs 19.3** | **20.7 vs 12.5** | **Holds everywhere, largest gap** |
| App bugs and login | 3.5 vs 1.7 | 4.5 vs 2.5 | 3.3 vs 1.6 | Holds, small reach |
| Offers and coupons | 6.2 vs 4.0 | 7.9 vs 4.9 | 5.7 vs 4.3 | Holds, but 43% of its tags are on 4 to 5 star reviews |
| Late delivery | 16.1 vs 13.8 | 20.1 vs 19.0 | 19.0 vs 13.8 | Mostly disappears when length is controlled |
| Customer support | 22.4 vs 21.5 | 30.0 vs 31.7 | 24.3 vs 21.2 | No stable gap |

### Insight 3: Cancellation charges drive a third of that gap

I split cancellation complaints with simple text patterns <span class="tag r">My analysis</span>:

| Inside cancellation and refund complaints | Swiggy | Zomato |
|---|---|---|
| Fee or charge mentioned near "cancel", per 100 unhappy reviews | **3.5** | **1.0** |
| Refund never arrived, per 100 unhappy reviews | 4.3 | 3.6 (no clear difference) |
| Complaint also mentions a delay | 27% | 29% |

Charges explain about 2.5 of the 6.8-point gap, and the difference is stable across six four-week blocks. Delays do not explain it, because both apps' complaints mention them equally often. When Swiggy users say they were charged:

| Situation | Share of Swiggy charge complaints | Swiggy vs Zomato, per 100 unhappy reviews |
|---|---|---|
| Cancelled by mistake or within moments of ordering | 22% | 0.77 vs 0.14 |
| Cancelled because the order was running late | 24% | 0.84 vs 0.37 |
| Charged although the restaurant, rider or app cancelled | 8% | 0.28 vs 0.08 |

The patterns overlap, and about half of complaints fit none of them. Users name the fix themselves <span class="tag q">Qualitative</span>: *"no 30 sec cancelation window"* and *"There should be a buffer time before the preparation of an order starts, like 60 seconds atleast"*.

## 3. Prioritization

ReviewRadar's priority score (reach, severity, momentum and competitive gap, with adjustable weights) puts customer support (49.7) and cancellations and refunds (49.1) in a near tie at the top. The score ranks problems. Choosing one needs judgment about where Swiggy can actually win.

| Candidate | Share of Swiggy reviews | Real gap vs Zomato? | Cause specific enough to act on? | Decision |
|---|---|---|---|---|
| Customer support | 7.5% | No | No, a symptom of many issues | Guardrail |
| **Cancellations and refunds** | **6.4%** | **Yes, robust** | **Partly, charges stand out** | **Focus** |
| Late delivery | 5.6% | Not robust | Operations-heavy | Not now |
| Offers and coupons | 3.3% | Yes | Unclear, many tags are praise | Fix the taxonomy first |
| App bugs and login | 1.3% | Yes | Needs engineering logs | Hand to engineering |

- **Why not customer support?** Zomato's unhappy users raise it just as often, so fixing it would not differentiate Swiggy. It is also downstream of other problems. 37% of Swiggy's cancellation complaints also mention support.
- **Why charges, not refunds?** Missing refunds are a shared industry problem. Charges are where Swiggy is distinctively worse, and they are a policy lever, not a logistics overhaul.

## 4. Product recommendation

**Let users cancel free of charge for a short window right after placing an order, and show the exact charge and refund on the cancel screen once that window closes.** I would start with about 60 seconds <span class="tag a">Assumption</span>, long enough to catch a wrong address or a double tap, and short enough that most kitchens have not started cooking.

### User journey

| Step | Today, as reviews describe it | Proposed |
|---|---|---|
| 1. Spots a mistake right after ordering | Tries to cancel within moments | Cancels inside the free window |
| 2. Cancel screen | Charged even for an immediate cancellation | "Cancel free for the next 42 seconds" |
| 3. After the window | A third of charge complaints say most or all of the order value was kept | Exact charge and refund shown before confirming |
| 4. Afterwards | Contacts support or leaves a 1-star review | Fewer complaints <span class="tag a">Assumption</span> |

### Options and trade-offs

| Option | For | Against | Decision |
|---|---|---|---|
| **Free window plus a visible charge** | Widest Swiggy-to-Zomato ratio (0.77 vs 0.14). Users ask for it. Little food is wasted in the first minute. | Covers only about a fifth of charge complaints. Some users may order carelessly. | **Recommend** |
| Waive the charge on late orders | Similar share of complaints (0.84 vs 0.37) | Loses fee revenue on every late order, and the food is usually cooked | Test next |
| Overhaul customer support | Top of the priority score | No competitive gap, slow and expensive | Guardrail only |
| Faster refunds | A real pain | No Swiggy-specific gap | Later |

The core tension is **fee revenue and restaurant cost against user trust**. The window keeps both costs small by ending before most cooking starts. It is also possible that **clarity alone** solves most of it, if users object to *surprise* charges rather than charges themselves. The experiment tests that separately.

## 5. Success metrics and experiment

| Type | Metric |
|---|---|
| **Primary** | Complaints about cancellation charges per 1,000 cancelled orders, within 7 days (needs Swiggy's support data) |
| **Public proxy** | Cancellation-charge mentions per 100 unhappy Play Store reviews, now 3.5 against Zomato's 1.0. Target below 2.5 within eight weeks of rollout <span class="tag a">Assumption</span>. Trackable in ReviewRadar with a custom topic. |
| **Guardrails** | Orders cancelled in the first minute, restaurant food cost from cancellations, net revenue per order, repeat cancellers |
| **Secondary** | 30-day reorder rate among users who cancelled |

**Planned experiment (not run).**

| | |
|---|---|
| **Design** | Three-arm A/B test, randomised by user so a returning customer always sees the same policy |
| **Arms** | Control is today's flow. Arm A shows the exact charge and refund before confirming. Arm B is Arm A plus a 60-second free window. |
| **What it answers** | A vs control tests whether clarity alone helps. B vs A tests what the free window adds, and what it costs. |
| **Size and duration** | About 12,500 cancelled orders per arm, *if* 2% of cancelled orders lead to a charge complaint and the goal is detecting a fall to 1.5% at 80% power <span class="tag a">Assumption</span>. At least four weeks. |
| **Decision rule** | Ship the cheapest arm that cuts the primary metric by at least 20% with all guardrails inside limits agreed beforehand with finance and restaurant operations |
| **What would change my mind** | A rise in careless or abusive first-minute cancellations, or complaints simply moving from charges to refund timing |

## 6. Limitations and learnings

| Known from the data | Assumed | Still needs validation |
|---|---|---|
| Swiggy's cancellation gap is large, stable and holds on every check I ran | That charge complaints reflect a policy users find unfair or surprising | Swiggy's real cancellation policy, volumes and costs, which are not public |
| Charge complaints are about three and a half times as common on Swiggy | That 60 seconds is short enough to avoid food waste | How accurate the keyword tags are. No human tag audit has been run yet. |
| Users cite mistaken and late orders as charge triggers | That fewer surprises mean fewer complaints and better retention | What causes the other two thirds of the gap |

Reviews are self-selected, so they show direction, not population rates. The text patterns behind Insight 3 are rough pointers, not exact sizes. The data is a third-party scrape that I could not re-collect.

**What I learned by getting things wrong.**
- **Raw comparisons mislead.** I first presented raw gaps as findings. Controlling for rating mix and for testing 16 topics removed most of them.
- **Releases get blamed for trends.** My first release check found four "clear" regressions. Comparing versions within the same weeks, none held. One Zomato spike fell from z = 9.1 to z = 1.6.
- **Missing data can fake a story.** The feed gap made Swiggy's rating look up 0.10 on the previous period when it had slipped 0.03. Every comparison now skips those weeks.

**Next steps.** Hand-label 100 Swiggy cancellation complaints to explain the rest of the gap, run the in-app tag audit on the top topics, and test with 10 PM peers whether the fair comparison changes which gaps they would act on.

## Appendix: about the tool

ReviewRadar runs entirely in the browser, and imported reviews never leave the PM's machine. Its views cover an answer-first overview, a feedback explorer, trends with release checks, the competitor benchmark, prioritisation, an evidence-linked roadmap and a tag audit. Every ranked item links back to the reviews behind it. Basic review tagging is already cheap (Appbot starts at $49 a month <span class="tag v">Verified</span>, Oct 2026), so ReviewRadar's angle is narrower: fair benchmarks, release checks that do not confuse trends with regressions, and a priority score a PM can defend. It is not built for small apps, since 88% of Google Play apps get 20 or fewer reviews a day (McIlroy et al., 2017 <span class="tag v">Verified</span>).

**Sources.** Dataset: [ba-capstone-app-reviews](https://github.com/Adithya-Monish-Kumar-K/ba-capstone-app-reviews), commit 019dae4, with its method in `DATA_SOURCES.md`. The 2023 comparison data is a [public compilation](https://github.com/tanishka-anand/tanishka-anand-zomato-swiggy-review-intelligence) of a Kaggle scrape. Full citations, the competitor landscape, academic research and a verification log for every figure are in `research/reviewradar_secondary_research.md`.
