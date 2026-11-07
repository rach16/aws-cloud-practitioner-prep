# Domain 4: Billing, Pricing and Support (12%)

Tests whether you can pick the right pricing model, the right cost tool and the right Support plan from a one-sentence scenario. Pure memorisation; nothing here is on the SAA path.

## 4.1 Pricing models

**Memorise:** the compute purchasing options and the one phrase that identifies each.

| Model | Commitment | Discount vs On-Demand | Pick it when the question says |
|---|---|---|---|
| On-Demand | None | None | "unpredictable", "short-term", "testing", "cannot be interrupted, no commitment" |
| Reserved Instances | 1 or 3 years, specific instance attributes | Up to about 72% | "steady-state", "predictable", "always on" |
| Savings Plans | 1 or 3 years, a spend amount per hour | Similar to RIs | "flexible across instance families, sizes or Regions" |
| Spot | None; AWS can reclaim | Up to about 90% | "fault-tolerant", "batch", "can be interrupted", "lowest cost" |
| Dedicated Hosts | On-Demand or reserved | Varies | "BYOL", "socket or core licensing", "physical server visibility" |
| Dedicated Instances | On-Demand | Per-instance premium | "hardware not shared with other accounts" but no host-level control |
| Capacity Reservations | None, any length | None (On-Demand rate) | "guarantee capacity in an AZ" without a term commitment |

Reserved Instances:

| Attribute | Standard RI | Convertible RI |
|---|---|---|
| Term | 1 or 3 years | 1 or 3 years |
| Change instance family, OS, tenancy | No | Yes, exchange for equal or greater value |
| Discount | Higher | Lower |
| Sellable on RI Marketplace | Yes | No |

- **Memorise:** RI payment options: All Upfront (biggest discount), Partial Upfront, No Upfront (smallest discount).
- RI scope: Regional (capacity not reserved, applies across AZs) or Zonal (capacity reserved in one AZ).
- RIs also exist for RDS, ElastiCache, Redshift, OpenSearch, DynamoDB (reserved capacity).

Savings Plans:

| Plan | Covers | Flexibility |
|---|---|---|
| Compute Savings Plan | EC2, Fargate, Lambda | Any family, size, OS, tenancy, Region; most flexible, lower discount |
| EC2 Instance Savings Plan | EC2 only | Locked to one instance family in one Region; any size, OS, tenancy; higher discount |
| SageMaker Savings Plan | SageMaker ML instances | Any family, size, Region |

- Savings Plans commit to a dollar-per-hour spend, not to an instance. Usage above the commitment bills On-Demand.
- Spot: 2-minute interruption warning via instance metadata and EventBridge. Spot Fleet is current; Spot blocks were retired in 2022. Never for databases or stateful servers in an exam answer.
- Per-second billing applies to Linux, Windows and other OS-flexible EC2 instances with a 60-second minimum; RHEL and SUSE bill per hour.
- Reserved and Spot pricing concepts apply beyond EC2; the exam may name Fargate and Lambda for Compute Savings Plans.

Data transfer rules:

| Direction | Billed? |
|---|---|
| Internet into AWS | Free |
| AWS out to internet | Billed, tiered by volume |
| Between AZs in a Region | Billed, both directions |
| Between Regions | Billed |
| Same AZ over private IP | Free |
| Same AZ over public or Elastic IP | Billed |
| Out to CloudFront from S3 or an origin | Free |
| S3 to a Gateway endpoint in the same Region | Free |

- **Memorise:** data in is free, data out costs, and cross-AZ is not free.

Storage pricing dimensions (S3 is the model; EBS and EFS share most of them):

| Dimension | Example |
|---|---|
| Capacity stored per GB-month | Standard vs IA vs Glacier tiers |
| Requests | PUT, GET, LIST priced per thousand; higher in IA tiers |
| Retrieval per GB | IA and Glacier classes; Standard has none |
| Minimum storage duration | 30 days IA, 90 days Glacier Flexible, 180 days Deep Archive |
| Data transfer out | As above |
| Early deletion | Charged for the remainder of the minimum duration |

- EBS bills provisioned GB-month whether written or not, plus provisioned IOPS and throughput on io and gp3 above baseline. Snapshots bill on changed blocks.

Free Tier:

| Type | Example | Note |
|---|---|---|
| Always free | Lambda 1M requests per month, DynamoDB 25 GB, CloudWatch 10 metrics | Never expires |
| 12 months free | 750 hours t2 or t3.micro per month, 5 GB S3 Standard, 750 hours RDS micro | From account creation |
| Trials | Short-term trials of specific services such as SageMaker or Inspector | Starts on first use |

- Accounts created after 15 July 2025 are on a credit-based free plan with a spend ceiling and a six-month limit rather than the 12-month tier above (verify current page).
- Free Tier usage alerts come from Budgets and the Billing console.

## 4.2 Billing and cost management

| Tool | What it does | Pick it when the question says |
|---|---|---|
| Billing and Cost Management console | Invoices, payment methods, Free Tier usage, tax | "view the bill" |
| Budgets | Alert at a threshold on cost, usage, RI utilisation or coverage, Savings Plans utilisation or coverage; Budget Actions can apply an IAM or SCP policy or stop EC2 and RDS | "notify when spend exceeds", "automatically stop instances when over budget" |
| Cost Explorer | Visualise 13 months back, forecast 12 months ahead, filter by service, tag, account; RI and Savings Plans recommendations; right-sizing recommendations | "analyse spending trends", "which service costs the most" |
| Cost and Usage Report (CUR) | Most granular billing data, hourly line items, delivered to S3 for Athena or QuickSight | "most detailed", "query billing data with Athena" |
| Cost allocation tags | AWS-generated (prefix aws:) and user-defined (prefix user:); must be activated in Billing before they appear in Cost Explorer and CUR | "break down cost by project or team" |
| Cost Categories | Group costs by rules into named categories | "map accounts and tags to business units" |
| Pricing Calculator | Estimate before building; shareable estimate; no account needed | "estimate the monthly cost of a planned architecture" |
| Billing Conductor | Custom billing rates and views for resellers and chargeback | "show business units a bill with markups or credits" |
| Cost Anomaly Detection | ML-based alert on unexpected spend | "alert on unusual spend without setting a threshold" |
| Compute Optimizer | Right-sizing recommendations for EC2, ASG, EBS, Lambda, ECS Fargate | "recommend a smaller instance based on utilisation" |

**Memorise:** before vs during vs after.

| Question | Pricing Calculator | Cost Explorer | CUR |
|---|---|---|---|
| When | Before building | Ongoing | Ongoing |
| Granularity | Estimate | Daily or monthly, by dimension | Hourly line items |
| Forecast | No | Yes, 12 months | No |
| Needs an account | No | Yes | Yes |
| Where it lives | Public web tool | Console | S3 bucket |

Organizations and consolidated billing:

- One bill for all member accounts; the management account pays.
- Volume discounts pooled: S3 and data transfer tiers are reached on combined usage.
- RI and Savings Plans discounts shared across accounts by default; can be turned off per account.
- Members still see their own usage; the management account sees everything.
- Service control policies (SCPs) are a Domain 2 topic but are set from the same Organizations console.
- Consolidated billing can be used alone; SCPs need all-features mode.

AWS Marketplace:

- Third-party software and SaaS bought through AWS and billed on the AWS invoice.
- Options: hourly, annual, BYOL, SaaS subscription, private offers.
- Marketplace spend counts toward consolidated billing and can be restricted with Private Marketplace.

## 4.3 Support

**Memorise:** the five Support plans as one table. Case response times are the most-tested facts in the domain.

| | Basic | Developer | Business | Enterprise On-Ramp | Enterprise |
|---|---|---|---|---|---|
| Cost | Free | Starts low, percentage of usage | Percentage of usage with a minimum | Percentage of usage with a minimum | Percentage of usage with a minimum |
| Who can open cases | Account and billing only | One primary contact | Unlimited contacts | Unlimited contacts | Unlimited contacts |
| Channels | None for technical | Email, business hours | Phone, chat, email, 24x7 | Phone, chat, email, 24x7 | Phone, chat, email, 24x7 |
| General guidance | n/a | 24 hours | 24 hours | 24 hours | 24 hours |
| System impaired | n/a | 12 hours | 12 hours | 12 hours | 12 hours |
| Production system impaired | n/a | n/a | 4 hours | 4 hours | 4 hours |
| Production system down | n/a | n/a | 1 hour | 1 hour | 1 hour |
| Business-critical system down | n/a | n/a | n/a | 30 minutes | 15 minutes |
| Trusted Advisor | Core checks only | Core checks only | Full set | Full set | Full set |
| TAM | No | No | No | Pool of TAMs | Designated TAM |
| Concierge Support Team | No | No | No | Yes | Yes |
| Infrastructure Event Management | No | No | Available for a fee | Yes | Yes |
| Third-party software guidance | No | No | Yes | Yes | Yes |
| Architectural guidance | No | General | Contextual to your use case | Consultative review | Consultative review and Well-Architected reviews |
| Support API | No | No | Yes | Yes | Yes |

- **Memorise:** 1 hour production down means Business or above. 15 minutes business-critical down means Enterprise. 30 minutes means Enterprise On-Ramp.
- Business is the cheapest plan with 24x7 phone support and full Trusted Advisor.
- Enterprise On-Ramp sits between Business and Enterprise; its TAM is a pool, not a named person.
- Developer plan: only one contact may open cases, and response is email only in business hours.

Trusted Advisor:

| Category | Example check |
|---|---|
| Cost optimization | Idle load balancers, underutilised EC2, unassociated Elastic IPs |
| Performance | Over-utilised instances, CloudFront alternate domain names |
| Security | S3 bucket permissions, security groups with unrestricted ports, root MFA, IAM use |
| Fault tolerance | EBS snapshot age, multi-AZ RDS, ELB cross-zone balancing |
| Service limits | Any quota above 80% usage |
| Operational excellence | Logging and monitoring configuration |

- **Memorise:** Basic and Developer get the core checks only: S3 bucket permissions, security groups unrestricted access, IAM use, MFA on root, EBS public snapshots, RDS public snapshots, plus all service limits checks.
- Trusted Advisor is automated and continuous; Well-Architected Tool is a manual questionnaire.

Health and status:

| Tool | Scope |
|---|---|
| AWS Health Dashboard (account view) | Events affecting your resources, scheduled changes, with EventBridge integration |
| AWS Health Dashboard (service view, formerly Service Health Dashboard) | Public, all-customer status of every service by Region |
| AWS Health API | Programmatic access; Business plan or above |

Other support resources:

| Resource | What it is | Pick it when the question says |
|---|---|---|
| Support Center | Console page for opening and tracking cases | "open a support case" |
| re:Post | Community Q&A, replaced the AWS Forums; free | "ask the community" |
| Knowledge Center | Curated FAQs and how-to articles from AWS Support | "self-service article for a common issue" |
| AWS IQ | Marketplace for hiring certified third-party experts for short engagements | "hire an expert for a few hours" |
| Professional Services | AWS's own consulting organisation for large engagements | "AWS consultants on a migration" |
| Managed Services (AMS) | AWS operates your infrastructure for you | "outsource day-to-day operations of the environment" |
| Solutions Architects | AWS staff who advise on design; part of the account team | "architectural guidance from AWS" |
| Partner Network (APN) | Program for third parties who build on or sell AWS | See partner types below |
| Technical Account Manager (TAM) | Named Enterprise contact for proactive guidance | "proactive, ongoing advocate inside AWS" |
| Prescriptive Guidance, whitepapers, Well-Architected Labs | Documentation | "AWS-published best practice document" |

Partner types:

| Type | Does |
|---|---|
| Consulting Partner | Services: migration, managed services, system integration |
| Technology (software) Partner | Sells software or SaaS that runs on or integrates with AWS, usually via Marketplace |
| Training Partner | Delivers AWS classroom and virtual training |
| Distribution Partner | Resells AWS to end customers in some geographies |

- Partner tiers (Select, Advanced, Premier) and competencies signal validated expertise in a workload or industry.
- Concierge Support Team handles billing and account questions for Enterprise customers; it is not technical support.

## Self-test

1. A workload runs 24x7 for the next three years on the same instance family but the team wants to change sizes freely. Which purchasing option?
2. A batch job can restart from a checkpoint if interrupted. Which pricing model is cheapest?
3. Which Support plan is the cheapest that offers a 1-hour response for a production system down?
4. What is the response time for a business-critical system down on Enterprise?
5. Which tool gives the most granular billing data, and where is it delivered?
6. A company wants an estimate of a planned architecture before creating an account. Which tool?
7. A tag was added to all EC2 instances but does not appear in Cost Explorer. Why?
8. Which Savings Plan covers Lambda and Fargate?
9. Two instances in the same AZ talk over private IPs. Is the traffic billed?
10. Which Trusted Advisor category is fully available on the Basic plan?

Answers:

1. EC2 Instance Savings Plan (or a Regional size-flexible Standard RI for Linux).
2. Spot.
3. Business.
4. 15 minutes.
5. Cost and Usage Report, delivered to an S3 bucket.
6. AWS Pricing Calculator.
7. The tag has not been activated as a cost allocation tag in the Billing console.
8. Compute Savings Plan.
9. No, same-AZ private IP traffic is free.
10. Service limits (plus a core subset of security checks).
