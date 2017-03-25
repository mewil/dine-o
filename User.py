class User(object):

	def __init__(self, phoneNumber, name=''):
		self.phoneNumber = phoneNumber
		self.name = name

	def setPhoneNumber(self, phoneNumber):
		self.phoneNumber = phoneNumber

	def getPhoneNumber(self):
		return self.phoneNumber

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name
