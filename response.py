# Response module that contains parsing functions

from Item import Item
from User import User

def parseMain(sms, fr, db, client):
	# PARSE RESPONSES
	# [Name][Phone#1,Phone#2,...][FirstItem,SecondItem,...]
	# find name
	index_openB = 0
	index_closeB = sms.find(']')
	name = sms[index_openB+1:index_closeB]
	# find phoneNumbers
	sms_phoneNumbers = sms[index_closeB+2:sms.find(']', index_closeB+1)]
	phoneNumbers = sms_phoneNumbers.split(',')
	for i in range(len(phoneNumbers)):
		if phoneNumbers[i][0] != 1 and len(phoneNumbers[i]) <=10:
			phoneNumbers[i] = '+1' + phoneNumbers[i]
		else:
			phoneNumbers[i] = '+' + phoneNumbers[i]
	# find items
	index_closeB = sms.find(']', index_closeB+len(sms_phoneNumbers))
	sms_items = sms[index_closeB+2:sms.find(']', index_closeB+1)]
	items = sms_items.split(',')

	# DEFINE USERS LIST AND RESTAURANTS LIST
	Users = []
	Users.append(User(fr, name))
	for i in range(len(phoneNumbers)):
		Users.append(User(phoneNumbers[i]))
	Items = []
	for i in range(len(items)):
		Items.append(Item(items[i]))

	# SELECT TWILIO PHONE NUMBER
	currentNumbers = client.phone_numbers.list()
	for currentNumber in currentNumbers:
		if currentNumber.phone_number not in db:
			#set phone number and other data, then return
			db[currentNumber.phone_number] = [Users, Items, 0]
			sendReplies(Users, Items, currentNumber.phone_number, client, db)
			return

	# # PURCHASE NEW TWILIO NUMBER IF THE TOO FEW TWILIO NUMBERS EXIST
	# purchaseNumbers = client.phone_numbers.search(
	#     area_code="734",
	#     country="US",
	#     type="local"
	# )
	# if purchaseNumbers:
	# 	purchasedNumber = purchaseNumbers[0].purchase()
	# 	sendReplies(Users, Items, purchasedNumber, client, db)
	# 	db[purchasedNumber] = [Users, Items, 0]
	# 	#send out surveys


def parseResponse(sms, to, db, client):
	#parse responses
	items = sms.split(',')

	#add restaurant responses
	for i in range(len(items)):
		if item[i] in db[to][1]:
			db[to][1][i].addVotes()

	db[to][2] += 1

	#send out decisions if necessary
	if db[to][2] >= len(db[to][0]):
		max = 0
		maxItem = ''
		for i in db[to][1]:
			if db[to][1][i] >= max:
				maxItem = db[to][1][i]
				max = db[to][1][i]
		for user in users:
			client.messages.create(
		    	to= db[to][0][user].getPhoneNumber(),
		    	from_= db[to],
		    	body = 'Your group chose ' + maxItem
		    )
		del db[to]

def sendHelpMenu(client):
	client.messages.create(
	    	to= ['From'],
	    	from_= TWILIO_PHONE_NUMBER,
	    	body = 'USAGE:\n HELP\n CURRENT\n POST [Name][Phone#1,Phone#2,...][FirstItem, SecondItem,...]'
    )

def sendReplies(users, items, phoneNumber, client, db):
	b = users[0].getName() + ' would like to Dine-o with you! Please reply with the items you would like from this list:\n'
	for i in range(len(db[phoneNumber][1])):
		b = b + str(i) + ' ' + str(db[phoneNumber][1][i])
	print users
	for i in range(len(users)):
		print('Sending message')
		client.messages.create(to= db[phoneNumber][0][i].getPhoneNumber(), from_= phoneNumber, body = b)
