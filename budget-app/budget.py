import math
class Category:
	title = ''
	ledger = list()

	def __init__(self,category):
		self.title = category.capitalize()
		self.ledger = list()

	def deposit(self,amount,description=''):
		self.ledger.append({'amount':amount, 'description':description})

	def withdraw(self,amount,description=''):
		if self.check_funds(amount):
			self.ledger.append({'amount':-amount, 'description':description})
			return True
		else:
			return False

	def get_balance(self):
		total = 0
		for entry in self.ledger:
			total += entry.get('amount')
		return total

	def check_funds(self,amount):
		return amount <= self.get_balance()

	def transfer(self,amount,destination):
		if self.check_funds(amount):
			message = f'Transfer to {destination.title}'
			self.withdraw(amount, message)
			message = f'Transfer from {self.title}'
			destination.deposit(amount, message)
			return True
		else:
			return False

	

	def __str__(self):
		string = self.title.center(30,'*') + '\n'
		for entry in self.ledger:
			description_str = entry.get('description')[:23].ljust(23,' ')
			amount = "{:.2f}".format(float(entry.get('amount')))
			amount_str = str(amount).rjust(7,' ')
			string +=  description_str + amount_str + '\n'
		string += 'Total: ' + str(self.get_balance())
		return string

	# Extra methods
	def get_title(self):
		return self.title

	def get_withdrawal(self):
		total = 0
		for entry in self.ledger:
			amount = entry.get('amount')
			if amount < 0:
				total += amount
		return total


def get_percentages(categories):
	spends = list()
	total = 0
	for category in categories:
		spend = category.get_withdrawal()
		spends.append(spend)
		total += spend
	percentages = list()
	for spend in spends:
		percentages.append(math.floor(spend/total*100))
	return percentages

def get_titles(categories):
	longest_title_length = 0
	titles = list()
	for category in categories:
		title = category.get_title()
		titles.append(title)
		if len(title) > longest_title_length: longest_title_length=len(title)
	titles.append(longest_title_length)
	return titles

def create_spend_chart(categories):
	num_categories = len(categories)
	chart = 'Percentage spent by category\n'
	# The graph
	y = ('100', ' 90', ' 80', ' 70', ' 60', ' 50', ' 40', ' 30', ' 20', ' 10', '  0')
	percentages = get_percentages(categories)
	for line in y:
		num = int(line)
		tmp = line + '|'
		for percentage in percentages:
			if percentage >= num: tmp += ' o '
			else: tmp += '   '
		chart += tmp + ' \n'

	# x-axis
	chart += '    ' + '---'*num_categories + '-\n'

	# categories title
	titles = get_titles(categories)
	lines = titles.pop()
	for line in range(lines):
		tmp = '    '
		for title in titles:
			try:
				tmp += ' ' + title[line] + ' '
			except:
				tmp += '   '
		chart += tmp + ' \n'

	return chart.rstrip()+'  '