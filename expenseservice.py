from user import User
from split import Split
from expense import Expense
from equalsplit import EqualSplit
from percentsplit import PercentSplit
from exactsplit import ExactSplit


class ExpenseService(object):
	def createExpense(self, expenseType, amount, paidBy, splits):
		if(expenseType == "EXACT"):
			return ExactExpense(amount, paidBy, splits)
		if(expenseType == "PERCENT"):
			for split in splits:
				split.amount = float(amount)*split.percent/100.0
			return PercentExpense(amount, paidBy, splits)
		if(expenseType == "EQUAL"):
			totalSplits = len(splits)
			splitAmount = float(amount)/float(totalSplits)
			for split in splits:
				split.amount = splitAmount
			return EqualExpense(amount, paidBy, splits)
		return None