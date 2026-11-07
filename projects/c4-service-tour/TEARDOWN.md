# C4 teardown

Ordered by what bills fastest. The instance and its public IP are hourly;
everything else is pro rata or free.

- [ ] Terminate the instance: `aws ec2 terminate-instances --instance-ids INSTANCE_ID`. Wait for `terminated`.
- [ ] Confirm the root volume went with it: `aws ec2 describe-volumes --query 'Volumes[].[VolumeId,State,Size]' --output table` shows nothing new. If a volume is left, delete-on-termination was off; delete it.
- [ ] Confirm no Elastic IP was allocated: `aws ec2 describe-addresses` is empty. Release any that is not.
- [ ] Delete the security group once the instance is gone: `aws ec2 delete-security-group --group-id SG_ID`
- [ ] Delete the function: `aws lambda delete-function --function-name clf-hello`
- [ ] Delete its log group, which is not deleted with the function: `aws logs delete-log-group --log-group-name /aws/lambda/clf-hello`
- [ ] Delete the execution role Lambda created, from the IAM console (it is named `clf-hello-role-...`).
- [ ] Empty the bucket including every version, then delete it. `aws s3 rm --recursive` does not remove old versions:
  ```bash
  aws s3api delete-objects --bucket BUCKET --delete "$(aws s3api list-object-versions --bucket BUCKET --query '{Objects: Versions[].{Key:Key,VersionId:VersionId}}' --output json)" && aws s3 rb s3://BUCKET
  ```
- [ ] Run the S0 sweeper and paste its output into `results.md`.
