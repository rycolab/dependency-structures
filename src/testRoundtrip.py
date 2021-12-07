import unittest
from unittest.main import main
from algorithms import *
from termdep import Tree

# projective trees
proj = []
proj.append(((-1, 0), (0, 4), (1, 3), (3, 2), (4, 1)))
proj.append(((0, 1), (1, 2), (-1, 0)))
proj.append(((0, 1), (1, 2), (-1, 3), (3, 0)))
proj.append(((-1, 0), (5, 4), (1, 5), (0, 1), (2, 3), (4, 2)))
proj.append(((2, 1), (3, 2), (-1, 3), (3, 9), (3, 5),
             (5, 4), (5, 6), (6, 8), (8, 7), (1, 0)))
proj.append(((1, 2), (2, 3), (4, 1), (5, 4), (5, 7), (8, 5), (7, 6),
             (1, 0), (-1, 8), (8, 13), (13, 9), (10, 11), (13, 12), (13, 10)))
proj.append(((2, 1), (-1, 2), (2, 5), (2, 3), (1, 0), (5, 4)))
proj.append(((1, 0), (-1, 1), (1, 3), (3, 2), (1, 4), (4, 6), (6, 5)))

# non-projective trees
nonproj = []
nonproj.append(((1, 3), (2, 0), (0, 1), (-1, 2)))
nonproj.append(((1, 0), (-1, 1), (0, 2)))
nonproj.append(((-1, 0), (2, 3), (3, 1), (0, 2)))
nonproj.append(((2, 0), (-1, 1), (1, 2), (0, 3)))
nonproj.append(((0, 2), (1, 0), (-1, 1)))
nonproj.append(((0, 2), (3, 4), (-1, 0), (4, 1), (2, 3)))


class TestRoundTrip(unittest.TestCase):

	# TODO: fix the functions to take a tree as input
	# test whether two trees are the same
	def same(self, lst1, lst2):
		set1, set2 = set(lst1), set(lst2)
		for s in set1:
			self.assertIn(s, set2)
		for s in set2:
			self.assertIn(s, set1)

	# tests whether two trees are different
	def diff(self, lst1, lst2):
		def tmp(lst1, lst2):
			set1, set2 = set(lst1), set(lst2)
			for s in set1:
				if s not in set2:
					return True
			for s in set2:
				if s in set1:
					return True
			return False
		self.assertTrue(tmp(lst1, lst2))

	def test_proj(self):
		# projective unit test
		print()
		for tree1 in proj:
			print(Tree(tree1))
			term = encode_proj(tree1)
			tree2 = decode_proj(term)
			self.same(tree1, tree2)

	def test_non_proj(self):
		# non-projective unit test
		for tree1 in nonproj:
			term = encode_proj(tree1)
			tree2 = decode_proj(term)
			self.diff(tree1, tree2)

if __name__ == '__main__':
    unittest.main()