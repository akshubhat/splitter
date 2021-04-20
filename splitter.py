from user import User
from split import Split
from expense import Expense
from exactsplit import ExactSplit
from expenseservice import ExpenseService
from expensemanager import ExpenseManager

expenseManager = ExpenseManager()

expenseManager.addUser(User(1, "User1", "akshay1@bhat.com", "9876543210"));
expenseManager.addUser(User(2, "User2", "akshay2@bhat.comh", "9876543210"));
expenseManager.addUser(User(3, "User3", "akshay3@bhat.com", "9876543210"));
expenseManager.addUser(User(4, "User4", "akshay4@bhat.com", "9876543210"));

