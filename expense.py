from user import User
from split import Split

class Expense(object):
	def __init__(self, amount, paidBy, splits):
		self.amount = amount
		self.paidBy = paidBy
		self.splits = splits
