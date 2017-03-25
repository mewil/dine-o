class User(object):

	def __init__(self, phoneNumber, name=''):
		self.phoneNumber = phoneNumber
		self.name = name

	def setPhoneNumber(phoneNumber):
		self.phoneNumber = phoneNumber

	def getPhoneNumber():
		return self.phoneNumber

	def setName(name):
		self.name = name

	def getName():
		return self.name
