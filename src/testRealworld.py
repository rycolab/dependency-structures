from typing import List
import unittest
from unittest.main import main
from algorithms import *
from termdep import TreeBank
import os

# NOTE: These are not actually tests.
# I'm just abusing the testing framework to have a convenient way of executing code.
# We compute some statistics about real treebanks.


class TestRealworld(unittest.TestCase):
    def importFile(self, path: str):
        abs_path = os.path.abspath(path)
        tree_bank = TreeBank(abs_path)
        trees = [Tree(t) for t in tree_bank.generator()]
        return trees

    def statistics(self, path: str):
        trees = self.importFile(path)
        n_projective = 0
        n_nonprojective = 0
        for tree in trees:
            # print(tree)
            if is_projective(tree):
                n_projective += 1
                # print("projective")
            else:
                n_nonprojective += 1
                # print("non-prejective")

        print()  # newline to get below dot printed by testing framework
        filename = os.path.basename(path)
        print(os.path.splitext(filename)[0])
        print("entries:        " + str(n_projective + n_nonprojective))
        print("projective:     " + str(n_projective))
        print("non-projective: " + str(n_nonprojective))
        fraction = n_projective/(n_projective+n_nonprojective)
        percentage = fraction * 100
        print("fraction      : {:.2f}%".format(percentage))

    def test_Danish_DDT(self):
        # book says: 84.95% projective, but this is on a different data set
        # (this one is from 2015, the book is from 2010)
        self.statistics("data/UD_Danish-DDT/da_ddt-ud-dev.conllu")

    def test_English_ParTut(self):
        self.statistics("data/UD_English-ParTUT/en_partut-ud-dev.conllu")

    def test_German_GSD(self):
        self.statistics("data/UD_German-GSD/de_gsd-ud-dev.conllu")

    def test_Swiss_German_UZH(self):
        self.statistics("data/UD_Swiss_German-UZH/gsw_uzh-ud-test.conllu")


if __name__ == '__main__':
    unittest.main()
