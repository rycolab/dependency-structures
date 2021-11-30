import pyconll
import argparse


class Tree(object):

    def __init__(self, tree):
        self.tree = tree

    def __str__(self):
        """ TODO: add proper tree visualization here """
        return str(self.tree)

    def __repr__(self):
        """ TOOD: add proper tree visualization here """
        return str(self)


class TreeBank(object):

    def __init__(self, fin):
        self.trees = pyconll.load_from_file(fin)

    def generator(self):
        """
        Returns trees as a tuple of pairs, e.g., 
        ((2, 0), (2, 1), (-1, 2), (5, 3), (5, 4), (2, 5), (2, 6)),
        The ordering of the pairs does not matter. 
        -1 is a distinguished integer for the root 
        """
        for n, sentence in enumerate(self.trees):
            
            broken, dep = False, []
            for i, word in enumerate(sentence):
                if word.head is None:
                    broken = True
                    break
                dep.append((int(word.head)-1, i))
            dep = Tree(tuple(dep))

            if broken:
                continue

            yield dep


# test code
parser = argparse.ArgumentParser(description='Parse Dependency Parses as Terms')
parser.add_argument('--trees')
args = parser.parse_args()

tb = TreeBank(args.trees)
gen = tb.generator()
for x in gen:
    print(x)      
    input()