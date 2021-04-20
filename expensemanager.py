from user import User
from split import Split
from expense import Expense
from exactsplit import ExactSplit
from expenseservice import ExpenseService

class ExpenseManager(object):
	# def __init__(self):
	# 	self.expenses = []
	# 	self.userMap = {}
	# 	self.balanceSheet = {}

	def __init__(self, expenses=[], userMap={}, balanceSheet={}):
		self.expenses = expenses
		self.userMap = userMap
		self.balanceSheet = balanceSheet

	def addUser(self, user):
		self.userMap[user.id] = {}

	def addExpense(self, expenseType, amount, paidBy, splits):
		expense = ExpenseService.createExpense(expenseType, amount, paidBy, splits)
		self.expenses.append(expense)
		for split in splits:
			paidTo = split.user.id
			balances = balanceSheet[paidBy]
			if paidTo not in balanceSheet:
				balanceSheet[paidTo] = 0.0
			balanceSheet[paidTo] = balanceSheet[paidTo] + split.amount

			balances = balanceSheet[paidTo]
			if paidBy not in balanceSheet:
				balanceSheet[paidBy] = 0.0
			balanceSheet[paidBy] = balanceSheet[paidBy] - split.amount

	def printBalance(user1, user2, amount):
		print user1.name+" owes "+user2.name+" : "+amount

	def showBalance(self, user):
		print self.balanceSheet[user.id]
