#!/usr/bin/env python

import json
import os
import sys
import urllib2

# Define empty lists
gh_users = [];
anon_users = [];

def process_gh_user(user):
	gh_users.append({
		'username': user["login"], 
		'commits': user["contributions"]
	})

def process_anon_user(user):
	anon_users.append(user)

def print_results():
	print "# GitHub users"
	sorted_gh_users = sorted(gh_users, key=lambda k: k['commits'], reverse=True)
	for gh_user in sorted_gh_users:
		print "- [ ] " + str(gh_user['commits']) + " ["+ gh_user['username'] +"](https://github.com/" + gh_user['username'] + ")"
	
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
	page = 1;

	while True:
		print "Processing page " + str(page)
		repo_url = "https://api.github.com/repos/zeromq/libzmq/contributors?anon=true&access_token=" + gh_token + "&page=" + str(page);
		content_json_str = urllib2.urlopen(repo_url).read()
		user_arr = json.loads(content_json_str)
		
		if (len(user_arr) == 0):
			break;
			
		for user in user_arr:
			if (user["type"] == "User"):
				process_gh_user(user)
			else:
				process_anon_user(user)
			
		page += 1

	print_results()

if __name__== "__main__":
	main()
