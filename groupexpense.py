from user import User
from split import Split
from expense import Expense
from group import Group

class GroupExpense(Expense):
	def __init__(self, amount, paidBy, splits, group):
		self.amount = amount
		self.paidBy = paidBy
		self.splits = splits
		self.group = group

	def validate(self):
		#Group Validation
		for split in self.splits:
			if split.user not in group.users:
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