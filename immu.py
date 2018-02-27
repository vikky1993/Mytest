# functional programming in python using immutable data structures

# definition: Functional programming is a programming paradigm or a style of programming where we mainly
# use immutable data structures and we try to avoid side affects by doing all form of computation using
# evaluation of mathematical functions	

scientists = [
	{'name': 'Ada Lovelace', 'field': 'math', 'born': 1815, 'nobel': False},
	{'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
]

import collections

Scientist = collections.namedtuple('Scientist', [
	'name',
	'field',
	'born',
	'nobel',
	])
