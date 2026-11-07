# Baseline: every domain, every task statement

The whole CLF-C02 blueprint on one page, paraphrased from the
[official exam guide](https://docs.aws.amazon.com/aws-certification/latest/examguides/cloud-practitioner-02.html),
with a self-rating column. This is not the roadmap; the roadmap is in
[plan/](../plan/). This is the map of everything the exam can ask, so that
the roadmap can be checked against it and nothing is studied twice or not at
all.

**How to use it.** Fill the Baseline column on Fri 6 Nov before reading any
notes, and the Recheck column on Wed 25 Nov after practice exam 2. Scoring:

| Score | Meaning |
|---|---|
| 0 | Could not say what this is |
| 1 | Recognise it, would guess between two answers |
| 2 | Could answer it under exam conditions and say why the other options are wrong |

Add up each domain. Anything still at 0 or 1 on the recheck is the reading
list for Sat 28 Nov. The totals at the bottom give a rough weighted readiness
figure; it is a steer, not a prediction.

## Domain 1: Cloud Concepts (24%)

### 1.1 Define the benefits of the AWS Cloud

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| The six advantages of cloud computing, by name | | | [01 §1.1](01-cloud-concepts.md) |
| Economies of scale and why they lower unit cost | | | [01 §1.1](01-cloud-concepts.md) |
| Global reach and speed of deployment from the global infrastructure | | | [01 §1.1](01-cloud-concepts.md) |
| High availability, elasticity, agility: define and distinguish | | | [01 §1.1](01-cloud-concepts.md), [traps](exam-traps.md) |

### 1.2 Identify design principles of the AWS Cloud

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| The six Well-Architected pillars by name, one line each | | | [01 §1.2](01-cloud-concepts.md) |
| Pick the pillar from a scenario keyword | | | [traps](exam-traps.md) |
| Design principles: scalability, disposable resources, automation, loose coupling | | | [01 §1.2](01-cloud-concepts.md) |
| Managed against unmanaged services and when each is right | | | [01 §1.2](01-cloud-concepts.md) |

### 1.3 Understand the benefits of and strategies for migration

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Cloud Adoption Framework: the six perspectives | | | [01 §1.3](01-cloud-concepts.md) |
| CAF benefits: reduced risk, ESG, revenue, operational efficiency | | | [01 §1.3](01-cloud-concepts.md) |
| The 7 Rs of migration, one line each | | | [01 §1.3](01-cloud-concepts.md), [traps](exam-traps.md) |
| Which tool for which migration: DMS, Snow family, Application Migration Service, DataSync, Transfer Family | | | [01 §1.3](01-cloud-concepts.md) |

### 1.4 Understand concepts of cloud economics

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Fixed against variable cost; CapEx against OpEx | | | [01 §1.4](01-cloud-concepts.md) |
| What on-premises costs that cloud does not: TCO components | | | [01 §1.4](01-cloud-concepts.md) |
| Licensing: BYOL and license-included | | | [01 §1.4](01-cloud-concepts.md) |
| Right-sizing, and what automation saves | | | [01 §1.4](01-cloud-concepts.md) |
| Managed services reduce operational cost: RDS, ECS, EKS, DynamoDB as the examples | | | [01 §1.4](01-cloud-concepts.md) |

**Domain 1 total** (max 34): baseline ___ recheck ___

## Domain 2: Security and Compliance (30%)

### 2.1 Understand the AWS shared responsibility model

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| What is AWS's, what is the customer's, what is shared | | | [02 §2.1](02-security-compliance.md) |
| How the line moves across EC2, RDS, Lambda, S3 | | | [02 §2.1](02-security-compliance.md) |
| "Security of the cloud" against "security in the cloud" | | | [02 §2.1](02-security-compliance.md) |

### 2.2 Understand security, governance and compliance concepts

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| AWS Artifact: what it holds and who uses it | | | [02 §2.2](02-security-compliance.md) |
| Compliance varies by Region and industry; data residency | | | [02 §2.2](02-security-compliance.md) |
| Encryption in transit against at rest, and which services provide each | | | [02 §2.2](02-security-compliance.md) |
| KMS against CloudHSM | | | [02 §2.2](02-security-compliance.md), [traps](exam-traps.md) |
| CloudTrail against Config against CloudWatch: which answers "who", "what changed", "how is it performing" | | | [02 §2.2](02-security-compliance.md), [traps](exam-traps.md) |
| Audit Manager, Security Hub, Trusted Advisor as governance tools | | | [02 §2.2](02-security-compliance.md) |
| Where logs live for governance | | | [02 §2.2](02-security-compliance.md) |

### 2.3 Identify AWS access management capabilities

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Root user: what only it can do, how to protect it | | | [02 §2.3](02-security-compliance.md), [C3](../projects/c3-iam-hygiene) |
| Least privilege as a principle and in a policy | | | [02 §2.3](02-security-compliance.md) |
| Users, groups, roles, policies: when each | | | [02 §2.3](02-security-compliance.md), [traps](exam-traps.md) |
| Managed against inline against customer-managed policies | | | [02 §2.3](02-security-compliance.md) |
| Policy evaluation: default deny, explicit deny wins | | | [02 §2.3](02-security-compliance.md), [C3](../projects/c3-iam-hygiene) |
| MFA types; access keys and password policies | | | [02 §2.3](02-security-compliance.md) |
| Credential storage: Secrets Manager against Parameter Store | | | [02 §2.3](02-security-compliance.md), [traps](exam-traps.md) |
| IAM Identity Center, federation, cross-account roles | | | [02 §2.3](02-security-compliance.md) |
| Cognito: user pools against identity pools | | | [02 §2.3](02-security-compliance.md) |

### 2.4 Identify components and resources for security

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Security groups against NACLs | | | [02 §2.4](02-security-compliance.md), [traps](exam-traps.md) |
| WAF against Shield Standard against Shield Advanced | | | [02 §2.4](02-security-compliance.md) |
| GuardDuty, Inspector, Macie, Security Hub, Detective: which one from the keyword | | | [02 §2.4](02-security-compliance.md), [traps](exam-traps.md) |
| Firewall Manager, Network Firewall, Certificate Manager | | | [02 §2.4](02-security-compliance.md) |
| Third-party security products come from Marketplace | | | [02 §2.4](02-security-compliance.md) |
| Where to find security information: Knowledge Center, Security Center, Security blog | | | [02 §2.4](02-security-compliance.md) |
| Trusted Advisor's security checks | | | [02 §2.4](02-security-compliance.md) |

**Domain 2 total** (max 52): baseline ___ recheck ___

## Domain 3: Cloud Technology and Services (34%)

### 3.1 Define methods of deploying and operating in the AWS Cloud

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Console, CLI, SDKs, APIs, infrastructure as code: when each | | | [03 §3.1](03-technology-services.md) |
| CloudFormation against CDK against Elastic Beanstalk | | | [03 §3.1](03-technology-services.md) |
| Cloud-native, hybrid, on-premises deployment models | | | [03 §3.1](03-technology-services.md) |
| Connectivity: public internet, VPN, Direct Connect | | | [03 §3.1](03-technology-services.md), [traps](exam-traps.md) |

### 3.2 Define the AWS global infrastructure

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Regions, AZs, edge locations and how they relate | | | [03 §3.2](03-technology-services.md), [traps](exam-traps.md) |
| High availability from multiple AZs; AZs share no single point of failure | | | [03 §3.2](03-technology-services.md) |
| When to use multiple Regions: DR, latency, data sovereignty | | | [03 §3.2](03-technology-services.md) |
| Local Zones, Wavelength, Outposts | | | [03 §3.2](03-technology-services.md) |
| Edge services: CloudFront against Global Accelerator | | | [03 §3.2](03-technology-services.md), [traps](exam-traps.md) |

### 3.3 Identify AWS compute services

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| EC2 against containers against serverless: when each | | | [03 §3.3](03-technology-services.md), [traps](exam-traps.md) |
| EC2 instance families: compute, memory, storage, accelerated, general | | | [03 §3.3](03-technology-services.md) |
| ECS against EKS against Fargate against ECR | | | [03 §3.3](03-technology-services.md) |
| Lambda: what it is for and its limits at concept level | | | [03 §3.3](03-technology-services.md) |
| Auto Scaling for elasticity; load balancer types | | | [03 §3.3](03-technology-services.md) |
| Lightsail, Batch, Elastic Beanstalk, Outposts | | | [03 §3.3](03-technology-services.md) |

### 3.4 Identify AWS database services

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Self-managed on EC2 against managed | | | [03 §3.4](03-technology-services.md) |
| RDS against Aurora | | | [03 §3.4](03-technology-services.md) |
| DynamoDB; ElastiCache; Redshift: pick from the keyword | | | [03 §3.4](03-technology-services.md), [traps](exam-traps.md) |
| Multi-AZ against read replica | | | [03 §3.4](03-technology-services.md), [traps](exam-traps.md) |
| DMS and Schema Conversion Tool | | | [03 §3.4](03-technology-services.md) |
| The long tail: DocumentDB, Neptune, Keyspaces, QLDB, Timestream, MemoryDB | | | [03 §3.4](03-technology-services.md) |

### 3.5 Identify AWS network services

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| VPC components: subnets, route tables, internet gateway, NAT | | | [03 §3.5](03-technology-services.md) |
| Security inside a VPC: security groups, NACLs | | | [03 §3.5](03-technology-services.md) |
| Route 53 and its routing policies by name | | | [03 §3.5](03-technology-services.md) |
| VPC peering, Transit Gateway, PrivateLink, endpoints | | | [03 §3.5](03-technology-services.md) |
| CloudFront, API Gateway | | | [03 §3.5](03-technology-services.md) |
| VPN against Direct Connect | | | [03 §3.5](03-technology-services.md), [traps](exam-traps.md) |

### 3.6 Identify AWS storage services

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| S3 and its storage classes, by retrieval time and minimum duration | | | [03 §3.6](03-technology-services.md), [traps](exam-traps.md) |
| S3 features: versioning, lifecycle, replication, Object Lock, Transfer Acceleration | | | [03 §3.6](03-technology-services.md), [C4](../projects/c4-service-tour) |
| EBS against instance store against EFS against S3 | | | [03 §3.6](03-technology-services.md), [traps](exam-traps.md) |
| FSx variants; Storage Gateway types | | | [03 §3.6](03-technology-services.md) |
| AWS Backup; Snow family by size | | | [03 §3.6](03-technology-services.md) |

### 3.7 Identify AWS AI/ML and analytics services

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| SageMaker, Bedrock, Rekognition, Textract, Comprehend, Lex, Polly, Transcribe, Translate, Kendra, Personalize | | | [03 §3.7](03-technology-services.md) |
| Athena, EMR, Glue, Kinesis variants, QuickSight, OpenSearch, MSK, Data Exchange | | | [03 §3.7](03-technology-services.md) |

### 3.8 Identify services from other in-scope categories

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Application integration: SQS against SNS against EventBridge against Step Functions | | | [03 §3.8](03-technology-services.md), [traps](exam-traps.md) |
| Business applications and customer engagement: Connect, SES, Pinpoint, Activate, IQ, Managed Services | | | [03 §3.8](03-technology-services.md) |
| Developer tools: the Code* family, Cloud9, X-Ray | | | [03 §3.8](03-technology-services.md) |
| End-user computing: WorkSpaces, AppStream 2.0, WorkSpaces Web | | | [03 §3.8](03-technology-services.md) |
| Frontend and mobile: Amplify, AppSync, Device Farm | | | [03 §3.8](03-technology-services.md) |
| IoT: IoT Core, Greengrass | | | [03 §3.8](03-technology-services.md) |
| Management and governance: CloudWatch, CloudTrail, Config, Systems Manager, Service Catalog, Control Tower, Organizations, License Manager, Compute Optimizer, Well-Architected Tool | | | [03 §3.8](03-technology-services.md) |

**Domain 3 total** (max 82): baseline ___ recheck ___

## Domain 4: Billing, Pricing and Support (12%)

### 4.1 Compare AWS pricing models

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| On-Demand, Reserved, Spot, Savings Plans, Dedicated Hosts, Dedicated Instances, Capacity Reservations: pick from the scenario | | | [04 §4.1](04-billing-pricing-support.md), [traps](exam-traps.md) |
| Reserved Instance flexibility: Standard against Convertible, terms, payment options | | | [04 §4.1](04-billing-pricing-support.md), [C2](../projects/c2-pricing-api) |
| Reserved Instances and Savings Plans shared across an Organization | | | [04 §4.1](04-billing-pricing-support.md) |
| Spot behaviour and interruption | | | [04 §4.1](04-billing-pricing-support.md) |
| Data transfer charges: in, out, between AZs, between Regions | | | [04 §4.1](04-billing-pricing-support.md), [C2](../projects/c2-pricing-api) |
| Storage pricing dimensions and tiers | | | [04 §4.1](04-billing-pricing-support.md) |
| Free Tier: always free, 12 months, trials, and the credit-based plan for new accounts | | | [04 §4.1](04-billing-pricing-support.md) |

### 4.2 Understand resources for billing, budget and cost management

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| Budgets against Cost Explorer against Cost and Usage Report against Pricing Calculator against Billing Conductor | | | [04 §4.2](04-billing-pricing-support.md), [C1](../projects/c1-cost-controls) |
| Consolidated billing in Organizations: one bill, pooled discounts | | | [04 §4.2](04-billing-pricing-support.md) |
| Cost allocation tags: AWS-generated, user-defined, must be activated | | | [04 §4.2](04-billing-pricing-support.md), [C1](../projects/c1-cost-controls) |
| Where to find pricing information | | | [04 §4.2](04-billing-pricing-support.md) |

### 4.3 Identify AWS technical resources and Support options

| Item | Baseline | Recheck | Notes |
|---|---|---|---|
| The five Support plans: response times, TAM, Trusted Advisor scope, channels | | | [04 §4.3](04-billing-pricing-support.md), [traps](exam-traps.md) |
| Trusted Advisor categories and what Basic gets | | | [04 §4.3](04-billing-pricing-support.md), [C4](../projects/c4-service-tour) |
| AWS Health Dashboard against Service Health Dashboard; Health API | | | [04 §4.3](04-billing-pricing-support.md) |
| Where documentation lives: whitepapers, docs, blogs, Knowledge Center, re:Post, Support Center | | | [04 §4.3](04-billing-pricing-support.md) |
| Partner Network and partner types; Professional Services; Solutions Architects; Managed Services; IQ | | | [04 §4.3](04-billing-pricing-support.md) |

**Domain 4 total** (max 32): baseline ___ recheck ___

## Readiness

Divide each domain total by its maximum, multiply by its weight, add the four.

| | Weight | Baseline | Recheck |
|---|---|---|---|
| Domain 1 | 24% | ___ / 34 | ___ / 34 |
| Domain 2 | 30% | ___ / 52 | ___ / 52 |
| Domain 3 | 34% | ___ / 82 | ___ / 82 |
| Domain 4 | 12% | ___ / 32 | ___ / 32 |
| **Weighted** | | ___ % | ___ % |

A weighted figure above 85% on the recheck, with no item still at 0, is where
the three practice exams should take you. The practice exams are the real
measure; this sheet is what tells you which domain to spend Saturday on.
