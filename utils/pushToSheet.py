import gspread
from oauth2client.service_account import ServiceAccountCredentials
from startSauron import getTokens #resuing the function ;)
from utils.validateDetails import verifyStateDistrict, verifySpam, verifyNum
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('res/credentials.json',scope) # hidden, it's a secret

client = gspread.authorize(creds)
tokens = getTokens()

sheet = client.open_by_url(tokens[1]).worksheet('Sheet1')  # till here all gspread API stuff

def next_available_row(worksheet): # returns the next available row in the sheet
	str_list = list(filter(None, worksheet.col_values(1)))
	return str(len(str_list)+1)

def death_update(dataList): #used in startSauron.py
	next_row = next_available_row(sheet)
	column = "A"
	i = 1
	try:
		suggestions = verifyStateDistrict(dataList[3], dataList[4])[1]
	except:
		pass

	if(verifyStateDistrict(dataList[3], dataList[4])[0] == 0 and verifySpam(dataList[3], dataList[4], 'death') and verifyNum(dataList[5])):
		while(column < "J"):
			if(column != "E"):
				sheet.update_acell("{}{}".format(column,next_row), dataList[i]) #this is what pushes the data to the sheet
				i += 1
			column = chr(ord(column) + 1)  # we cant do column += 1 since it's a char, this is the only way to increase it
		return ['I have updated my database successfully!', True]
	
	elif(not verifyNum(dataList[5])):
		return['Hey! You have to enter a number, not type it! /help for more help', False]
	elif(verifyStateDistrict(dataList[3], dataList[4])[0] == 1):
		return ['Unable to find {} in {}, please check and try again\nPossible suggestions:\n{}'.format(dataList[4], dataList[3], suggestions), False]
	elif(verifyStateDistrict(dataList[3], dataList[4])[0] == 2):
		return ['Unable to find {}, please check and try again\nPossible suggestions:\n{}'.format(dataList[3], suggestions), False]
	else:
		return ['This is already reported. Be more careful next time', False]
	
	# the return is sent to startSauron.py, and is sent as a reply to the user

def infection_update(dataList): # this too is used in startSauron.py, very similar to the above function
	next_row = next_available_row(sheet)
	column = "A"
	i = 1
	try:
		suggestions = verifyStateDistrict(dataList[3], dataList[4])[1]
	except:
		pass
	
	if(verifyStateDistrict(dataList[3], dataList[4])[0] == 0 and verifySpam(dataList[3], dataList[4], 'infection') and verifyNum(dataList[5])):
		while(column < "J"):
			if(column != "F"):
				sheet.update_acell("{}{}".format(column,next_row), dataList[i])
				i += 1
			column = chr(ord(column) + 1)
		return ['I have updated my database successfully!', True]

	elif(not verifyNum(dataList[5])):
		return['Hey! You have to enter a number, not type it! /help for more help', False]
	elif(verifyStateDistrict(dataList[3], dataList[4])[0] == 1):
		return ['Unable to find {} in {}, please check and try again\nPossible suggestions:\n{}'.format(dataList[4], dataList[3], suggestions), False]
	elif(verifyStateDistrict(dataList[3], dataList[4])[0] == 2):
		return ['Unable to find {}, please check and try again\nPossible suggestions:\n{}'.format(dataList[3], suggestions), False]
	else:
		return ['This is already reported. Be more careful next time', False]