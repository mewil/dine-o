from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient

from response import *

from Item import Item
from User import User

#AUTHORIZATION KEYS
ACCOUNT_SID = 'ACad66d36626749e01761ba8b7f811e80d' 
AUTH_TOKEN = 'eaddcc0f9ea6603d03d12509f4d4c6cd'
TWILIO_BASE_PHONE_NUMBER = '+12485957598'

db = {} # users_list, item_list, numReplies

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def inbound_sms():
	print("Message received")
	if request.form['Body'].lower() == 'help':
		sendHelpMenu(client)
	
	elif request.form['To'] == TWILIO_BASE_PHONE_NUMBER:
		parseMain(request.form['Body'], request.form['From'], db, client)

	elif request.formrequest.form['To'] in db:
		parseResponse(request.form['Body'], request.form['To'], db, client)

	else:
		sendHelpMenu(client)

	return 'SUCCESS'




app.run(host='0.0.0.0', debug=True)