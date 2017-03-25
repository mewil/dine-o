def parseMain(sms):
	# parse responses
	# Name,Phone#1,Phone#2,...
	indices_comma = []
	for i in range(0, len(sms)):
		if sms[i] == ',':
			indices_comma.append(i)
	numCommas, numPhoneNumbers = len(indices_comma), len(indices_comma)
	name_primary = sms[:indices_comma[0]]
	phoneNumbers = []
	for i in range(0,numCommas):
		phoneNumbers.append
	db.#add users
	#send out surveys




def parseResponse(sms):
	#parse responses
	db.#add restaurant responses
	#send out decisions if necessary


def sendHelpMenu():
	client.messages.create(
	    	to= ['From'],
	    	from_= TWILIO_PHONE_NUMBER,
	    	body = 'USAGE:\n /HELP\n /CURRENT\n /POST Name,Phone#1,Phone#2,...\n     [FirstItem, SecondItem,...]'
    )