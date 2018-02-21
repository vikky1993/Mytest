# Difference between regular methods, class methods and static methods

# regular methods in a class automatically takes in instance as the first argument and by convention we wer 
# calling this self

# So how can we make it to take class as the first argument, to do that we gonna use class methods


#just add a decorator called @classmethod to make a class method

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

# common convention for class variable is cls
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

# you may hear people say they use class methods as alternative constructors
# what do they mean by this is we can use these class methods in order to provide multiple ways of creating or objects

# this new method as an alternative constructor, usually these start with from - and that's convention also
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay) #this line is going to create the new employee, so we will return it too

# now lets see what is a static method, static method dont pass as argument automatically
# usually they behave just like regular functions, except we include them in our classes because they have some
# logically connection with the class

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

#usually a method should be made static if you dont access instance(self) or class(cls) anywhere within function

emp1 = Employee('Vickranth', 'Kalloli', 70000)
emp2 = Employee('User', 'Test', 50000)

import datetime
my_date = datetime.date(2018, 2, 21)

print(Employee.is_workday(my_date))