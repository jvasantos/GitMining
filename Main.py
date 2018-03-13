from github import Github
import json

USER = ""
PASS = ""
organization = ""
repository = ""
g = Github(USER, PASS)

D = {}

count = 0
countOp = 0
countEd = 0
org = g.get_organization(organization)
repo = org.get_repo(repository)

# get commits
for con in repo.get_contributors():
    D[con.login] = {}
    D[con.login]['commits'] = con.contributions
    D[con.login]['opened issues'] = 0
    D[con.login]['closed issues'] = 0
    D[con.login]['pull requests'] = 0
    D[con.login]['merged pulls'] = 0

# get issues
for issue in repo.get_issues(state='all'):
    u1 = issue.user.login
    if issue.state == "closed":
        u2 = issue.closed_by.login
        if u2 not in D:
            D[u2] = {}
            D[u2]['commits'] = 0
            D[u2]['opened issues'] = 0
            D[u2]['closed issues'] = 0
            D[u2]['pull requests'] = 0
            D[u2]['merged pulls'] = 0
        D[u2]['closed issues'] += 1
    if u1 not in D:
        D[u1] = {}
        D[u1]['commits'] = 0
        D[u1]['opened issues'] = 0
        D[u1]['closed issues'] = 0
        D[u1]['pull requests'] = 0
        D[u1]['merged pulls'] = 0
    D[u1]['opened issues'] += 1
    countOp += 1
    print(countOp)

# get pulls
for pull in repo.get_pulls(state="all"):
    u = pull.user.login
    if u not in D:
        D[u] = {}
        D[u]['commits'] = 0
        D[u]['opened issues'] = 0
        D[u]['closed issues'] = 0
        D[u]['pull requests'] = 0
        D[u]['merged pulls'] = 0
    D[u]['pull requests'] += 1
    if pull.merged:
        D[u]['merged pulls'] += 1
    count += 1
    print(count)


print(D)

with open('data.json', 'w') as outfile:
    json.dump(D, outfile, ensure_ascii=False)