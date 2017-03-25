from user import User

class Dine(object):

	def __init__(self, location, phoneNumbers_friends, phoneNumber_primary, primaryName):
		self.phoneNumbers = phoneNumbers # list of all the phone numbers of friends
		self.phoneNumber_primary = phoneNumber_primary
		self.primaryName = primaryName
		self.location = location
		
		self.users = []
		for pn in range(0, len(phoneNumbers)):
			users.append(User(phoneNumbers[pn]))
		users.append(User(phoneNumber_primary, primaryName))