from user import User
from split import Split

class ExactSplit(Split):
	def __init__(self, user, amount):
		Split.__init__(user, amount)
