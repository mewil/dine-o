from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient

from response import *

from Item import Item
from User import User

#AUTHORIZATION KEYS
TWILIO_ACCOUNT_SID = 'ACad66d36626749e01761ba8b7f811e80d' 
TWILIO_AUTH_TOKEN = 'eaddcc0f9ea6603d03d12509f4d4c6cd'
TWILIO_BASE_PHONE_NUMBER = '+12485957598'

db = {} # users_list, restaurants_list, numReplies

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def inbound_sms():
	if ['Body'] == '/help' or ['Body'] == '/Help' or ['Body'] == '/HELP':
		sendHelpMenu(client)
	
	elif ['To'] == TWILIO_BASE_PHONE_NUMBER:
		parseMain(['Body'], ['From'], db, client)

	elif ['To'] in db:
		parseResponse(['Body'], ['To'], db, client)

	else:
		sendHelpMenu(client)




app.run(host='0.0.0.0', debug=True)