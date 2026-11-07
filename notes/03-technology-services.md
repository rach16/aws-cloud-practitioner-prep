# Domain 3: Cloud Technology and Services (34%)

What it tests: service recognition. A one-line scenario, four service names, pick the one whose job that is. Optimise for the keyword that maps to the service, not for depth.

## 3.1 Deploying and operating

| Access method | Use when | Keyword |
|---|---|---|
| Management Console | Exploring, one-off tasks | "web interface" |
| CLI | Scripting, repeatable commands | "shell script", "automate from a terminal" |
| SDKs | Calling AWS from application code (Python boto3, Java, JS, .NET, Go) | "from my application" |
| Infrastructure as Code | Repeatable, version-controlled environments | "same environment in three Regions", "template" |

| Provisioning tool | Model | Keyword |
|---|---|---|
| **CloudFormation** | Declarative JSON/YAML templates, stacks, change sets, drift detection | "template", "stack", "repeatable infrastructure" |
| **CDK** | Write infrastructure in TypeScript/Python/Java, synthesises to CloudFormation | "programming language", "familiar language" |
| **Elastic Beanstalk** | PaaS: upload code, it provisions EC2, ELB, ASG, RDS. You still see and pay for the resources. | "just deploy my web app", "developer does not want to manage infrastructure", free service, pay for resources |
| **OpsWorks** | Managed Chef and Puppet (deprecated, may still appear) | "Chef", "Puppet" |
| **App Runner** | Container or source to running web service, fully managed | "containerised web app, no infrastructure" |

- Systems Manager (SSM): fleet management. Capabilities to recognise: **Session Manager** (shell without SSH or open ports), **Run Command**, **Patch Manager**, **State Manager**, **Parameter Store**, **Inventory**, **Automation**, **OpsCenter**. Works on EC2 and on-premises via the SSM Agent.
- **Memorise:** "connect to an instance without opening port 22" = Session Manager.

| Deployment model | Means |
|---|---|
| Cloud | Everything on AWS |
| Hybrid | On-premises connected to AWS: Direct Connect, VPN, Outposts, Storage Gateway, Snow, ECS/EKS Anywhere |
| On-premises / private cloud | Own data centre, possibly VMware Cloud on AWS as the bridge |

| Connectivity | Path | Keyword |
|---|---|---|
| Public internet | HTTPS to public endpoints | Default |
| Site-to-Site VPN | Encrypted IPsec over the internet, minutes to set up | "quick", "encrypted", "cheap" |
| Direct Connect | Dedicated private fibre, weeks to provision, 1 to 100 Gbps | "consistent latency", "large data volumes", "private, not over the internet" |
| Client VPN | Individual users into the VPC | "remote workers" |

## 3.2 Global infrastructure

| Construct | Is | Count / fact | Keyword |
|---|---|---|---|
| **Region** | Geographic area, isolated, 3+ AZs in every new Region | 30+ | "data residency", "compliance" |
| **Availability Zone** | One or more discrete data centres with separate power, cooling, networking, connected by low-latency links | Within a Region, ms apart, separated to limit blast radius | "high availability", "fault isolation" |
| **Edge location** | CloudFront and Route 53 points of presence | 600+ | "cache content close to users", "low latency" |
| **Regional edge cache** | Larger cache between edge locations and origin | | |
| **Local Zone** | AWS compute/storage in a metro area far from the parent Region | | "single-digit ms latency in a city", "gaming", "media" |
| **Wavelength** | AWS compute inside a 5G telecom provider's network | | "5G", "mobile edge" |
| **Outposts** | AWS hardware racks in your data centre, same APIs | | "on-premises", "data must stay in the building", "hybrid" |

- Choosing a Region, in order: compliance and data sovereignty, latency to users, service availability (not all services in all Regions), pricing (differs by Region).
- High availability = deploy across **multiple AZs**. Disaster recovery = across **multiple Regions**.
- Global services (not Regional): IAM, Route 53, CloudFront, WAF (on CloudFront), Organizations, Artifact. S3 bucket names are global but buckets are Regional.

| Edge service | Does | Keyword |
|---|---|---|
| **CloudFront** | CDN, caches HTTP(S) content at edge locations, integrates with S3, ALB, any origin, Shield, WAF | "static content", "video", "cache", "reduce latency to global users" |
| **Global Accelerator** | Two static anycast IPs, routes TCP/UDP over the AWS backbone to the nearest healthy endpoint | "static IP", "non-HTTP", "gaming", "fast regional failover" |
| **Route 53** | DNS, health checks, domain registration, routing policies | "domain", "DNS", "failover routing" |

## 3.3 Compute

| EC2 family | Letter | Purpose |
|---|---|---|
| General purpose | T (burstable), M | Balanced, web servers, dev |
| Compute optimised | C | Batch, HPC, gaming servers, encoding |
| Memory optimised | R, X, z | In-memory DBs, big caches, SAP |
| Storage optimised | I, D, H | High sequential IO, NoSQL, data warehousing |
| Accelerated | P, G, Inf, Trn, F | GPU, ML training/inference, FPGA |
| HPC | Hpc | Tightly coupled HPC |

- Instance naming: `m5.large` = family m, generation 5, size large. Graviton (ARM) = `g` suffix, e.g. `m7g`.
- AMI = template for the root volume plus launch permissions. Regional; copy to use elsewhere.
- User data = script run on first boot. Instance metadata at `169.254.169.254`.

| EC2 purchasing option | Fit | Keyword |
|---|---|---|
| On-Demand | Short, unpredictable, no commitment | "testing", "cannot be interrupted, no commitment" |
| Reserved Instances | 1 or 3 year, steady state, up to ~72% off, Standard or Convertible | "steady state", "known for a year" |
| Savings Plans | Commit to spend per hour for 1 or 3 years. Compute SP spans EC2, Fargate, Lambda. EC2 Instance SP locks family and Region. | "flexible commitment", "Lambda and Fargate too" |
| Spot | Up to 90% off, can be reclaimed with 2 minute warning | "fault tolerant", "batch", "can be interrupted" |
| Dedicated Host | Physical server for you, visibility into sockets/cores | "BYOL", "server-bound licensing", "compliance requires dedicated hardware" |
| Dedicated Instance | Instance on hardware not shared with other accounts, no socket visibility | "isolated hardware, no licensing need" |
| Capacity Reservation | Reserve capacity in an AZ, any duration, On-Demand price | "guarantee capacity for an event" |

| | EC2 Auto Scaling | Elastic Load Balancing |
|---|---|---|
| Does | Adds and removes instances by policy, replaces unhealthy ones | Distributes traffic across healthy targets in multiple AZs |
| Answers | Scalability and self-healing | Availability and distribution |
| Scaling types | Manual, scheduled, dynamic (target tracking, step, simple), predictive | n/a |

| Load balancer | Layer | Routes on | Keyword |
|---|---|---|---|
| **ALB** | 7 | Path, host, header, query, HTTP methods; targets: EC2, IP, Lambda, containers | "HTTP/HTTPS", "microservices", "path-based routing", "WebSocket" |
| **NLB** | 4 | TCP/UDP/TLS, static IP per AZ, millions of req/s | "extreme performance", "static IP", "non-HTTP" |
| **GWLB** | 3 | Transparent gateway to third-party virtual appliances (firewalls, IDS) | "third-party security appliance", "inspect traffic inline" |
| Classic | 4/7 | Legacy | "Classic" only in old questions |

| Serverless and containers | Is | Keyword |
|---|---|---|
| **Lambda** | Run code on event, pay per request and GB-second, 15 min max, up to 10 GB memory | "no servers", "event-driven", "runs briefly" |
| **ECS** | AWS-native container orchestration | "Docker", "AWS-native, simpler than Kubernetes" |
| **EKS** | Managed Kubernetes control plane | "Kubernetes", "portable to other clouds" |
| **Fargate** | Serverless compute for ECS and EKS, no EC2 to manage | "containers without managing instances" |
| **ECR** | Container image registry | "store Docker images" |
| **Lightsail** | Bundled VPS with fixed monthly price: compute, storage, DNS, simple DB | "simple website", "WordPress", "predictable low price", "beginner" |
| **Batch** | Managed batch job scheduling, provisions compute including Spot | "batch jobs", "thousands of jobs" |
| **Outposts** | EC2, EBS, S3, RDS on-premises | "on-prem" |

## 3.4 Databases

| Service | Model | Use | Keyword |
|---|---|---|---|
| **RDS** | Managed relational: MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Db2 | OLTP, existing SQL app | "relational", "managed MySQL", "lift and shift database" |
| **Aurora** | AWS-built MySQL/PostgreSQL compatible, 6 copies across 3 AZs, up to 15 replicas, Serverless option | Higher performance relational on AWS | "5x MySQL performance", "auto-scaling storage", "Serverless relational" |
| **DynamoDB** | Key-value and document NoSQL, serverless, single-digit ms, DAX cache, Global Tables | Web scale, session state, gaming, IoT | "NoSQL", "millisecond at any scale", "key-value", "serverless database" |
| **Redshift** | Columnar data warehouse, PB scale, SQL | OLAP, BI | "data warehouse", "analytics on petabytes", "columnar" |
| **ElastiCache** | In-memory Redis or Memcached | Cache, session store, leaderboards | "sub-millisecond", "cache", "reduce DB load" |
| **MemoryDB** | Redis-compatible durable primary DB | In-memory primary database | "Redis as the primary database, durable" |
| **DocumentDB** | MongoDB-compatible document DB | JSON documents | "MongoDB" |
| **Neptune** | Graph DB, Gremlin and SPARQL | Social graphs, fraud rings, recommendation | "graph", "relationships between entities" |
| **Keyspaces** | Cassandra-compatible | Wide column | "Cassandra" |
| **QLDB** | Immutable, cryptographically verifiable ledger, centralised | Audit trail, system of record | "ledger", "immutable history", "verifiable" |
| **Timestream** | Serverless time series DB | IoT metrics, telemetry | "time series" |
| **Managed Blockchain** | Hyperledger Fabric, Ethereum, decentralised | Multi-party trust | "blockchain", "decentralised" |
| **OpenSearch Service** | Search and log analytics | Full-text search, log dashboards | "search", "Kibana/OpenSearch Dashboards" |

- **Memorise:** QLDB is a ledger owned by one party. Managed Blockchain is for multiple parties with no central owner.

| RDS feature | Multi-AZ | Read replica |
|---|---|---|
| Purpose | Availability: synchronous standby, automatic failover | Scalability: asynchronous copy for read traffic |
| Serves reads | No (standby is idle) | Yes |
| Cross-Region | Multi-AZ no, always one Region | Yes |
| Keyword | "failover", "disaster", "HA" | "offload reporting queries", "read-heavy" |

| Migration | Does | Keyword |
|---|---|---|
| **DMS** | Migrate databases with minimal downtime, homogeneous or heterogeneous, continuous replication | "migrate database", "source stays online" |
| **Schema Conversion Tool (SCT)** | Converts schema and code between engines, e.g. Oracle to Aurora PostgreSQL | "different engine", "convert stored procedures" |

## 3.5 Networking

| Component | Does | Keyword |
|---|---|---|
| **VPC** | Isolated virtual network in a Region, your CIDR | "isolated network" |
| Subnet | CIDR slice of the VPC in one AZ; public if its route table has an IGW route | "public subnet", "private subnet" |
| Internet Gateway | Two-way internet access for public subnets | "internet access" |
| NAT Gateway | Outbound-only internet for private subnets, managed, per-AZ | "private instances need to download updates" |
| Route table | Rules for where subnet traffic goes | |
| Security group | Stateful instance firewall, allow only | |
| NACL | Stateless subnet firewall, allow and deny | |
| VPC peering | Private 1:1 connection between two VPCs, non-transitive, can be cross-account and cross-Region | "connect two VPCs", "no overlapping CIDR" |
| **Transit Gateway** | Hub connecting many VPCs and on-premises, transitive | "hub and spoke", "hundreds of VPCs" |
| **PrivateLink / Interface endpoint** | Private access to AWS services or partner services via ENI, no IGW, no NAT | "access S3 or a SaaS without the internet", "keep traffic on the AWS network" |
| Gateway endpoint | Free route-table-based endpoint for S3 and DynamoDB only | "S3 from a private subnet, no NAT" |
| VPC Flow Logs | IP traffic metadata | |
| **API Gateway** | Create, publish, secure REST/HTTP/WebSocket APIs, throttling, keys, fronts Lambda | "expose Lambda as an API", "throttle", "API keys" |

**Memorise, Route 53 routing policies:**

| Policy | Routes by |
|---|---|
| Simple | One record, no health check |
| Weighted | Percentage split, A/B and gradual migration |
| Latency | Lowest latency Region for the user |
| Failover | Primary with health check, secondary on failure |
| Geolocation | User's country or continent |
| Geoproximity | Distance to resource, with bias to shift traffic |
| Multivalue answer | Up to 8 healthy records, cheap client-side load balancing |
| IP-based | By client CIDR |

| | Site-to-Site VPN | Direct Connect |
|---|---|---|
| Medium | Internet, IPsec encrypted | Dedicated private line |
| Setup | Minutes to hours | Weeks to months |
| Bandwidth | Up to 1.25 Gbps per tunnel | 1, 10, 100 Gbps dedicated; hosted from 50 Mbps |
| Encrypted | Yes | Not by default; add VPN over DX or MACsec |
| Keyword | "quickly", "backup to DX" | "consistent", "private", "high throughput" |

## 3.6 Storage

**Memorise, S3 storage classes:**

| Class | Retrieval | Min duration | AZs | Keyword |
|---|---|---|---|---|
| Standard | ms | None | 3+ | Frequently accessed, default |
| Intelligent-Tiering | ms (archive tiers optional) | None (monitoring fee) | 3+ | "unknown or changing access pattern" |
| Standard-IA | ms | 30 days, per-GB retrieval fee | 3+ | "infrequent but needs instant access" |
| One Zone-IA | ms | 30 days | 1 | "reproducible data, infrequent" |
| Glacier Instant Retrieval | ms | 90 days | 3+ | "archive but needs ms retrieval, quarterly access" |
| Glacier Flexible Retrieval | minutes to 12 hours (Expedited 1 to 5 min, Standard 3 to 5 h, Bulk 5 to 12 h) | 90 days | 3+ | "archive, hours is fine" |
| Glacier Deep Archive | 12 to 48 hours | 180 days | 3+ | "7 year compliance archive, cheapest" |

- Durability is eleven nines for all classes. Availability differs. One Zone-IA is lost if the AZ is lost.
- Object max 5 TB, multipart upload for over 100 MB recommended, required over 5 GB.

| S3 feature | Does |
|---|---|
| Versioning | Keep every version, protects against overwrite and delete; cannot be disabled, only suspended |
| Lifecycle rules | Transition classes and expire objects on a schedule |
| Replication (CRR / SRR) | Async copy to another bucket, needs versioning both sides |
| Object Lock | WORM: retention periods and legal holds, Governance or Compliance mode |
| Transfer Acceleration | Upload via nearest edge location over the AWS backbone |
| Block Public Access | Account or bucket level override of any public ACL or policy |
| Presigned URL | Time-limited access to a private object |
| Event notifications | To SNS, SQS, Lambda, EventBridge on object events |
| S3 Select / Glacier Select | Query a subset of an object with SQL |
| Static website hosting | Serve HTML directly from a bucket |

| Block / file storage | Is | Keyword |
|---|---|---|
| **EBS** | Network block volume for one instance (io1/io2 Multi-Attach excepted), single AZ, snapshots to S3 | "boot volume", "database disk" |
| EBS gp3 / gp2 | General purpose SSD | Default |
| EBS io2 / io1 | Provisioned IOPS SSD | "high IOPS database" |
| EBS st1 | Throughput HDD | "big data, sequential, cheap" |
| EBS sc1 | Cold HDD | "lowest cost, infrequent" |
| Instance store | Local disk on the host, ephemeral, lost on stop | "temporary", "highest IO, data can be lost" |
| **EFS** | Managed NFS, Linux, multi-AZ, thousands of instances, pay per GB used, IA class | "shared file system, Linux, many instances" |
| **FSx for Windows File Server** | SMB, Active Directory integrated | "Windows", "SMB" |
| **FSx for Lustre** | HPC, ML, integrates with S3 | "high performance computing", "hundreds of GB/s" |
| FSx for NetApp ONTAP / OpenZFS | Enterprise NAS features | "NetApp", "ZFS" |

| Hybrid and transfer | Is | Keyword |
|---|---|---|
| **Storage Gateway, File** | On-prem NFS/SMB backed by S3 | "extend on-prem file share to S3" |
| **Storage Gateway, Volume** | iSCSI block, cached or stored mode, EBS snapshots | "on-prem block storage backed by cloud" |
| **Storage Gateway, Tape** | Virtual tape library to Glacier | "replace physical tapes" |
| **AWS Backup** | Central backup policies across EBS, RDS, DynamoDB, EFS, FSx, S3 | "one place for backups across services" |
| **DataSync** | Online bulk transfer on-prem to S3/EFS/FSx, scheduled | "migrate NFS share over the network" |
| **Transfer Family** | Managed SFTP/FTPS/FTP into S3 or EFS | "SFTP" |
| **Snowcone** | 8 TB, rugged, portable | "edge, very small" |
| **Snowball Edge** | Up to 80 TB usable, Storage or Compute Optimised, can run EC2/Lambda | "petabytes, no network", "weeks over the internet" |
| **Snowmobile** | Truck, up to 100 PB | "exabyte" (retired 2024) |

## 3.7 AI/ML and analytics

| AI/ML | One line | Keyword |
|---|---|---|
| **SageMaker** | Build, train, deploy ML models end to end | "custom model", "data scientists" |
| **Bedrock** | Foundation models via API, no infrastructure | "generative AI", "foundation model" |
| **Rekognition** | Image and video analysis, faces, objects, moderation | "images", "faces" |
| **Textract** | Extract text, forms, tables from documents | "scanned forms", "OCR with structure" |
| **Comprehend** | NLP: sentiment, entities, PII, language | "sentiment", "entities in text" |
| **Lex** | Chatbots, voice and text | "chatbot", "Alexa-like" |
| **Polly** | Text to speech | "read aloud" |
| **Transcribe** | Speech to text | "transcribe call recordings" |
| **Translate** | Text translation | "translate" |
| **Kendra** | Enterprise intelligent search | "search internal documents with natural language" |
| **Personalize** | Recommendations | "recommend products" |
| **Forecast** | Time series forecasting | "demand forecast" |
| **Fraud Detector** | Fraud scoring | "fraudulent transactions" |
| **Augmented AI (A2I)** | Human review of ML predictions | "human in the loop" |
| **CodeWhisperer / Q Developer** | Code suggestions | "AI coding assistant" |

| Analytics | One line | Keyword |
|---|---|---|
| **Athena** | Serverless SQL over S3, pay per TB scanned | "query S3 with SQL, no servers" |
| **EMR** | Managed Hadoop, Spark, Hive, Presto clusters | "Spark", "Hadoop", "big data framework" |
| **Glue** | Serverless ETL plus Data Catalog, crawlers | "ETL", "catalog", "prepare data for analytics" |
| **Glue DataBrew** | Visual data preparation | "no-code cleaning" |
| **Kinesis Data Streams** | Real-time stream ingestion, custom consumers, retention up to 365 days | "real-time", "custom processing" |
| **Kinesis Data Firehose** | Load streams to S3, Redshift, OpenSearch, near real time, no code | "deliver to S3", "near real-time" |
| **Kinesis Data Analytics / Managed Flink** | SQL or Flink over streams | "analyse stream in flight" |
| **Kinesis Video Streams** | Ingest video | "camera feeds" |
| **MSK** | Managed Apache Kafka | "Kafka" |
| **QuickSight** | BI dashboards, ML insights, pay per session | "dashboard", "visualise" |
| **OpenSearch Service** | Search and log analytics | "log analytics", "full-text" |
| **Data Exchange** | Find and subscribe to third-party datasets | "third-party data" |
| **Lake Formation** | Build and secure a data lake on S3 | "data lake permissions" |
| **Redshift** | Warehouse (see 3.4) | |

## 3.8 Other service categories

**Memorise, application integration:**

| | SQS | SNS | EventBridge | Step Functions |
|---|---|---|---|---|
| Pattern | Queue, pull, one consumer per message | Pub/sub, push, fan-out to many subscribers | Event bus, rules route events incl. SaaS and AWS events, scheduler | Workflow orchestration, state machine |
| Keyword | "decouple", "buffer", "retry", "FIFO" | "notify many", "SMS/email/push", "fan-out" | "react to AWS events", "cron", "third-party SaaS events" | "orchestrate Lambdas", "visual workflow", "retries and branching" |
| Note | Standard: at-least-once, unordered. FIFO: exactly-once, ordered, 300 msg/s (3000 batched) | Topic to SQS/Lambda/HTTP/email/SMS | Replaces CloudWatch Events | Standard and Express workflows |

- Amazon MQ: managed ActiveMQ/RabbitMQ, for migrating apps that already speak those protocols.
- AppFlow: SaaS to AWS data transfer (Salesforce to S3) with no code.

| Customer engagement | One line |
|---|---|
| **Connect** | Cloud contact centre |
| **SES** | Transactional and bulk email |
| **Pinpoint** | Marketing campaigns, SMS, push, email, analytics |
| **Chime SDK** | Voice/video into apps |

| Developer tools | One line |
|---|---|
| **CodeCommit** | Managed Git (closed to new customers, may still appear) |
| **CodeBuild** | Build and test, pay per build minute |
| **CodeDeploy** | Deploy to EC2, Lambda, ECS, on-prem; blue/green and rolling |
| **CodePipeline** | CI/CD orchestration of the above |
| **CodeArtifact** | Package repository (npm, pip, Maven) |
| **CodeStar** | Project bootstrap (retired 2024) |
| **Cloud9** | Browser IDE (closed to new customers) |
| **X-Ray** | Distributed tracing, find the slow service in a request chain |
| **CloudShell** | Browser shell with CLI preconfigured |

| End-user computing | One line |
|---|---|
| **WorkSpaces** | Managed virtual desktops (DaaS) |
| **AppStream 2.0** | Stream a single application to a browser |
| **WorkSpaces Web / Secure Browser** | Managed secure browser |

| Front-end, mobile, IoT | One line |
|---|---|
| **Amplify** | Build and host full-stack web/mobile apps, auth, hosting, CI |
| **AppSync** | Managed GraphQL and real-time subscriptions |
| **Device Farm** | Test apps on real phones and browsers |
| **IoT Core** | Connect devices via MQTT, rules to other services |
| **IoT Greengrass** | Run Lambda and ML on edge devices offline |

**Memorise, management and monitoring:**

| Service | One line | Keyword |
|---|---|---|
| **CloudWatch** | Metrics, alarms, logs, dashboards, Events (now EventBridge), Logs Insights | "CPU alarm", "custom metric", "application log" |
| **CloudTrail** | API audit log | "who did what" |
| **Config** | Resource configuration history and compliance rules | "configuration drift", "is X compliant" |
| **Trusted Advisor** | Best-practice checks in 5 to 6 categories, more with Business/Enterprise | "recommendations", "service limits" |
| **Health Dashboard** | Service Health (public, all Regions) and Account Health (personal, your resources, scheduled events) | "is AWS having an outage", "will my instance be retired" |
| **Service Catalog** | Approved product portfolio (CloudFormation templates) for self-service | "approved templates", "governance of what teams can launch" |
| **License Manager** | Track software licences across AWS and on-prem | "Oracle licences", "BYOL tracking" |
| **Compute Optimizer** | ML recommendations to right-size EC2, ASG, EBS, Lambda | "right-size", "over-provisioned" |
| **Launch Wizard** | Guided sizing and deployment for SAP, SQL Server, AD | "deploy SAP" |
| **Well-Architected Tool** | Self-assessment against the 6 pillars, produces improvement plan | "review my workload against best practices" |
| **Resource Groups and Tag Editor** | Group and tag resources in bulk | |
| **Managed Grafana / Managed Prometheus** | Open-source observability, managed | "Grafana", "Prometheus" |
| **Resilience Hub** | Assess and improve resilience, RTO/RPO targets | "resilience assessment" |
| **Fault Injection Service** | Chaos engineering | "inject failures" |

## Self-test

1. A developer wants to deploy a web app without managing servers, but still see the EC2 and ELB it runs on. Which service?
2. Which Route 53 policy sends 10% of traffic to a new version?
3. Query CSV files in S3 with SQL and no infrastructure. Which service?
4. Which S3 class for data accessed once a quarter that must still be retrievable in milliseconds?
5. Which load balancer for a third-party firewall appliance inspecting all traffic inline?
6. Shared Linux file system mounted by 200 instances across AZs. EBS or EFS?
7. Which service converts an Oracle schema to Aurora PostgreSQL?
8. Private subnet instances need to reach S3 without a NAT Gateway and at no extra cost. What do you add?
9. Which service sends a scheduled event every hour to trigger a Lambda?
10. Which service tells you an EC2 instance is scheduled for retirement next week?

Answers:
1. Elastic Beanstalk.
2. Weighted routing.
3. Athena.
4. S3 Glacier Instant Retrieval.
5. Gateway Load Balancer.
6. EFS. EBS attaches to one instance in one AZ.
7. AWS Schema Conversion Tool (DMS does the data).
8. A gateway VPC endpoint for S3.
9. EventBridge Scheduler (or an EventBridge rule on a cron schedule).
10. AWS Health Dashboard, the account-level view.
