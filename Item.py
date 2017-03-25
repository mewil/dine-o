class Item(object):

	def __init__(self, name, numVotes=0):
		self.name = name
		self.numVotes = numVotes

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setNumVotes(self, numVotes):
		self.numVotes = numVotes

	def addVotes(self, numVotes=1):
		self.numVotes += numVotes

	def getVotes(self):
		return self.numVotes