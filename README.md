# triage-desk-demo

A throwaway repository used to demonstrate
[triage-desk](https://github.com/Seif-Abdelhamid/triage-desk) on a real pull
request. `app.py` on the demo branch is **deliberately vulnerable**. Do not
deploy or reuse it.

The review comments on the pull request were posted by triage-desk's scan job
(`jobs.run_scan`) run locally against the GitHub API. The `/triage` reply was
processed by its command handler (`jobs.handle_comment`). There is no hosted
bot and no webhook. The bot and the reviewer use the same GitHub account.
