# Response module that contains parsing functions

def parseMain(sms):
	# parse responses
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

	currentNumbers = client.phone_numbers.list()
	for currentNumber in currentNumbers:
		if currentNumber !in db.phoneNumbers:
			#set phone number and other data, then returns
			sendReplies(users, currentNumber)
			return

	#otherwise purchases a new number and sets it and other data
	purchaseNumbers = client.phone_numbers.search(
	    area_code="734",
	    country="US",
	    type="local"
	)

	if purchaseNumbers:
	    purchasedNumber = purchaseNumbers[0].purchase()
		sendReplies(users, purchasedNumber)
		db.#add users
		#send out surveys

	return




def parseResponse(sms):
	#parse responses
	items = sms.split(',')
	#db.#add restaurant responses
	#send out decisions if necessary


def sendHelpMenu():
	client.messages.create(
	    	to= ['From'],
	    	from_= TWILIO_PHONE_NUMBER,
	    	body = 'USAGE:\n /HELP\n /CURRENT\n /POST [Name][Phone#1,Phone#2,...][FirstItem, SecondItem,...]'
    )

def sendReplies(users, phoneNumber):
	for user in users;
		client.messages.create(
	    	to= user.phoneNumber,
	    	from_= phoneNumber,
	    	body = 'USAGE:\n /HELP\n /CURRENT\n /POST [Name][Phone#1,Phone#2,...][FirstItem, SecondItem,...]'
	    )



