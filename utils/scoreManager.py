# To monitor and update the scores of users
import json
import os
allContributors = {}

def reloadData():
	try:
		global allContributors
		allContributors = json.load(open('res/contributors.json', 'r'))
	except:
		pass

def updatePoints(userId): # this is used in the startSauron.py
	userId = str(userId)
	reloadData()
	if (userId not in allContributors):
		allContributors[userId] = 1
	else:
		allContributors[userId] += 1
	
	j = json.dumps(allContributors)
	f = open('res/contributors.json', 'w')
	f.write(j)
	f.close()