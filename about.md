# About this plan

The reasoning, resources and conventions behind [the roadmap](README.md).

A 24-evening plan for the AWS Certified Cloud Practitioner exam (CLF-C02),
booked for **Monday 30 November 2026**, at 60 to 90 minutes an evening.

This is a different kind of repository from the other two. The AI Practitioner
and Solutions Architect repos are project portfolios. This one is a study plan,
and the reason it can be short is that most of CLF-C02 is already covered by
holding AIF-C01 and preparing for SAA-C03. What is left is a **memorisation
sprint** on the four areas neither of those touch, plus a **recognition sweep**
of the service catalogue, which is a third of the exam.

The four areas off the SAA path, and where they live here:

| Area | Why it needs its own pass | File |
|---|---|---|
| Support plan tiers | Pure memorisation: response times, TAM, Trusted Advisor scope | [notes/04](notes/04-billing-pricing-support.md) |
| Billing tools | Budgets vs Cost Explorer vs CUR vs Pricing Calculator vs Billing Conductor | [notes/04](notes/04-billing-pricing-support.md), [C1](projects/c1-cost-controls) |
| Pricing mechanics | RIs vs Savings Plans vs Spot vs Dedicated, data transfer rules, Free Tier | [notes/04](notes/04-billing-pricing-support.md), [C2](projects/c2-pricing-api) |
| Business framing | CapEx vs OpEx, TCO, the six advantages, Well-Architected pillars by name, 7 Rs | [notes/01](notes/01-cloud-concepts.md) |

## The exam

| | CLF-C02 |
|---|---|
| Questions | 65, of which 50 scored and 15 unscored trial items you cannot identify |
| Time | 90 minutes |
| Format | Multiple choice (one of four) and multiple response (two or more of five) |
| Passing | 700 on a scaled range of 100 to 1000. Not 70% correct: questions are weighted and the score is scaled. |
| Delivery | Pearson VUE, test centre or online proctored |
| Date | Monday 30 November 2026 |

Confirm the weights below on the official exam guide before the first practice
exam. They are CLF-C02 as of November 2026.

The full blueprint, every task statement across all four domains with a
self-rating column, is [notes/00-baseline.md](notes/00-baseline.md). It is
the map; the week plans are the route.

| Domain | Weight | Notes | Week |
|---|---|---|---|
| 1 · Cloud Concepts | 24% | [notes/01-cloud-concepts.md](notes/01-cloud-concepts.md) | 1 |
| 2 · Security and Compliance | 30% | [notes/02-security-compliance.md](notes/02-security-compliance.md) | 2 |
| 3 · Cloud Technology and Services | 34% | [notes/03-technology-services.md](notes/03-technology-services.md), [service-catalogue.md](notes/service-catalogue.md) | 3 |
| 4 · Billing, Pricing and Support | 12% | [notes/04-billing-pricing-support.md](notes/04-billing-pricing-support.md) | 1 |

Domain 4 is only 12% but it is where the unfamiliar material is, so it goes in
week 1 and gets revisited every week. Domain 3 is the biggest and is mostly
"which service does X", so it is a recognition exercise rather than a study
one, and [exam-traps.md](notes/exam-traps.md) is the flashcard deck for it.

## The four weeks

| Week | Dates | Focus | Projects | Practice |
|---|---|---|---|---|
| [1](plan/week-1.md) | Fri 6 to Thu 12 Nov | Cloud Concepts, Billing, Pricing and Support | C1, C2 | Baseline: free official 20-question set |
| [2](plan/week-2.md) | Fri 13 to Thu 19 Nov | Security and Compliance | C3 | Practice exam 1 |
| [3](plan/week-3.md) | Fri 20 to Thu 26 Nov | Technology and Services | C4 | Practice exam 2 |
| [4](plan/week-4.md) | Fri 27 to Sun 29 Nov | Practice and review only | none | Practice exam 3 |

Thursday 26 November is Thanksgiving and is planned as a buffer, not a study
day. If a week slips, the buffer absorbs one evening and week 4 absorbs one
more. If it slips more than that, cut C4, not the practice exams.

## The evening

Every evening has the same shape, so there is nothing to decide at 8pm.

| Minutes | What |
|---|---|
| 0 to 15 | Review: one category of [service-catalogue.md](notes/service-catalogue.md), two sections of [exam-traps.md](notes/exam-traps.md), cover-and-recall |
| 15 to 75 | The day's item from the week plan |
| 75 to 90 | Self-test on what was just read, or the project write-up |
| last 5 | Log it in [practice/log.md](practice/log.md) and anything missed in [practice/weak-spots.md](practice/weak-spots.md) |

The daily plan assumes 60 to 90 minutes. Days marked **long** need the full
two hours (the timed practice exams and C4). Days marked **short** can be done
in 45.

## The projects

Four, each one evening, each costing nothing or close to it, each torn down the
same evening. They exist because the exam asks about Budgets, IAM policy
evaluation and the EC2 stop-versus-terminate lifecycle, and twenty minutes in
the console beats an hour of reading for all three.

| | Project | What it proves | Cost | Week |
|---|---|---|---|---|
| **C1** | [Cost controls](projects/c1-cost-controls) | Budgets, Cost Explorer, cost allocation tags and the Pricing Calculator, each used once for real | None | 1 |
| **C2** | [Pricing API](projects/c2-pricing-api) | On-Demand against every Reserved option for one instance, from the API rather than a course slide | None | 1 |
| **C3** | [IAM hygiene](projects/c3-iam-hygiene) | Explicit deny beats allow, proved with the policy simulator. Root MFA, credential report, Access Analyzer, CloudTrail | None | 2 |
| **C4** | [Service tour](projects/c4-service-tour) | S3, EC2, Lambda and CloudWatch in one evening. What a stopped instance loses and a terminated one does not get back | Pennies, if torn down the same evening | 3 |

The build is yours. Each README is a checklist with a checkpoint command after
every step; the write-up at the end is from what you observed, not what the
docs say. Same rule as the SAA repo.

## Resources

Free first. The paid item is the one worth paying for.

| Resource | Use | Cost |
|---|---|---|
| [Official exam guide](https://docs.aws.amazon.com/aws-certification/latest/examguides/cloud-practitioner-02.html) | Read once on day 1. The in-scope service list at the end is the catalogue. | Free |
| [AWS Skill Builder: official practice question set, CLF-C02](https://skillbuilder.aws/) | 20 questions, the baseline on day 1 | Free |
| [AWS Skill Builder: Exam Prep Standard Course, CLF-C02](https://skillbuilder.aws/) | Skim the domain 4 modules only; the rest is covered | Free |
| [Tutorials Dojo CLF-C02 cheat sheets](https://tutorialsdojo.com/aws-cheat-sheets/) | Second opinion on any service that is fuzzy after the notes | Free |
| Tutorials Dojo CLF-C02 practice exams | The three full-length timed exams in weeks 2, 3 and 4. Review mode after each. | Paid |
| AWS Skill Builder official practice exam | Alternative to the above if a Skill Builder subscription is already in place | Paid |

Skip the full "Cloud Practitioner Essentials" course. It is six hours of
material already covered by the two other certifications.

## Conventions

- **No cost figure appears in this repository until it has been through the
  Pricing API.** Same rule as the SAA repo, same reason. C2 is the tool for it.
- Notes are terse: tables for comparisons, one line per fact, **Memorise:**
  on anything that has to be known cold. If a note needs a paragraph to
  explain, it is SAA material and belongs in that repo.
- Each project README and the three note sections that need a picture
  (global infrastructure, shared responsibility, policy evaluation) carry a
  Mermaid diagram in the AWS brand palette, nested the way the SAA repo draws
  them: Global Infrastructure outside, Regions inside, services where they
  live. Orange is a service, blue a network or policy layer, green a store or
  observer, navy anything outside AWS. Dotted arrows carry no traffic.
- Every practice score goes in [practice/log.md](practice/log.md), split by
  domain. The target before the exam is two consecutive full-length practice
  exams above 80%.
- Every wrong practice answer becomes a line in
  [practice/weak-spots.md](practice/weak-spots.md) until it has been answered
  correctly twice.

## Related

- [aws-ai-practitioner-projects](https://github.com/rach16/aws-ai-practitioner-projects): AIF-C01, passed September 2026. Covers domain 3.7 here.
- [aws-saa-projects](https://github.com/rach16/aws-saa-projects): SAA-C03, in progress. Covers most of domains 2 and 3 here in far more depth, and its S0 cost sweeper is what confirms C4 was torn down.
