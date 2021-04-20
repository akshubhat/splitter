from user import User
from split import Split

class EqualSplit(Split):
	def __init__(self, user):
		self.user = user