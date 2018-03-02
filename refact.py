## before refactoring

# def get_answer_previous(prompt):
# 	answer = input(prompt)
# 	# 1 while not (answer == "yes" or answer == "no"):
# 	# 2 while answer not in ("yes", "no"):
# 	# 3 while answer not in ["yes", "no"]:
# 	while answer not in ("yes", "no"):
# 		answer = input(prompt)
# 	return answer

# print(get_answer("yes or no?"))


## after refactoring
def get_answer(prompt):
	while True:
	 	answer = input(prompt) #.strip().lower() # strip() to strip spaces and lower to accept the cases
		if answer in ('yes', 'no'):
			return answer

print(get_answer("yes or no?"))
