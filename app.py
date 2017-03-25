from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient
import urllib
# from googleplaces import GooglePlaces, types, lang
from smsParser import *

#AUTHORIZATION KEYS
TWILIO_ACCOUNT_SID = 'ACad66d36626749e01761ba8b7f811e80d' 
TWILIO_AUTH_TOKEN = 'eaddcc0f9ea6603d03d12509f4d4c6cd'
TWILI0_PHONE_NUMBER= '+12485957598'

GOOGLE_API_KEY = 'AIzaSyD6Gz70kzaVyt_nMmo--S6nrXswUjH1TE8'

google_places = GooglePlaces(YOUR_API_KEY)


# 1 
# Recieve initialization sms from primary user
# Expected contents:
# 	Location
# 	Numbers of Friends
# 	Name
myDine = parseInit(['Body'])

 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
app = Flask(__name__)

 
# A route to respond to SMS messages and kick off a phone call.
@app.route('/sms', methods=['POST'])
def inbound_initial_sms():

	
	response = twiml.Response()
	response.message('Your Group has been notified')

	# Grab the relevant phone numbers.
	from_number = TWILI0_PHONE_NUMBER
	to_number = request.form['To']

	for friend in friends:
		client.messages.create(
	    	to= friend.number,
	    	from_= TWILI0_PHONE_NUMBER,
	    	body = 'Your friend ' + primaryUser + ' would like to get some food near ' + location +
	    		   '\n '
    	)
	
 
	return str(response)
 
 
# A route to handle the logic for phone calls.
@app.route('/sms', methods=['POST'])
def outbound_sms():
	song_title = request.args.get('track')
	track_url = spotify.get_track_url(song_title)
 
	response = twiml.Response()
	response.play(track_url)
	return str(response)
 
app.run(host='0.0.0.0', debug=True)
