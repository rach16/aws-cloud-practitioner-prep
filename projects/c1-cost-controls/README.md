# C1: Cost controls

**Proves:** Budgets alerts before spend, Cost Explorer explains spend after, the
Pricing Calculator estimates before building, and cost allocation tags are what
make any of it attributable. Four tools, four different questions.

**Cost:** none. Every tool here is free at this scale. Cost Explorer's API
calls are billed per request (verify the rate before scripting against it);
the console is free.

**Time:** 45 minutes.

## Steps

Replace `ACCOUNT` with the output of
`aws sts get-caller-identity --query Account --output text`.

- [ ] 1. Billing preferences. Console → Billing and Cost Management → Billing preferences. Turn on Free Tier usage alerts and PDF invoices by email. Note whether "IAM user and role access to billing information" is activated; only root can change it.
- [ ] 2. Budgets. Check what already exists:
  ```bash
  aws budgets describe-budgets --account-id ACCOUNT --query 'Budgets[].[BudgetName,BudgetLimit.Amount,BudgetType]' --output table
  ```
  If there is no monthly cost budget, create one in the console: monthly, fixed amount at your ceiling, alerts at 50% and 80% of **actual** and 100% of **forecasted**, to your email. Re-run the checkpoint.
- [ ] 3. Cost Explorer. Console → Cost Explorer. Last 3 months, monthly, grouped by service. Record the top three services. Checkpoint from the CLI (first call enables the API if the console has been opened):
  ```bash
  aws ce get-cost-and-usage --time-period Start=2026-08-01,End=2026-11-01 --granularity MONTHLY --metrics UnblendedCost --group-by Type=DIMENSION,Key=SERVICE --query 'ResultsByTime[].Groups[?Metrics.UnblendedCost.Amount>`0.01`].[Keys[0],Metrics.UnblendedCost.Amount]' --output table
  ```
- [ ] 4. Cost allocation tags. Console → Billing → Cost allocation tags. Activate the user-defined tag `project`. It takes up to 24 hours to appear in reports; the point is that it is inactive until someone activates it.
  ```bash
  aws ce list-cost-allocation-tags --status Active --output table
  ```
- [ ] 5. Pricing Calculator. [calculator.aws](https://calculator.aws). Estimate a small three-tier app in your region: two `t3.small` Linux On-Demand, one Application Load Balancer, one `db.t3.micro` RDS MySQL Multi-AZ, 50 GB S3 Standard, 100 GB data transfer out. Save and copy the share link.
- [ ] 6. Same estimate, EC2 switched to a 1-year No Upfront Compute Savings Plan. Record the percentage change in the monthly total, not the dollar figures.
- [ ] 7. Free Tier. Console → Billing → Free Tier. Record which services show usage and how close any is to its limit.
- [ ] 8. Optional. CloudWatch billing alarm. Console → CloudWatch, region `us-east-1` only → Alarms → Billing. Note that it needs "Receive Billing Alerts" enabled in Billing preferences first, and that this is the older mechanism the exam still mentions; Budgets is the answer for anything that says "alert" or "forecast".

## Write-up

`results.md`, in this directory:

- The budget that exists: name, amount, which thresholds alert.
- Top three services, last three months, in order. No figures until they have been through C2.
- The activated tag and the date.
- The calculator share link, and the percentage saving from step 6.
- One line each: when you would open Budgets, Cost Explorer, the Pricing Calculator, the Cost and Usage Report.

## Teardown

Nothing to tear down. Leave the budget and the tag in place.
