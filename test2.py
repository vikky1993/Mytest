# Class Variables

## class variables are variables that are shared among all instances of a class.

class Employee:

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1 #we are using Employee instead of self because we do not want it to be different
		# and we do not want it to be changed using instance

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps) #before instantiating

emp1 = Employee('Vickranth', 'Kalloli', 65000)
emp2 = Employee('Test', 'User', 50000)

#To print out namespace of the emp1 and we can see there is no raise_amount in this
print(emp1.__dict__)
#prints out the raise_amount and this is the value our instances see
print(Employee.__dict__)



print(emp1.raise_amount)
print(Employee.raise_amount)

print(Employee.num_of_emps) #after instantiating