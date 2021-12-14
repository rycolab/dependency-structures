from typing import List
import unittest
from unittest.main import main
from algorithms import *
from termdep import TreeBank
import os


class TestRealworld(unittest.TestCase):
    def importFile(self, path: str):
        abs_path = os.path.abspath(path)
        tree_bank = TreeBank(abs_path)
        trees = [Tree(t) for t in tree_bank.generator()]
        return trees

    def test_German_GSD(self):
        trees = self.importFile("data/UD_German-GSD/de_gsd-ud-dev.conllu")
        for tree in trees:
            print(tree)

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


if __name__ == '__main__':
    unittest.main()
