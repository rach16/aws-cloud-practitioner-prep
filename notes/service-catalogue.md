# CLF-C02 service catalogue

Every service on the CLF-C02 exam guide's in-scope list, grouped the way the guide groups them.

**How to use this file:** 15 minutes at the start of every evening, one category at a time, cover the right-hand columns and recite. The last column is the word in a question stem that should make you reach for the service. The exam tests recognition, not depth: know the one-line job and the keyword and you have the question.

Legend: **(verify)** marks a detail checked against memory rather than the current exam guide. Confirm against [the official guide](https://docs.aws.amazon.com/aws-certification/latest/examguides/cloud-practitioner-02.html) before trusting it.

## Analytics

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon Athena | Analytics | SQL queries directly against files in S3, serverless, pay per data scanned | "query data in S3 with SQL", "no infrastructure" |
| AWS Data Exchange | Analytics | Find, subscribe to and use third-party datasets | "third-party data", "subscribe to datasets" |
| Amazon EMR | Analytics | Managed Hadoop and Spark clusters for big data processing | "Hadoop", "Spark", "big data processing" |
| AWS Glue | Analytics | Serverless ETL and the Data Catalog | "ETL", "data catalog", "prepare data for analytics" |
| Amazon Kinesis | Analytics | Ingest and process real-time streaming data | "real-time", "streaming", "clickstream", "IoT telemetry" |
| Amazon Managed Streaming for Apache Kafka (MSK) | Analytics | Managed Kafka clusters | "Kafka" |
| Amazon OpenSearch Service | Analytics | Search, log analytics and visualisation (formerly Elasticsearch) | "search", "log analytics", "Kibana/Dashboards" |
| Amazon QuickSight | Analytics | Serverless BI dashboards, pay per session | "dashboards", "business intelligence", "visualise" |
| Amazon Redshift | Analytics | Petabyte-scale data warehouse, columnar, SQL | "data warehouse", "petabyte", "OLAP", "analytics on structured data" |

## Application Integration

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon EventBridge | Application Integration | Serverless event bus routing events from AWS, SaaS and custom apps to targets | "event-driven", "route events", "SaaS integration", "schedule" |
| Amazon Simple Notification Service (SNS) | Application Integration | Pub/sub push to many subscribers (email, SMS, Lambda, SQS) | "fan-out", "push notification", "publish/subscribe", "one to many" |
| Amazon Simple Queue Service (SQS) | Application Integration | Managed message queue to decouple producers from consumers | "decouple", "queue", "buffer", "loosely coupled", "retry later" |
| AWS Step Functions | Application Integration | Visual workflow orchestration of Lambda and other services as a state machine | "orchestrate", "workflow", "state machine", "coordinate steps" |

## Business Applications

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon Connect | Business Applications | Cloud contact centre | "contact centre", "call centre", "customer service agents" |
| Amazon Simple Email Service (SES) | Business Applications | Send bulk and transactional email | "send email", "marketing email", "transactional email" |

## Cloud Financial Management

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Billing Conductor | Cloud Financial Management | Custom billing views and pro-forma rates for chargeback across accounts | "customise billing for business units", "pro forma", "chargeback" |
| AWS Budgets | Cloud Financial Management | Set cost, usage, RI and Savings Plan thresholds with alerts and optional actions | "alert when spend exceeds", "forecast to exceed", "budget" |
| AWS Cost and Usage Report (CUR) | Cloud Financial Management | Most granular billing data, delivered to S3 hourly or daily | "most detailed billing data", "line item level", "deliver to S3" |
| AWS Cost Explorer | Cloud Financial Management | Visualise and analyse historical and forecast spend, with rightsizing recommendations | "analyse past spend", "forecast", "trend", "which service cost the most" |
| AWS Marketplace | Cloud Financial Management | Catalogue of third-party software and SaaS billed through your AWS bill | "third-party software", "consolidated billing for ISV products", "AMI from a vendor" |
| AWS Pricing Calculator | Cloud Financial Management | Estimate the cost of a planned architecture before building it | "estimate", "before deployment", "planning" |

## Compute

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Batch | Compute | Run batch computing jobs at any scale, provisions compute for you | "batch jobs", "hundreds of thousands of jobs" |
| Amazon EC2 | Compute | Resizable virtual servers you manage | "virtual machine", "full control of OS", "instance" |
| AWS Elastic Beanstalk | Compute | PaaS: upload code, it provisions EC2, ELB, Auto Scaling and monitoring | "deploy web app without managing infrastructure", "still see underlying resources", "PaaS" |
| Amazon EC2 Auto Scaling | Compute | Add and remove EC2 instances to match demand, replace unhealthy ones | "scale out/in automatically", "maintain desired capacity", "self-healing" |
| Amazon Lightsail | Compute | Bundled VPS with fixed monthly price for simple workloads | "simple website", "predictable monthly price", "WordPress", "beginner" |
| AWS Local Zones | Compute | AWS infrastructure in metro areas near end users for single-digit ms latency | "latency-sensitive in a specific city" |
| AWS Outposts | Compute | AWS hardware and services racked in your own data centre | "on-premises", "data residency", "same APIs on-prem" |
| AWS Wavelength | Compute | AWS compute embedded in 5G telecom networks | "5G", "mobile edge", "ultra-low latency to mobile devices" |

## Containers

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon Elastic Container Registry (ECR) | Containers | Store and manage Docker images | "container image registry", "store images" |
| Amazon Elastic Container Service (ECS) | Containers | AWS-native container orchestration | "run containers", "Docker", "AWS-native orchestration" |
| Amazon Elastic Kubernetes Service (EKS) | Containers | Managed Kubernetes control plane | "Kubernetes", "k8s", "portable to other clouds" |
| AWS Fargate | Containers | Serverless compute for ECS and EKS, no instances to manage | "containers without managing servers", "serverless containers" |

## Customer Engagement

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Activate for Startups | Customer Engagement | Credits, support and training for startups | "startup credits" |
| AWS IQ | Customer Engagement | Marketplace for hiring AWS-certified third-party experts for short projects | "hire an AWS expert", "on-demand help" |
| AWS Managed Services (AMS) | Customer Engagement | AWS operates your infrastructure for you | "outsource operations", "AWS runs it" |
| AWS Support | Customer Engagement | Basic, Developer, Business, Enterprise On-Ramp, Enterprise tiers | "TAM", "response time", "support plan" |

## Database

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon Aurora | Database | AWS-built MySQL and PostgreSQL compatible, up to 5x/3x throughput, 6 copies across 3 AZs | "MySQL/PostgreSQL compatible with higher performance", "cloud-native relational" |
| Amazon DynamoDB | Database | Serverless key-value and document NoSQL, single-digit ms at any scale | "NoSQL", "key-value", "single-digit millisecond", "serverless database" |
| Amazon MemoryDB | Database | Redis-compatible, durable, in-memory primary database | "Redis as primary database", "durable in-memory" |
| Amazon Neptune | Database | Managed graph database | "graph", "relationships", "social network", "fraud rings" |
| Amazon RDS | Database | Managed relational DB: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 | "relational", "SQL", "managed patching and backups", "OLTP" |
| Amazon ElastiCache | Database | Managed Redis and Memcached in-memory cache | "cache", "sub-millisecond", "reduce database load", "session store" |
| Amazon DocumentDB | Database | MongoDB-compatible document database | "MongoDB" |
| Amazon Keyspaces | Database | Apache Cassandra-compatible serverless database | "Cassandra" |
| Amazon Quantum Ledger Database (QLDB) | Database | Immutable, cryptographically verifiable transaction log | "immutable ledger", "verifiable history", "no blockchain network needed" |
| Amazon Timestream | Database | Serverless time-series database | "time-series", "IoT sensor data over time" |

## Developer Tools

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS AppConfig | Developer Tools | Deploy application configuration and feature flags safely | "feature flags", "configuration rollout" |
| AWS Cloud9 | Developer Tools | Browser-based IDE | "IDE in a browser" |
| AWS CloudShell | Developer Tools | Browser-based shell with the CLI preconfigured in the console | "shell from the console", "no local CLI install" |
| AWS CodeArtifact | Developer Tools | Managed artifact and package repository | "package repository", "npm/Maven/pip packages" |
| AWS CodeBuild | Developer Tools | Managed build and test service | "compile", "run tests", "build" |
| AWS CodeCommit | Developer Tools | Managed private Git repositories (closed to new customers since July 2024) | "Git repository" |
| AWS CodeDeploy | Developer Tools | Automate deployments to EC2, Lambda, ECS and on-prem | "deploy to instances", "blue/green", "rolling" |
| AWS CodePipeline | Developer Tools | CI/CD pipeline orchestration | "CI/CD", "pipeline", "automate release" |
| AWS CodeStar | Developer Tools | Unified project dashboard for the Code* tools (retired July 2024) | "project dashboard for CI/CD" |
| AWS Command Line Interface (CLI) | Developer Tools | Scriptable terminal access to AWS APIs | "script", "automate from the terminal" |
| AWS X-Ray | Developer Tools | Distributed tracing of requests across services | "trace a request", "find the bottleneck", "latency across microservices" |

## End-User Computing

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon AppStream 2.0 | End-User Computing | Stream desktop applications to a browser | "stream an application", "no install on user devices" |
| Amazon WorkSpaces | End-User Computing | Managed virtual desktops (DaaS) | "virtual desktop", "remote workers", "DaaS" |
| Amazon WorkSpaces Web (now WorkSpaces Secure Browser) | End-User Computing | Secure browser access to internal websites and SaaS | "secure browser", "access internal web apps" |

## Frontend Web and Mobile

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Amplify | Frontend Web and Mobile | Build, host and deploy full-stack web and mobile apps | "full-stack web/mobile app", "frontend hosting with backend" |
| AWS AppSync | Frontend Web and Mobile | Managed GraphQL APIs with real-time and offline sync | "GraphQL", "real-time data sync" |
| AWS Device Farm | Frontend Web and Mobile | Test apps on real physical phones and browsers | "test on real devices" |

## IoT

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS IoT Core | IoT | Connect devices to AWS via MQTT, route messages | "connect devices", "MQTT", "sensors" |
| AWS IoT Greengrass | IoT | Run Lambda and ML at the edge on devices, work offline | "edge compute on devices", "intermittent connectivity" |

## Machine Learning

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon Comprehend | Machine Learning | NLP: sentiment, entities, key phrases, PII in text | "sentiment", "extract entities from text" |
| Amazon Kendra | Machine Learning | ML-powered enterprise search over documents | "natural language search over company documents" |
| Amazon Lex | Machine Learning | Conversational chatbots, voice and text (Alexa engine) | "chatbot", "voice bot" |
| Amazon Polly | Machine Learning | Text to speech | "text to speech", "lifelike voice" |
| Amazon Rekognition | Machine Learning | Image and video analysis: faces, objects, moderation | "image recognition", "detect faces", "content moderation" |
| Amazon SageMaker | Machine Learning | Build, train and deploy ML models end to end | "train a custom model", "data scientists" |
| Amazon Textract | Machine Learning | Extract text, forms and tables from scanned documents | "OCR", "forms", "scanned documents" |
| Amazon Transcribe | Machine Learning | Speech to text | "speech to text", "transcripts of calls" |
| Amazon Translate | Machine Learning | Language translation | "translate" |

## Management and Governance

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Auto Scaling | Management and Governance | Scaling plans across EC2, ECS, DynamoDB, Aurora in one place | "scale multiple resources together" |
| AWS CloudFormation | Management and Governance | Infrastructure as code with JSON/YAML templates, stacks | "template", "IaC", "repeatable deployment", "stack" |
| AWS CloudTrail | Management and Governance | Log of every API call: who, what, when, from where | "who did what", "audit API calls", "governance", "compliance trail" |
| Amazon CloudWatch | Management and Governance | Metrics, logs, alarms, dashboards for resources and apps | "monitor", "metric", "alarm", "CPU utilisation", "logs" |
| AWS Compute Optimizer | Management and Governance | ML recommendations for right-sizing EC2, EBS, Lambda, ECS | "right-size", "over-provisioned instances" |
| AWS Config | Management and Governance | Record resource configuration history, evaluate against rules | "configuration changed", "compliance rules", "drift", "history of a resource" |
| AWS Control Tower | Management and Governance | Set up and govern a multi-account landing zone with guardrails | "landing zone", "set up multi-account environment", "guardrails" |
| AWS Health Dashboard | Management and Governance | Personalised view of AWS events affecting your resources | "events affecting my account", "scheduled maintenance on my instances" |
| AWS Launch Wizard | Management and Governance | Guided sizing and deployment for SAP, SQL Server and similar | "guided deployment of SAP/SQL Server" |
| AWS License Manager | Management and Governance | Track and enforce software licence usage | "BYOL", "track licences" |
| AWS Management Console | Management and Governance | The web UI | "point and click" |
| AWS Organizations | Management and Governance | Multi-account management, consolidated billing, SCPs | "multiple accounts", "consolidated billing", "SCP", "volume discounts across accounts" |
| AWS Resource Groups and Tag Editor | Management and Governance | Group and tag resources in bulk | "tag", "group resources by project" |
| AWS Service Catalog | Management and Governance | Curated portfolio of approved products users can self-serve | "approved products", "self-service provisioning within governance" |
| AWS Systems Manager | Management and Governance | Operate fleets: patching, run commands, Session Manager, Parameter Store | "patch", "run command on many instances", "no SSH", "Parameter Store" |
| AWS Trusted Advisor | Management and Governance | Best-practice checks: cost, performance, security, fault tolerance, service limits | "recommendations", "idle resources", "service limits", "best practice checks" |
| AWS Well-Architected Tool | Management and Governance | Review workloads against the six pillars | "review architecture against best practices", "pillars" |

## Migration and Transfer

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Application Discovery Service | Migration and Transfer | Inventory on-prem servers and dependencies before migrating | "discover what is on-prem", "plan migration" |
| AWS Application Migration Service (MGN) | Migration and Transfer | Lift-and-shift servers to EC2 with continuous replication | "lift and shift", "rehost servers", "replication agent" |
| AWS Database Migration Service (DMS) | Migration and Transfer | Migrate databases with minimal downtime, homogeneous or heterogeneous | "migrate a database", "Oracle to Aurora", "minimal downtime" |
| AWS DataSync | Migration and Transfer | Move large datasets online between on-prem and S3/EFS/FSx | "transfer file data online", "NFS/SMB to S3", "scheduled sync" |
| AWS Migration Hub | Migration and Transfer | Single place to track migration progress across tools | "track migration status" |
| AWS Schema Conversion Tool (SCT) | Migration and Transfer | Convert schemas between database engines | "convert Oracle schema to PostgreSQL" |
| AWS Snow Family | Migration and Transfer | Physical devices for offline transfer: Snowcone, Snowball Edge, Snowmobile | "petabytes offline", "limited bandwidth", "ship a device" |
| AWS Transfer Family | Migration and Transfer | Managed SFTP, FTPS, FTP into S3 and EFS | "SFTP" |

## Networking and Content Delivery

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| Amazon API Gateway | Networking and Content Delivery | Create, publish and secure REST, HTTP and WebSocket APIs | "expose Lambda as an API", "throttle", "API keys" |
| Amazon CloudFront | Networking and Content Delivery | CDN caching content at edge locations worldwide | "cache", "low latency to global users", "static content", "edge" |
| AWS Direct Connect | Networking and Content Delivery | Dedicated private physical link from on-prem to AWS | "dedicated connection", "consistent bandwidth", "not over the internet", "weeks to provision" |
| AWS Global Accelerator | Networking and Content Delivery | Static anycast IPs routing traffic over the AWS backbone to the nearest healthy endpoint | "static IP", "non-HTTP", "gaming/VoIP", "improve TCP/UDP performance" |
| AWS PrivateLink | Networking and Content Delivery | Private connectivity to services without traversing the internet | "privately access a service", "interface endpoint" |
| Amazon Route 53 | Networking and Content Delivery | DNS, domain registration, health-checked routing policies | "DNS", "domain", "routing policy", "failover routing" |
| Amazon VPC | Networking and Content Delivery | Isolated virtual network: subnets, route tables, gateways | "isolated network", "subnet", "internet gateway", "NAT" |
| AWS Site-to-Site VPN | Networking and Content Delivery | Encrypted IPsec tunnel over the internet from on-prem to a VPC | "quick to set up", "encrypted over internet", "VPN" |
| AWS Client VPN | Networking and Content Delivery | Managed OpenVPN endpoint for remote users | "remote employees connect to VPC" |
| AWS Transit Gateway | Networking and Content Delivery | Hub connecting many VPCs and on-prem networks | "hub and spoke", "connect many VPCs" |
| Elastic Load Balancing (ELB) | Networking and Content Delivery | Distribute traffic across targets: ALB (HTTP), NLB (TCP/UDP), GLB (appliances) | "distribute traffic", "layer 7", "layer 4", "health check" |

## Security, Identity and Compliance

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Artifact | Security, Identity and Compliance | Self-service download of AWS compliance reports and agreements | "SOC report", "ISO certification", "compliance documents", "download report" |
| AWS Audit Manager | Security, Identity and Compliance | Continuously collect evidence for audits against frameworks | "collect audit evidence", "assessment against a framework" |
| AWS Certificate Manager (ACM) | Security, Identity and Compliance | Provision and auto-renew TLS certificates | "SSL/TLS certificate", "HTTPS", "free public cert" |
| AWS CloudHSM | Security, Identity and Compliance | Dedicated single-tenant hardware security modules you control | "dedicated hardware", "FIPS 140-2 Level 3", "you manage the keys entirely" |
| Amazon Cognito | Security, Identity and Compliance | Sign-up, sign-in and identity for your app's end users | "customer-facing app login", "social login", "user pools" |
| Amazon Detective | Security, Identity and Compliance | Investigate root cause of security findings with graphs | "investigate", "root cause of a finding" |
| AWS Directory Service | Security, Identity and Compliance | Managed Microsoft Active Directory | "Active Directory", "domain join" |
| AWS Firewall Manager | Security, Identity and Compliance | Centrally manage WAF, Shield and security group rules across accounts | "manage firewall rules across accounts" |
| Amazon GuardDuty | Security, Identity and Compliance | Intelligent threat detection from CloudTrail, VPC Flow Logs, DNS logs | "threat detection", "compromised instance", "unusual API calls", "malicious IP" |
| AWS IAM Identity Center | Security, Identity and Compliance | Single sign-on for the workforce across accounts and apps | "SSO", "employees", "one login for many accounts" |
| AWS Identity and Access Management (IAM) | Security, Identity and Compliance | Users, groups, roles, policies for AWS access | "permissions", "least privilege", "role", "MFA" |
| Amazon Inspector | Security, Identity and Compliance | Automated vulnerability scanning of EC2, ECR images, Lambda | "vulnerabilities", "CVE", "unintended network exposure" |
| AWS Key Management Service (KMS) | Security, Identity and Compliance | Create and control encryption keys, integrated across services | "encrypt at rest", "manage keys", "envelope encryption" |
| Amazon Macie | Security, Identity and Compliance | ML discovery of sensitive data (PII) in S3 | "PII in S3", "sensitive data discovery" |
| AWS Network Firewall | Security, Identity and Compliance | Managed stateful firewall at the VPC level | "VPC-wide firewall", "intrusion prevention" |
| AWS Resource Access Manager (RAM) | Security, Identity and Compliance | Share resources (subnets, Transit Gateways) across accounts | "share a resource with another account" |
| AWS Secrets Manager | Security, Identity and Compliance | Store and automatically rotate secrets and DB credentials | "rotate credentials", "database password" |
| AWS Security Hub | Security, Identity and Compliance | Aggregate findings from GuardDuty, Inspector, Macie and partners, score against standards | "single pane of glass for security", "aggregate findings", "CIS benchmark" |
| AWS Shield | Security, Identity and Compliance | DDoS protection: Standard free and automatic, Advanced paid with DRT access | "DDoS" |
| AWS WAF | Security, Identity and Compliance | Web application firewall: SQL injection, XSS, rate limiting, geo-blocking | "SQL injection", "cross-site scripting", "block by IP/country", "layer 7 rules" |

## Serverless

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Lambda | Serverless | Run code in response to events, billed per request and ms of execution, 15 min max | "no servers", "event-triggered code", "pay only when it runs" |
| AWS Fargate | Serverless | Also listed here: serverless containers | see Containers |
| Amazon DynamoDB, S3, API Gateway, SQS, SNS, EventBridge, Step Functions | Serverless | Also serverless; listed in their own categories | "fully managed, no capacity to provision" |

## Storage

| Service | Category | One-line job | Keyword that points to it |
|---|---|---|---|
| AWS Backup | Storage | Centralised, policy-based backup across EBS, RDS, DynamoDB, EFS and more | "central backup policy", "backup across services" |
| Amazon Elastic Block Store (EBS) | Storage | Block storage volumes for a single EC2 instance in one AZ | "boot volume", "block storage", "database on EC2", "snapshot" |
| Amazon Elastic File System (EFS) | Storage | Shared NFS file system, elastic, multi-AZ, Linux | "shared file system", "many instances mount at once", "NFS" |
| AWS Elastic Disaster Recovery (DRS) | Storage | Continuous replication of on-prem or cloud servers for fast recovery | "disaster recovery for servers", "minutes RTO" |
| Amazon FSx | Storage | Managed third-party file systems: Windows File Server, Lustre, NetApp ONTAP, OpenZFS | "SMB", "Windows file share", "Lustre for HPC" |
| Amazon S3 | Storage | Object storage, 11 nines durability, unlimited scale | "object", "static website", "data lake", "backups", "unlimited" |
| Amazon S3 Glacier | Storage | Archive storage classes: Instant Retrieval, Flexible Retrieval, Deep Archive | "archive", "rarely accessed", "retrieval hours", "lowest cost" |
| AWS Storage Gateway | Storage | Hybrid bridge: on-prem apps use cloud storage via File, Volume, Tape gateways | "hybrid storage", "on-prem access to S3", "virtual tape library" |
| EC2 instance store | Storage | Ephemeral local disk on the host, lost on stop/terminate | "temporary", "highest IOPS", "data lost when instance stops" |
