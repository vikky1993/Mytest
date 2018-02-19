# Creating and instantiating classes

class Employee:
	# You can think of this method as initalize or as a constructor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


# A class is basically a blue-print for creating instances.

emp_1 = Employee('Vickranth', 'Kalloli', 50000)
emp_2 = Employee('Test', 'User', 60000)

#both are similar
print(emp_1.fullname()) 
print(Employee.fullname(emp_1))