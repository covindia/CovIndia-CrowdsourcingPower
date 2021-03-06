# To monitor and update the scores of users
import json
allContributors = {}

def reloadData():
	try:
		global allContributors
		allContributors = json.load(open('res/contributors.json', 'r'))
	except:
		pass

def updatePoints(userId, username): # this is used in the startSauron.py
	userId = str(userId)
	reloadData()
	if (userId not in allContributors):
		allContributors[userId] = []
		allContributors[userId].insert(0, username)
		allContributors[userId].insert(1, 1)
	else:
		allContributors[userId][1] += 1
	
	j = json.dumps(allContributors)
	f = open('res/contributors.json', 'w')
	f.write(j)
	f.close()

def getLeaderBoard():
	reloadData()
	scoreBoard = 'Current leaderBoard :\n\n'
	for boi in allContributors:
		scoreBoard += allContributors[boi][0] + ' : ' + str(allContributors[boi][1]) + '\n'
	return scoreBoard