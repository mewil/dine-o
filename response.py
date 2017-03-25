def parseMain(sms):
	#parse responses
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
	    	body = 'USAGE:\n /HELP\n /CURRENT\n /POST[Event][Name][Phone#1,Phone#2,...]\n     [FirstItem, SecondItem,...]'
    )