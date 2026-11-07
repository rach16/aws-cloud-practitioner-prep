# Domain 1: Cloud Concepts (24%)

Tests whether you can name the business reason for a cloud choice: which advantage, which pillar, which migration strategy, which cost model. Vocabulary, not architecture.

## 1.1 Benefits of the AWS Cloud

**Memorise:** the six advantages of cloud computing, in AWS's own words.

| Advantage | Exam phrasing to recognise |
|---|---|
| Trade fixed expense for variable expense | "pay only for what you consume", no upfront data centre spend |
| Benefit from massive economies of scale | lower per-unit price because AWS aggregates demand |
| Stop guessing capacity | no over- or under-provisioning, scale on demand |
| Increase speed and agility | resources in minutes, faster experimentation |
| Stop spending money running and maintaining data centres | focus on customers, not racking servers |
| Go global in minutes | deploy to multiple Regions with a few clicks |

Distinctions the exam loves:

| Term | Meaning | Not to be confused with |
|---|---|---|
| Elasticity | Capacity grows and shrinks automatically with demand | Scalability |
| Scalability | Capacity can grow (vertical: bigger instance; horizontal: more instances) | Elasticity (scalability does not imply shrinking) |
| Agility | Speed of provisioning and experimenting | Elasticity |
| High availability | Service keeps running when a component fails, measured in uptime; multi-AZ | Fault tolerance |
| Fault tolerance | Zero interruption when a component fails; stricter and costlier than HA | High availability |
| Disaster recovery | Recovering after a Region or site-level event; measured by RTO and RPO | HA (DR is cross-Region, HA is cross-AZ) |
| Reliability | Workload performs its function correctly and consistently | Availability (one input to reliability) |

- **Memorise:** RTO = how long until service is back. RPO = how much data you can afford to lose.
- Global reach = Regions, Availability Zones, edge locations. Multi-AZ = HA. Multi-Region = DR and latency.
- "Pay as you go" is the default; any upfront commitment (RI, Savings Plan) is a discount on top of it.

## 1.2 Design principles

**Memorise:** the six Well-Architected pillars, by name, in order.

| Pillar | One line | The question the exam asks |
|---|---|---|
| Operational Excellence | Run and monitor systems, improve procedures; infrastructure as code, small reversible changes, runbooks | "Which pillar covers automating deployments and learning from failures?" |
| Security | Protect data, systems and assets; identity, traceability, defence in depth, encrypt at rest and in transit | "Which pillar covers least privilege and enabling CloudTrail?" |
| Reliability | Recover from failure, scale to meet demand, test recovery; multi-AZ, auto scaling | "Which pillar covers automatically recovering from an AZ failure?" |
| Performance Efficiency | Use resources efficiently as demand and technology change; serverless, right instance type, experiment | "Which pillar covers choosing the right instance family or going serverless?" |
| Cost Optimization | Avoid unneeded cost; consumption model, measure efficiency, managed services, analyse spend | "Which pillar covers right-sizing and Reserved Instances?" |
| Sustainability | Minimise environmental impact; maximise utilisation, use managed services, reduce downstream impact | "Which pillar covers reducing idle resources to lower carbon footprint?" |

- Well-Architected Tool: free console tool that reviews a workload against the pillars and produces an improvement plan. Not an automated scanner (that is Trusted Advisor).
- General design principles worth recognising: stop guessing capacity, test at production scale, automate to make experimentation easier, allow for evolutionary architectures, drive architectures using data, improve through game days.

**Memorise:** the AWS Cloud Adoption Framework (CAF) six perspectives, split into business and technical.

| Group | Perspective | Owns |
|---|---|---|
| Business | Business | Strategy, value realisation, portfolio |
| Business | People | Culture, organisational change, skills |
| Business | Governance | Benefits management, risk, cloud financial management |
| Technical | Platform | Architecture, infrastructure, CI/CD |
| Technical | Security | Identity, detection, data protection, incident response |
| Technical | Operations | Observability, event management, availability |

- CAF outcomes: reduce business risk, improve ESG performance, grow revenue, increase operational efficiency.
- CAF transformation phases: Envision, Align, Launch, Scale.

## 1.3 Migration

**Memorise:** the 7 Rs of migration.

| R | One line | Typical trigger |
|---|---|---|
| Rehost | Lift and shift, no change; Application Migration Service | Fastest, large legacy estate |
| Replatform | Lift, tinker and shift; minor optimisation such as moving a DB to RDS | Some managed-service benefit, little code change |
| Repurchase | Drop and shop; move to SaaS | Replace CRM or HR system with a vendor product |
| Refactor / Re-architect | Rewrite for cloud-native, microservices, serverless | Need scale or agility the current design cannot give |
| Retire | Decommission; nothing to migrate | Found during discovery, no longer used |
| Retain | Leave on-premises for now | Compliance, recent upgrade, not worth moving yet |
| Relocate | Move VMware vSphere workloads to VMware Cloud on AWS without changing them | Hypervisor-level move, no re-platforming |

Migration services, and which one a question is pointing at:

| Service | Use when the question says |
|---|---|
| Migration Hub | "single place to track progress" of migrations across tools |
| Application Discovery Service | "inventory on-premises servers and dependencies" before migrating |
| Application Migration Service (MGN) | "lift and shift servers" with continuous block-level replication; the rehost tool |
| Database Migration Service (DMS) | "migrate a database with minimal downtime", homogeneous or heterogeneous; pairs with Schema Conversion Tool (SCT) for engine changes |
| Snowcone / Snowball Edge / Snowmobile | "limited bandwidth", "petabytes", "offline transfer"; physical devices |
| DataSync | "online transfer of files" NFS, SMB, HDFS, S3 to AWS over the network, scheduled, with verification |
| Transfer Family | "SFTP / FTPS / FTP endpoint into S3 or EFS" for partners who need a managed file transfer protocol |
| Storage Gateway | "hybrid, keep on-premises access, back to S3"; not strictly migration; it is a Domain 3 storage service |

- Snow family sizes: Snowcone is the smallest (TBs), Snowball Edge is tens of TBs per device, Snowmobile was a truck for exabyte scale. Snowmobile was retired in 2024 and Snowcone is no longer offered (verify), leaving Snowball Edge; all three can still appear in a question.
- **Memorise:** DMS = databases, DataSync = files, Snow = offline, MGN = servers.
- Migration Evaluator (formerly TSO Logic) builds the business case; Migration Acceleration Program (MAP) is the AWS-funded programme.

## 1.4 Cloud economics

| Concept | What the exam wants |
|---|---|
| CapEx vs OpEx | Cloud converts upfront capital expense (buy servers) into operating expense (pay monthly for usage) |
| Fixed vs variable cost | On-premises is mostly fixed regardless of use; cloud is variable with consumption |
| TCO | Total cost of ownership: hardware, software, facilities, power, staff, over the asset lifetime; the comparison on-premises vs cloud |
| Right-sizing | Match instance size to actual utilisation; Compute Optimizer and Cost Explorer recommend it |
| Economies of scale | AWS buys at volume and passes savings on; the reason per-unit prices fall over time |
| Automation | Lower operational cost by removing manual work: IaC, auto scaling, managed patching |
| Managed services | Shift undifferentiated operations (patching, backups, failover) to AWS, reducing staff cost |

Licensing:

| Option | Meaning |
|---|---|
| License included | AWS supplies and bills the license with the instance (Windows, SQL Server, Oracle on RDS) |
| BYOL | Bring your own license; often requires Dedicated Hosts for socket or core-bound licenses |
| License Manager | Tracks license usage and enforces rules across accounts |

- Dedicated Hosts exist mainly for BYOL compliance and socket-bound licensing, not performance.
- Cost reduction levers, in the order the exam expects: turn it off, right-size, use the right pricing model (RI, SP, Spot), use managed or serverless services, move to cheaper storage tiers.
- "Reduce operational overhead" in an answer choice almost always means a managed service.

## Self-test

1. A startup wants to avoid buying servers it may never fully use. Which advantage of cloud computing applies?
2. What is the difference between elasticity and scalability?
3. Which Well-Architected pillar addresses the ability to recover automatically from an AZ failure?
4. A company needs to move 500 TB from a site with a 10 Mbps link. Which service?
5. Which migration strategy moves an application to a SaaS product?
6. Name the three business perspectives of the CAF.
7. A workload will be migrated with no code changes. Which R and which service?
8. What does RPO measure?
9. A company wants to know how much its on-premises data centre really costs over five years compared with AWS. Which concept?
10. Which pillar covers maximising utilisation to reduce environmental impact?

Answers:

1. Trade fixed expense for variable expense (also acceptable: stop guessing capacity).
2. Scalability is the ability to grow capacity; elasticity is automatic growth and shrinkage with demand.
3. Reliability.
4. Snowball Edge (multiple devices) or Snowmobile; a physical Snow device, because the link cannot carry it in time.
5. Repurchase.
6. Business, People, Governance.
7. Rehost, Application Migration Service (MGN).
8. The maximum acceptable data loss, as a window of time before the failure.
9. Total cost of ownership (TCO).
10. Sustainability.
