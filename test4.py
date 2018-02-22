# Class Inheritance

# Inheritance allows us to inherit attributes and methods from a parent class
# it is useful because we can create subclasses

class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) # or Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay) # or Employee.__init__(self, first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp not in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())



dev1 = Developer('Vickranth', 'Kalloli', 65000, 'Python')
dev2 = Developer('Test', 'User', 60000, 'Golang')

# print(dev1.email)
# print(dev1.prog_lang)

mgr1 = Manager('Mgr', 'Test', 95000, [dev1])

# two built in classes called isinstance() and issubclass()
# isinstance() will tell us if an object is an instance of a class

mgr1.print_emps()
print(isinstance(mgr1, Employee))
print(issubclass(Manager, Developer))