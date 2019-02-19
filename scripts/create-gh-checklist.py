#!/usr/bin/env python

import json
import os
import string
import sys
import urllib2

# Define repository to check
GH_REPO = "zeromq/libzmq"

# Define empty lists
gh_users = {}
anon_users = []


def process_gh_user(user):
    gh_users[string.lower(user["login"])] = {
        'username': user["login"],
        'commits': user["contributions"],
        'signed': False
    }


def process_anon_user(user):
    anon_users.append(user)


def check_gh_grants():
    relicense_contents_url = "https://api.github.com/repos/" + GH_REPO + "/contents/RELICENSE"

    try:
        relicense_contents_str = urllib2.urlopen(relicense_contents_url).read()
        relicense_grants = json.loads(relicense_contents_str)

        for relicense_grant in relicense_grants:
            if relicense_grant['type'] != "file":
                continue

            gh_user = string.lower(relicense_grant['name'])
            if gh_user.endswith(".md"):
                gh_user = gh_user[:-3]

            if gh_user in gh_users:
                gh_users[gh_user]['signed'] = True
    except urllib2.HTTPError, e:
        print "RELICENSE directory does not exist for " + GH_REPO + " !!"


def print_results():
    print "# GitHub users"
    sorted_gh_users = sorted(gh_users.values(), key=lambda k: (k['signed'], k['commits']), reverse=True)

    for gh_user in sorted_gh_users:
        print "- [" + ("x" if gh_user['signed'] else " ") + "] " + str(gh_user['commits']) + \
              " [" + gh_user['username'] + "](https://github.com/" + gh_user['username'] + ")"

    print ""
    print "# Anonymous users"
    sorted_anon_users = sorted(anon_users, key=lambda k: k['name'])
    for anon_user in sorted_anon_users:
        print "- [ ] " + anon_user['name'].encode('utf-8') + " <" + anon_user['email'].encode('utf-8') + ">"


def main():
    if 'ZMQ_GH_TOKEN' not in os.environ:
        print "ERROR: ZMQ_GH_TOKEN env variable not set!"
        sys.exit()

    gh_token = (os.environ['ZMQ_GH_TOKEN'])

    # Execute request
    page = 1

    while True:
        print "Processing page " + str(page)
        repo_url = "https://api.github.com/repos/" + GH_REPO + "/contributors?anon=true&access_token=" + gh_token + \
                   "&page=" + str(page)
        content_json_str = urllib2.urlopen(repo_url).read()
        user_arr = json.loads(content_json_str)

        if len(user_arr) == 0:
            break

        for user in user_arr:
            if user["type"] == "User":
                process_gh_user(user)
            else:
                process_anon_user(user)

        page += 1

    check_gh_grants()
    print_results()


if __name__ == "__main__":
    main()
