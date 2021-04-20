from user import User
from split import Split
from expense import Expense
from exactsplit import ExactSplit

class ExactExpense(Expense):
	def __init__(self, amount, paidBy, splits):
		self.amount = amount
		self.paidBy = paidBy
		self.splits = splits

	def validate(self):
		for split in self.splits:
			if not isinstance(split, ExactSplit):
				return False

		totalAmount = self.amount
		sumSplitAmount = 0
		for split in self.splits:
		    amountSplit = split.amount
		    sumSplitAmount += amountSplit


		if (totalAmount != sumSplitAmount):
		    return False

		return True


# es = EqualSplit(User(1, "ad", "sad", 123))

# print isinstance(es, EqualSplit)