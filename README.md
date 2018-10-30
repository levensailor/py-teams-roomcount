# py-teams-roomcount

Uses the Webex Teams SDK to count memberships of the rooms per token user or bot. 

#### Instructions

1. Copy API token from https://developer.webex.com and set token variable in roomcount.py
2. Run `pip install webexteamssdk`
3. Run `python roomcount.py`

```sh
(python3) jlevensailor in ~/Code/py-teams-roomcount 🌮 python roomcount.py

name: Brainstorming
team: Code Camp
last activity: 2018-10-19T18:44:41.823Z
created: 2017-12-07T19:40:06.956Z
count: 87

name: General
team: Spark me UP
last activity: 2018-10-26T21:44:11.167Z
created: 2017-09-20T15:49:44.423Z
count: 197

name: Jeffs Bot Playground
team:
last activity: 2018-09-28T15:58:33.321Z
created: 2017-09-20T22:42:14.752Z
count: 19
```