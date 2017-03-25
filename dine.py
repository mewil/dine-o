from user import User

class Dine(object):
# location is the area i.e. South U
	def __init__(self, location, phoneNumbers_friends, phoneNumber_primary, primaryName):
		self.phoneNumbers = phoneNumbers # list of all the phone numbers of friends
		self.phoneNumber_primary = phoneNumber_primary
		self.primaryName = primaryName
		self.location = location
		self.votes = []
		self.restaurants = []
		self.dictionary = {}
		self.users = []
		#Adds phoneNumbers_friends and phoneNumber_primary to users
		for pn in range(0, len(phoneNumbers)):
			users.append(User(phoneNumbers[pn]))
		users.append(User(phoneNumber_primary, primaryName))

	def setRestaurants(restaurantList):
        self.restaurants = restaurantList

    def getRestaurants():
        return self.restaurants

    def setVotes(restaurantList):
        self.votes = votesList

    def getVotes():
        return self.votes

    def setDictionary(restaurantList, voteList):
        self.dictionary = dict(zip(restaurantList, voteList))

    def getDictionary():
        return self.dictionary
