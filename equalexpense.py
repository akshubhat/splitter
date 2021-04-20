from user import User
from split import Split
from expense import Expense
from equalsplit import EqualSplit

class EqualExpense(Expense):
	def __init__(self, amount, paidBy, splits):
		self.amount = amount
		self.paidBy = paidBy
		self.splits = splits

	def validate(self):
		for split in self.splits:
			if not isinstance(split, EqualSplit):
				return False
		return True


es = EqualSplit(User(1, "ad", "sad", 123))

print isinstance(es, Split)