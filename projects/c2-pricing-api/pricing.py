#!/usr/bin/env python3
"""Price one EC2 instance type, the S3 storage classes and data transfer for a
region, from the AWS Pricing API, as Markdown tables.

The Pricing API is served from us-east-1 (and ap-south-1) only; the --region
flag selects which region's prices to look up, not where the call goes.
"""

import argparse
import json
import sys
from datetime import date

import boto3

LOCATIONS = {
    "us-east-1": "US East (N. Virginia)",
    "us-east-2": "US East (Ohio)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    "ca-central-1": "Canada (Central)",
    "eu-west-1": "EU (Ireland)",
    "eu-west-2": "EU (London)",
    "eu-central-1": "EU (Frankfurt)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "ap-south-1": "Asia Pacific (Mumbai)",
}

HOURS_PER_YEAR = 8760


def tf(field, value):
    return {"Type": "TERM_MATCH", "Field": field, "Value": value}


def products(client, service_code, filters):
    """Every product matching the filters, parsed from the JSON strings."""
    out = []
    token = None
    while True:
        kwargs = {"ServiceCode": service_code, "Filters": filters, "MaxResults": 100}
        if token:
            kwargs["NextToken"] = token
        page = client.get_products(**kwargs)
        out.extend(json.loads(p) for p in page["PriceList"])
        token = page.get("NextToken")
        if not token:
            return out


def dims(term):
    """Price dimensions of a term, sorted by the start of their range."""
    ds = list(term["priceDimensions"].values())
    return sorted(ds, key=lambda d: float(d.get("beginRange", "0") or 0))


def usd(d):
    return float(d["pricePerUnit"]["USD"])


def ec2(client, location, instance_type):
    filters = [
        tf("instanceType", instance_type),
        tf("location", location),
        tf("operatingSystem", "Linux"),
        tf("tenancy", "Shared"),
        tf("preInstalledSw", "NA"),
        tf("capacitystatus", "Used"),
        tf("licenseModel", "No License required"),
    ]
    found = products(client, "AmazonEC2", filters)
    if not found:
        print(f"No EC2 product for {instance_type} in {location}", file=sys.stderr)
        return
    p = found[0]
    attrs = p["product"]["attributes"]
    on_demand = next(iter(p["terms"]["OnDemand"].values()))
    od_hourly = usd(dims(on_demand)[0])

    print(f"## EC2 {instance_type}, {location}")
    print()
    print(f"{attrs.get('vcpu')} vCPU, {attrs.get('memory')}, {attrs.get('operatingSystem')}, shared tenancy.")
    print()
    print("| Option | Term | Class | Payment | Upfront USD | Hourly USD | Effective hourly USD | Saving vs On-Demand |")
    print("|---|---|---|---|---|---|---|---|")
    print(f"| On-Demand | | | | 0.00 | {od_hourly:.4f} | {od_hourly:.4f} | 0% |")

    rows = []
    for term in p["terms"].get("Reserved", {}).values():
        ta = term["termAttributes"]
        years = int(ta["LeaseContractLength"].rstrip("yr"))
        upfront = sum(usd(d) for d in dims(term) if d["unit"] == "Quantity")
        hourly = sum(usd(d) for d in dims(term) if d["unit"] == "Hrs")
        effective = hourly + upfront / (years * HOURS_PER_YEAR)
        saving = 1 - effective / od_hourly if od_hourly else 0
        rows.append((effective, years, ta["OfferingClass"], ta["PurchaseOption"], upfront, hourly, saving))
    for effective, years, cls, pay, upfront, hourly, saving in sorted(rows, key=lambda r: (r[1], r[2], -r[4])):
        print(f"| Reserved | {years}yr | {cls} | {pay} | {upfront:.2f} | {hourly:.4f} | {effective:.4f} | {saving:.0%} |")
    print()
    print("Effective hourly spreads the upfront fee over every hour of the term. Spot is not in the Pricing API; see the README for the EC2 call.")
    print()


def s3(client, location):
    filters = [tf("location", location), tf("productFamily", "Storage")]
    found = products(client, "AmazonS3", filters)
    print(f"## S3 storage, {location}, first pricing tier per GB-month")
    print()
    print("| Storage class (volumeType) | USD per GB-month | Tier |")
    print("|---|---|---|")
    seen = {}
    for p in found:
        vt = p["product"]["attributes"].get("volumeType", "?")
        od = p["terms"].get("OnDemand")
        if not od:
            continue
        first = dims(next(iter(od.values())))[0]
        price = usd(first)
        if vt not in seen or price < seen[vt][0]:
            seen[vt] = (price, first.get("beginRange", "0"), first.get("endRange", "Inf"))
    for vt, (price, b, e) in sorted(seen.items(), key=lambda kv: -kv[1][0]):
        print(f"| {vt} | {price:.5f} | {b} to {e} GB |")
    print()
    print("Storage only. Requests, retrieval and minimum storage duration are separate charges and are where the cheap classes get expensive.")
    print()


def transfer(client, location):
    print(f"## Data transfer, {location}")
    print()
    print("| Direction | Range GB | USD per GB |")
    print("|---|---|---|")
    queries = [
        ("Out to internet", [tf("fromLocation", location), tf("toLocation", "External"), tf("transferType", "AWS Outbound")]),
        ("In from internet", [tf("fromLocation", "External"), tf("toLocation", location), tf("transferType", "AWS Inbound")]),
        ("Between AZs, same region", [tf("fromLocation", location), tf("toLocation", location), tf("transferType", "IntraRegion")]),
    ]
    for label, filters in queries:
        found = products(client, "AWSDataTransfer", filters)
        if not found:
            print(f"| {label} | no product returned | |")
            continue
        for term in found[0]["terms"]["OnDemand"].values():
            for d in dims(term):
                print(f"| {label} | {d.get('beginRange', '0')} to {d.get('endRange', 'Inf')} | {usd(d):.4f} |")
    print()
    print("Cross-AZ is billed in each direction, so a round trip is two charges.")
    print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--region", default="us-west-2", help="region whose prices to look up")
    ap.add_argument("--instance-type", default="t3.micro")
    args = ap.parse_args()

    location = LOCATIONS.get(args.region)
    if not location:
        sys.exit(f"Unknown region {args.region}; add it to LOCATIONS with its Pricing API location name.")

    client = boto3.client("pricing", region_name="us-east-1")
    print(f"# Pricing API results, {date.today().isoformat()}")
    print()
    print(f"Region {args.region}. Source: AWS Price List API, On-Demand and Reserved terms as published on the date above.")
    print()
    ec2(client, location, args.instance_type)
    s3(client, location)
    transfer(client, location)


if __name__ == "__main__":
    main()
