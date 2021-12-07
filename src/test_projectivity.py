import unittest
import argparse
from algorithms import *
from termdep import TreeBank


# helper functions
def same(lst1, lst2):
	set1, set2 = set(lst1), set(lst2)
	for s in set1:
		assert s in set2
	for s in set2:
		assert s in set1


def diff(lst1, lst2):
	def tmp(lst1, lst2):
		set1, set2 = set(lst1), set(lst2)
		for s in set1:
			if s not in set2:
				return True
		for s in set2:
			if s in set1:
				return True
		return False
	assert tmp(lst1, lst2)


class Projectivity(unittest.TestCase):

	def test_naive(self):
		pass


# test code
parser = argparse.ArgumentParser(description='Parse Dependency Parses as Terms')
parser.add_argument('--trees')
args = parser.parse_args()

proj, total = 0, 0

tb = TreeBank(args.trees)
gen = tb.generator()

for count, tree1 in enumerate(gen):
	term = encode_proj(tree1)
	tree2 = decode_proj(term)
	#print(tree1)
	if is_projective_naive(tree1):
		same(tree1, tree2)
		proj += 1
	else:
		diff(tree1, tree2)
	total += 1

print(float(proj) / total)
