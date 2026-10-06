## Merging and approvals

Ask the owner your questions BEFORE you build. Their answers approve the approach. After that, merge your own pull request when the checks are green, review comments are addressed, and there are no conflicts, and say so in your update. Never turn on auto-merge.

These still need the owner's explicit go, typed by them and naming the action, every time:
- Releasing to production.
- Any change to shared data or a shared database.
- Changing an account, cloud, or tenant setting.
- Sending any message on the owner's behalf.
- Deleting anything you didn't create.

Ask for approvals one at a time. Each ask says in plain words what it changes.

## When something is missing

Say exactly what is missing (a permission, a decision, a file, a secret) and stop that part. Don't substitute, mock, or guess.
