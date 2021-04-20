from user import User
from split import Split

class PercentSplit(Split):
	def __init__(self, user, percent):
		self.user = user
		self.percent = percent


# ps = PercentSplit(User(1, "ad", "sad", 123), 100)
# ps.amount = 1000

