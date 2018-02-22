# magic methods
# These special methods allow us to emulate some built-in behavior within python and its also how we 
# implement operator over-loading

# These special methods are always surrounded by __str__ and these are called dunder

class Employee:

	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

		Employee.num_of_emps += 1 

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def __repr__(self):
		return 

	# def __str__(self):
	# 	pass


emp1 = Employee('Vickranth', 'Kalloli', 70000)
emp2 = Employee('User', 'Test', 50000)