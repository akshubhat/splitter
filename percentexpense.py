from user import User
from split import Split
from expense import Expense
from percentsplit import PercentSplit

class PercentExpense(Expense):
	def __init__(self, amount, paidBy, splits):
		self.amount = amount
		self.paidBy = paidBy
		self.splits = splits

	def validate(self):
		for split in self.splits:
			if not isinstance(split, PercentSplit):
				return False

		totalPercent = 100
		sumSplitPercent = 0
		for split in self.splits:
		    percentSplit = split.percent
		    sumSplitPercent += percentSplit

		if (totalPercent != sumSplitPercent):
		    return False

		return True


# es = EqualSplit(User(1, "ad", "sad", 123))

# print isinstance(es, EqualSplit)