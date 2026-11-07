# C3 teardown

Nothing here bills, so the order is by what a stray login could do, not by
cost. The user has a console password and must go first.

- [ ] Delete the user's console password: `aws iam delete-login-profile --user-name clf-test`
- [ ] Deactivate and delete any MFA device on the user, if one was added
- [ ] Remove the user from the group: `aws iam remove-user-from-group --group-name clf-readers --user-name clf-test`
- [ ] Delete the user: `aws iam delete-user --user-name clf-test`
- [ ] Delete the inline policy: `aws iam delete-group-policy --group-name clf-readers --policy-name deny-s3`
- [ ] Detach the managed policy: `aws iam detach-group-policy --group-name clf-readers --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess`
- [ ] Delete the group: `aws iam delete-group --group-name clf-readers`
- [ ] Access Analyzer: keep it. It is free and it is the thing that would tell you about a public bucket.
- [ ] Confirm: `aws iam list-users --query 'Users[].UserName'` and `aws iam list-groups --query 'Groups[].GroupName'` no longer show either.
