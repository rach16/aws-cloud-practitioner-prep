# CLF-C02 exam traps

The distinctions the exam tests over and over. Each section is one trap. Cover the right column and answer the left.

Rule of thumb for the whole exam: the question stem contains a keyword, and the keyword maps to exactly one service or concept. The wrong answers are the services that are adjacent to it.

## Scalability vs elasticity vs agility

| If the question says | The answer is |
|---|---|
| "handle growth over time", "add capacity as the business grows" | Scalability |
| "match capacity to demand", "scale out at peak and back in afterwards", "stop paying for idle" | Elasticity |
| "experiment quickly", "provision in minutes not weeks", "reduce time to market" | Agility |
| "no up-front investment", "pay only for what you use" | Trade capital expense for variable expense (the six advantages) |
| "benefit from massive economies of scale" | Lower variable cost than you could get yourself |
| "stop guessing capacity" | Elasticity again, phrased as an advantage |
| "deploy to users worldwide in minutes" | Go global in minutes |

## High availability vs fault tolerance vs disaster recovery

| If the question says | The answer is |
|---|---|
| "minimise downtime", "keep running if one AZ fails" | High availability: Multi-AZ, ELB, Auto Scaling |
| "zero interruption even during a failure", "no degradation" | Fault tolerance: redundant components absorb the failure invisibly |
| "recover after a Region-wide event", "RTO and RPO" | Disaster recovery: cross-Region backups, pilot light, warm standby, multi-site |
| "RPO" | How much data you can afford to lose (time since last backup) |
| "RTO" | How long you can afford to be down |
| "cheapest DR, slowest recovery" | Backup and restore |
| "fastest DR, most expensive" | Multi-site active/active |

## Region vs Availability Zone vs edge location

| If the question says | The answer is |
|---|---|
| "geographic area with multiple isolated locations" | Region |
| "one or more discrete data centres with redundant power and networking" | Availability Zone |
| "cache content close to users", "CloudFront", "Route 53" | Edge location |
| "data residency", "data must stay in a country" | Choose the Region |
| "low latency to a specific metro" | Local Zone |
| "5G mobile edge" | Wavelength Zone |
| "AWS hardware in my data centre" | Outposts |
| "minimum AZs per Region" | 3 |

## Security group vs network ACL

| If the question says | The answer is |
|---|---|
| "instance level", "stateful", "allow rules only" | Security group |
| "subnet level", "stateless", "allow and deny rules", "rules evaluated in number order" | Network ACL |
| "block a specific IP address" | NACL (security groups cannot deny) |
| "return traffic automatically allowed" | Security group (stateful) |
| "default allows all inbound and outbound" | Default NACL |
| "default denies all inbound, allows all outbound" | Default security group |

## IAM user vs role vs group vs policy

| If the question says | The answer is |
|---|---|
| "a person or application with long-term credentials" | IAM user |
| "temporary credentials", "assumed by a service or another account", "EC2 needs to call S3" | IAM role |
| "apply the same permissions to many users" | IAM group (groups cannot be nested) |
| "JSON document that defines allow/deny" | IAM policy |
| "AWS-maintained policy" | AWS managed policy |
| "sets the maximum permissions an identity can have" | Permissions boundary |
| "attached to a resource rather than an identity", "S3 bucket policy" | Resource-based policy |
| "an explicit deny anywhere" | Wins over any allow |
| "least privilege" | Grant only what the task needs |
| "an application on EC2 needs AWS credentials" | Attach a role to the instance, never embed keys |
| "centralised identity for employees across accounts" | IAM Identity Center |

## Root user only actions

| If the question says | The answer is |
|---|---|
| "change account settings, name, email, root password" | Root user only |
| "close the account" | Root user only |
| "change the support plan" | Root user only |
| "restore IAM user permissions after a lockout" | Root user only |
| "sign up for GovCloud" | Root user only |
| "register as a seller in Reserved Instance Marketplace" | Root user only |
| "enable MFA delete on an S3 bucket" | Root user only |
| "what to do with the root user" | Enable MFA, lock away credentials, delete root access keys, never use for daily work |

## CloudTrail vs CloudWatch vs Config

| If the question says | The answer is |
|---|---|
| "who made this API call", "who deleted the bucket", "audit", "governance" | CloudTrail |
| "CPU utilisation", "metric", "alarm", "log group", "dashboard" | CloudWatch |
| "what did the configuration look like last week", "is this resource compliant with a rule", "drift" | Config |
| "alert when a threshold is crossed" | CloudWatch alarm |
| "record of API activity delivered to S3" | CloudTrail trail |
| "enabled by default for 90 days" | CloudTrail event history |
| "see events across all accounts in an Organization" | CloudTrail organisation trail |

## Trusted Advisor vs Inspector vs GuardDuty vs Macie vs Security Hub

| If the question says | The answer is |
|---|---|
| "best practice recommendations", "cost, performance, security, fault tolerance, service limits" | Trusted Advisor |
| "vulnerabilities", "CVEs", "software on EC2 or in container images" | Inspector |
| "threat detection", "unusual API calls", "compromised credentials", "crypto mining" | GuardDuty |
| "find PII in S3", "sensitive data discovery" | Macie |
| "aggregate findings in one place", "security score against standards" | Security Hub |
| "investigate the root cause of a GuardDuty finding" | Detective |
| "all Trusted Advisor checks" | Business, Enterprise On-Ramp or Enterprise support |
| "only core security and service limit checks" | Basic and Developer support |

## KMS vs CloudHSM

| If the question says | The answer is |
|---|---|
| "managed keys", "integrates with S3, EBS, RDS", "multi-tenant" | KMS |
| "dedicated hardware", "single-tenant", "FIPS 140-2 Level 3", "you control everything" | CloudHSM |
| "AWS manages the key entirely" | AWS managed key / AWS owned key |
| "you create and manage the key, AWS stores it" | Customer managed key in KMS |
| "key rotation automatically" | KMS |

## Secrets Manager vs Parameter Store

| If the question says | The answer is |
|---|---|
| "automatic rotation of database credentials" | Secrets Manager |
| "store configuration values and strings, hierarchically" | Systems Manager Parameter Store |
| "free tier for plain config" | Parameter Store standard parameters |
| "generate a random password" | Secrets Manager |

## S3 storage classes by retrieval need

| If the question says | The answer is |
|---|---|
| "frequently accessed", "default" | S3 Standard |
| "unknown or changing access pattern", "automatically move between tiers" | S3 Intelligent-Tiering |
| "infrequent access, millisecond retrieval, multi-AZ" | S3 Standard-IA |
| "infrequent, recreatable, single AZ is fine" | S3 One Zone-IA |
| "archive, millisecond retrieval, accessed quarterly" | S3 Glacier Instant Retrieval |
| "archive, minutes to hours retrieval" | S3 Glacier Flexible Retrieval |
| "lowest cost, retrieval within 12 hours, accessed once a year" | S3 Glacier Deep Archive |
| "move objects between classes automatically on a schedule" | S3 Lifecycle policy |
| "11 nines" | Durability of every S3 class |
| "keep every version of an object", "protect from overwrite" | S3 Versioning |
| "replicate to another Region" | S3 Cross-Region Replication |
| "retention lock, WORM" | S3 Object Lock |
| "upload large files faster from far away" | S3 Transfer Acceleration |

## EBS vs EFS vs S3 vs instance store

| If the question says | The answer is |
|---|---|
| "block storage for one instance", "boot volume", "database disk" | EBS |
| "shared file system across many instances", "NFS", "Linux" | EFS |
| "Windows file share", "SMB" | FSx for Windows File Server |
| "object storage", "unlimited", "static website", "data lake" | S3 |
| "temporary high-speed scratch disk", "lost on stop" | Instance store |
| "EBS persists after" | Instance stop (not after termination unless configured) |
| "EBS volume availability" | One AZ, snapshot to S3 to move |
| "EFS availability" | Multiple AZs in a Region |

## RDS vs DynamoDB vs Redshift vs ElastiCache

| If the question says | The answer is |
|---|---|
| "relational", "SQL joins", "transactions", "OLTP" | RDS or Aurora |
| "key-value", "NoSQL", "single-digit ms", "serverless", "massive scale" | DynamoDB |
| "data warehouse", "OLAP", "petabytes", "complex analytics queries" | Redshift |
| "in-memory", "sub-millisecond", "cache results", "session state" | ElastiCache |
| "MySQL compatible with 5x throughput" | Aurora |
| "MongoDB" | DocumentDB |
| "graph" | Neptune |
| "time-series" | Timestream |
| "immutable ledger" | QLDB |
| "run your own database engine with full OS control" | Database on EC2 |

## Multi-AZ vs read replica

| If the question says | The answer is |
|---|---|
| "high availability", "automatic failover", "synchronous" | Multi-AZ |
| "scale read traffic", "offload reporting queries", "asynchronous" | Read replica |
| "can a read replica be in another Region" | Yes |
| "does Multi-AZ serve reads from the standby" | No (RDS Multi-AZ standby is not readable) |
| "both" | Use both: Multi-AZ for HA plus read replicas for reads |

## SQS vs SNS vs EventBridge

| If the question says | The answer is |
|---|---|
| "queue", "decouple", "consumer polls", "process later", "buffer" | SQS |
| "push", "fan-out", "email/SMS/Lambda subscribers", "topic" | SNS |
| "route events by rule", "SaaS events", "schedule", "event bus" | EventBridge |
| "one message to many subscribers" | SNS |
| "one message to one consumer, at least once" | SQS standard |
| "exactly once, in order" | SQS FIFO |
| "orchestrate a multi-step workflow with retries" | Step Functions |

## ECS vs EKS vs Fargate vs Lambda

| If the question says | The answer is |
|---|---|
| "containers, AWS-native" | ECS |
| "Kubernetes", "portable across clouds" | EKS |
| "containers without managing EC2 instances" | Fargate (launch type for ECS or EKS) |
| "run code without any servers, event-driven, short-lived" | Lambda |
| "Lambda maximum execution time" | 15 minutes |
| "Lambda pricing" | Requests plus duration in ms times memory |
| "want full control of the underlying hosts" | ECS or EKS on EC2 launch type |
| "store container images" | ECR |

## Reserved vs Savings Plans vs Spot vs On-Demand vs Dedicated

| If the question says | The answer is |
|---|---|
| "steady-state, predictable, 1 or 3 year commitment, specific instance type" | Reserved Instances |
| "commit to spend per hour, flexible across instance family, size, Region, even Fargate and Lambda" | Compute Savings Plan |
| "commit to spend, flexible within one instance family in one Region" | EC2 Instance Savings Plan |
| "interruptible", "fault-tolerant batch", "up to 90% off", "can be reclaimed with 2 minutes notice" | Spot Instances |
| "unpredictable, short-term, no commitment" | On-Demand |
| "physical server dedicated to you, BYOL per-socket licences, compliance" | Dedicated Hosts |
| "instance on hardware not shared with other customers, no host visibility" | Dedicated Instances |
| "reserve capacity in an AZ without a billing commitment" | On-Demand Capacity Reservations |
| "largest discount" | All Upfront, 3 year |
| "sell unused reservations" | Reserved Instance Marketplace |
| "RIs apply across accounts" | Yes, in an Organization with consolidated billing (sharing on by default) |

## Budgets vs Cost Explorer vs Pricing Calculator vs CUR vs Billing Conductor

| If the question says | The answer is |
|---|---|
| "alert me when spend or forecast exceeds a threshold" | AWS Budgets |
| "analyse past spend, see trends, forecast, filter by tag" | Cost Explorer |
| "estimate what a planned architecture will cost before building" | Pricing Calculator |
| "most granular line-item data, deliver to S3, query with Athena" | Cost and Usage Report |
| "custom billing rates for business units, chargeback" | Billing Conductor |
| "group costs by project or team" | Cost allocation tags (activate them first) |
| "cost categories across accounts" | Cost Categories |
| "see RI and Savings Plan utilisation and coverage" | Cost Explorer or Budgets (RI/SP budgets) |
| "detect unusual spend automatically" | Cost Anomaly Detection |
| "one bill for many accounts" | Organizations consolidated billing |
| "volume discount tiers shared across accounts" | Consolidated billing aggregates usage |
| "free for 12 months after sign-up" | Free Tier, 12-month type |
| "always free within a limit", "1M Lambda requests a month" | Free Tier, always-free type |
| "free for a short period after enabling the service" | Free Tier, trials |

## Support plan by response time and feature

| If the question says | The answer is |
|---|---|
| "free, customer service and documentation only, no technical support" | Basic |
| "business hours email access to Cloud Support Associates, one primary contact" | Developer |
| "24/7 phone and chat, production system down in 1 hour, full Trusted Advisor, unlimited contacts, third-party software support" | Business |
| "business-critical system down in 15 minutes, pool of TAMs" | Enterprise |
| "business-critical system down in 30 minutes, pool of TAMs, lower cost than Enterprise" | Enterprise On-Ramp |
| "designated Technical Account Manager", "concierge support team", "Infrastructure Event Management included" | Enterprise |
| "general guidance response time" | Developer 24 hours, Business and above 24 hours |
| "system impaired response time" | Developer 12 hours, Business 12 hours, Enterprise On-Ramp 12 hours, Enterprise 12 hours |
| "production system impaired" | Business 4 hours, Enterprise On-Ramp 4 hours, Enterprise 4 hours |
| "production system down" | Business 1 hour, Enterprise On-Ramp 1 hour, Enterprise 1 hour |
| "business-critical system down" | Enterprise On-Ramp 30 minutes, Enterprise 15 minutes |
| "architectural guidance: general, contextual, consultative review" | Developer, Business, Enterprise respectively |
| "who can change the support plan" | Root user |
| "AWS Support API access" | Business and above |

## Shield vs WAF

| If the question says | The answer is |
|---|---|
| "DDoS", "volumetric attack", "layer 3/4" | Shield |
| "free and automatic on every account" | Shield Standard |
| "DDoS cost protection, 24/7 DDoS Response Team, advanced reporting" | Shield Advanced |
| "SQL injection", "cross-site scripting", "block countries", "rate-based rule", "layer 7" | WAF |
| "where WAF attaches" | CloudFront, ALB, API Gateway, AppSync, Cognito |
| "manage WAF rules across many accounts" | Firewall Manager |
| "firewall for a whole VPC with IPS" | Network Firewall |

## Direct Connect vs VPN

| If the question says | The answer is |
|---|---|
| "dedicated private physical connection", "consistent throughput", "bypass the internet", "takes weeks to provision" | Direct Connect |
| "quick to set up", "encrypted over the public internet", "cheaper", "hours not weeks" | Site-to-Site VPN |
| "Direct Connect encrypted by default" | No, pair it with a VPN or MACsec if encryption is required |
| "remote individual users to the VPC" | Client VPN |
| "connect many VPCs and on-prem in a hub" | Transit Gateway |
| "connect two VPCs directly" | VPC Peering (not transitive) |

## CloudFront vs Global Accelerator

| If the question says | The answer is |
|---|---|
| "cache static and dynamic content at the edge", "HTTP/HTTPS" | CloudFront |
| "static anycast IP addresses", "TCP or UDP", "gaming, VoIP, IoT", "route to nearest healthy regional endpoint, no caching" | Global Accelerator |
| "both use" | The AWS edge network and backbone |
| "restrict content to certain countries" | CloudFront geo restriction |
| "serve private content" | CloudFront signed URLs or cookies |

## Snow family by size

| If the question says | The answer is |
|---|---|
| "up to about 8 TB, rugged, tiny, edge compute, fits in a backpack" | Snowcone, 8 TB HDD or 14 TB SSD, no longer offered (verify) |
| "tens of TB to about 80 TB per device, edge compute and storage optimised variants" | Snowball Edge |
| "exabyte scale, shipping container on a truck" | Snowmobile (retired 2024) |
| "limited or no network bandwidth", "would take months online" | Snow family |
| "run EC2 and Lambda disconnected in the field" | Snowball Edge Compute Optimized or Snowcone |
| "rule of thumb" | Over about a week of transfer time online, consider Snow |

## DMS vs DataSync vs Transfer Family vs Application Migration Service

| If the question says | The answer is |
|---|---|
| "migrate a database", "source stays live during migration", "Oracle to PostgreSQL" | DMS (with SCT for heterogeneous engines) |
| "move file data online from NFS/SMB to S3/EFS/FSx", "scheduled, incremental" | DataSync |
| "SFTP, FTPS, FTP endpoint backed by S3 or EFS" | Transfer Family |
| "lift and shift whole servers to EC2 with block-level replication" | Application Migration Service (MGN) |
| "inventory on-prem servers and their dependencies first" | Application Discovery Service |
| "track all migrations in one dashboard" | Migration Hub |
| "move on-prem VMs as AMIs" (legacy) | VM Import/Export |

## Well-Architected pillar by its keyword

| If the question says | The answer is |
|---|---|
| "run and monitor systems, improve processes, infrastructure as code, small reversible changes" | Operational Excellence |
| "protect data, least privilege, traceability, encryption, prepare for security events" | Security |
| "recover from failure, test recovery, scale horizontally, stop guessing capacity" | Reliability |
| "use resources efficiently, serverless, experiment, go global, mechanical sympathy" | Performance Efficiency |
| "avoid unnecessary cost, measure efficiency, consumption model, managed services" | Cost Optimization |
| "reduce energy and carbon, maximise utilisation, managed services, region choice" | Sustainability |
| "how many pillars" | 6 |
| "the tool" | AWS Well-Architected Tool, free, in the console |
| "cloud adoption framework perspectives" | Business, People, Governance, Platform, Security, Operations |

## The 7 Rs of migration

| If the question says | The answer is |
|---|---|
| "lift and shift, no changes" | Rehost |
| "lift, tinker and shift, minor cloud optimisation (e.g. to RDS)" | Replatform |
| "move to a SaaS product, drop and shop" | Repurchase |
| "re-architect for cloud-native, microservices, serverless" | Refactor (re-architect) |
| "keep as is for now" | Retain |
| "decommission" | Retire |
| "move to a different location, e.g. VMware Cloud on AWS, without buying new hardware" | Relocate |

## Organizations vs Control Tower vs Service Catalog

| If the question says | The answer is |
|---|---|
| "manage many accounts, consolidated billing, SCPs, OUs" | Organizations |
| "set up a new multi-account environment with guardrails and best practices quickly", "landing zone" | Control Tower (built on Organizations) |
| "let users self-serve from a list of approved, pre-configured products" | Service Catalog |
| "SCP effect" | Sets the maximum permissions for accounts in an OU; does not grant anything |
| "SCP and the management account" | SCPs do not affect the management account |
| "share subnets or Transit Gateway across accounts" | Resource Access Manager |

## CapEx vs OpEx

| If the question says | The answer is |
|---|---|
| "buy servers up front, depreciate over years, data centre lease" | Capital expenditure (on-prem) |
| "pay as you go, monthly bill, scales with use" | Operational expenditure (cloud) |
| "total cost of ownership" | TCO: include hardware, power, cooling, space, staff, licences, not just the server |
| "what the Migration Evaluator does" | Builds a TCO business case from your on-prem data |
| "hidden on-prem costs" | Power, cooling, real estate, hardware refresh, staff |

## Identity Center vs Cognito vs IAM

| If the question says | The answer is |
|---|---|
| "employees sign in once to many AWS accounts and SaaS apps" | IAM Identity Center |
| "customers sign up and sign in to my web or mobile app", "social login" | Cognito |
| "permissions for AWS resources within an account" | IAM |
| "federate with an existing corporate directory" | IAM Identity Center or IAM identity provider with SAML |
| "Cognito user pool vs identity pool" | User pool authenticates users; identity pool gives them temporary AWS credentials |

## Artifact vs Audit Manager

| If the question says | The answer is |
|---|---|
| "download the SOC 2 report", "ISO 27001 certificate", "PCI attestation" | Artifact |
| "continuously collect evidence of my own compliance", "prepare for an audit" | Audit Manager |
| "accept an agreement like a BAA for HIPAA" | Artifact Agreements |

## Health Dashboard vs Service Health Dashboard

| If the question says | The answer is |
|---|---|
| "events affecting my resources", "my instance is scheduled for retirement", "personalised" | AWS Health Dashboard (Personal Health Dashboard) |
| "public status of all AWS services in all Regions" | AWS Service Health Dashboard (health.aws.amazon.com) |
| "programmatic access to health events" | AWS Health API (Business support and above) |

## Compute Optimizer vs Trusted Advisor vs Cost Explorer rightsizing

| If the question says | The answer is |
|---|---|
| "ML-based recommendations for EC2, EBS, Lambda, ECS Fargate sizing using CloudWatch metrics" | Compute Optimizer |
| "broad checks including idle load balancers, underutilised instances, unassociated EIPs" | Trusted Advisor |
| "rightsizing recommendations alongside spend analysis, RI purchase recommendations" | Cost Explorer |
| "all three are" | Free (Trusted Advisor full checks need Business support) |

## Shared responsibility model

| If the question says | The answer is |
|---|---|
| "security of the cloud" | AWS: hardware, facilities, hypervisor, managed service software, global infrastructure |
| "security in the cloud" | Customer: data, IAM, OS patching on EC2, network config, encryption, application |
| "patching the OS of an EC2 instance" | Customer |
| "patching the OS under RDS or Lambda" | AWS |
| "physical security of data centres" | AWS |
| "encrypting data at rest in S3" | Customer decides, AWS provides the tools |
| "configuring security groups" | Customer |
| "shared controls" | Patch management, configuration management, awareness and training |
| "who is responsible for compliance" | Both: AWS for infrastructure certifications, customer for how they use it |

## Words that give the answer away

| Keyword in the question | Points to |
|---|---|
| "petabyte-scale data warehouse" | Redshift |
| "sub-millisecond" | ElastiCache or DynamoDB DAX |
| "single-digit millisecond" | DynamoDB |
| "no servers to manage" | Lambda, Fargate, or any serverless service |
| "compliance reports", "SOC", "ISO" | Artifact |
| "interruptible workload" | Spot Instances |
| "steady-state workload" | Reserved Instances or Savings Plans |
| "unpredictable workload" | On-Demand |
| "decouple" | SQS |
| "fan-out" | SNS |
| "who made this API call" | CloudTrail |
| "CPU utilisation" | CloudWatch |
| "configuration history" | Config |
| "PII in S3" | Macie |
| "threat detection" | GuardDuty |
| "vulnerability scan" | Inspector |
| "DDoS" | Shield |
| "SQL injection" | WAF |
| "dedicated hardware security module" | CloudHSM |
| "rotate database credentials" | Secrets Manager |
| "temporary credentials" | IAM role, STS |
| "employees sign in once" | IAM Identity Center |
| "customer-facing login" | Cognito |
| "content delivery", "cache at the edge" | CloudFront |
| "static IP for global app, TCP/UDP" | Global Accelerator |
| "DNS", "domain registration" | Route 53 |
| "private connection, not the internet, weeks to set up" | Direct Connect |
| "encrypted tunnel over the internet" | Site-to-Site VPN |
| "shared file system, NFS" | EFS |
| "Windows file share, SMB" | FSx for Windows |
| "boot volume", "block" | EBS |
| "object storage", "static website hosting" | S3 |
| "archive, hours to retrieve, cheapest" | S3 Glacier Deep Archive |
| "unknown access pattern" | S3 Intelligent-Tiering |
| "SQL queries directly on S3 files" | Athena |
| "ETL", "data catalog" | Glue |
| "real-time streaming" | Kinesis |
| "Hadoop", "Spark" | EMR |
| "BI dashboards" | QuickSight |
| "Kubernetes" | EKS |
| "Docker, AWS-native" | ECS |
| "container registry" | ECR |
| "infrastructure as code", "template" | CloudFormation |
| "upload code and AWS handles the rest, PaaS" | Elastic Beanstalk |
| "fixed monthly price, simple VPS" | Lightsail |
| "AWS infrastructure on-premises" | Outposts |
| "petabytes offline, limited bandwidth" | Snowball Edge |
| "migrate a database with minimal downtime" | DMS |
| "lift and shift servers" | Application Migration Service |
| "online file transfer to S3" | DataSync |
| "SFTP" | Transfer Family |
| "estimate before building" | Pricing Calculator |
| "alert when forecast exceeds" | Budgets |
| "analyse last month's spend" | Cost Explorer |
| "most granular billing data" | Cost and Usage Report |
| "one bill, many accounts" | Organizations consolidated billing |
| "restrict what accounts in an OU can do" | Service control policy |
| "landing zone" | Control Tower |
| "approved product portfolio for self-service" | Service Catalog |
| "best practice checks, service limits" | Trusted Advisor |
| "right-size using ML" | Compute Optimizer |
| "scheduled maintenance affecting my instances" | AWS Health Dashboard |
| "Technical Account Manager" | Enterprise support |
| "production down within 1 hour" | Business support |
| "business-critical down within 15 minutes" | Enterprise support |
| "run commands on a fleet without SSH" | Systems Manager |
| "patch many instances" | Systems Manager Patch Manager |
| "text to speech" | Polly |
| "speech to text" | Transcribe |
| "chatbot" | Lex |
| "extract text from scanned forms" | Textract |
| "image and video analysis" | Rekognition |
| "sentiment" | Comprehend |
| "train and deploy custom ML models" | SageMaker |
| "virtual desktops" | WorkSpaces |
| "connect IoT devices, MQTT" | IoT Core |
| "GraphQL" | AppSync |
| "trace a request across microservices" | X-Ray |
| "CI/CD pipeline" | CodePipeline |
| "six pillars" | Well-Architected Framework |
| "security of the cloud" | AWS's responsibility |
| "security in the cloud" | Customer's responsibility |
| "trade capital expense for variable expense" | One of the six advantages of cloud computing |
