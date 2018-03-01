## before refactoring

def get_answer(prompt):
	answer = input(prompt)
	# 1 while not (answer == "yes" or answer == "no"):
	# 2 while answer not in ("yes", "no"):
	# 3 while answer not in ["yes", "no"]:
	while answer not in ("yes", "no"):
		answer = input(prompt)
	return answer

print(get_answer("yes or no?"))


## after refactoring