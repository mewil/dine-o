# Module to contain functions used to parse sms input into app.py

from dine import Dine


# Function to parse initialization message from primary user
# prompt: List your name, the phone numbers of intended recipients and the AA zone (separated by commas, with no spaces after commas)
# format: name, number, number, ..., location
def parseInit(sms, phoneNumFrom):
	# parse the primary name
	index_comma1 = sms.find(',')
	primaryName = sms[:index_comma1]

	# parse the phone numbers into a list of strings
	numCommas = 0
	indices_comma = []
	for i in range(0, len(sms)):
		if sms[i] == ',':
			numCommas += 1
			indices_comma.append(i)
	numPhoneNumbers = numCommas - 1
	phoneNumbers_friends = []
	for i in range(0, numPhoneNumbers):
		phoneNumbers_friends.append(sms[indices_comma[i]+1:indices_comma[i+1]])

	# parse the location into a zone int
	location_str = sms[indices_comma[-1]+1:]
	if location_str == 'South U':
		location = 0
	elif location_str == 'Packard':
		location = 1
	elif location_str == 'State St':
		location = 2
	elif location_str == 'Downtown':
		location = 3
	else:
		location = -1

	# return type:  Dine(location, phoneNumbers_friends, phoneNumber_primary, primaryName)
	return Dine(location, phoneNumbers_friends, phoneNumber_primary, primaryName)

# Function to parse votes from primary and secondary users
# prompt: From the numbered list of restaurants, reply with the numbers of restaurants at which you'd be fine.
# response format is list of numbers separated by spaces or commas
#def parseVotesR1(string sms, Dine myDine):
	#parse string into myDine
	


#return type = Dine()