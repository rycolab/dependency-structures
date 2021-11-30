import pyconll
import argparse


class Tree(object):

    def __init__(self, tree, root):
        self.tree = tree
        self.root = root

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
            
            root = None
            broken = False
            dep = []

            for i, word in enumerate(sentence):

                if word.head is None:
                    broken = True
                    break

                head = int(word.head)-1
                dep.append((head, i))

                if head == -1:
                    root = dep

            assert root is not None
            dep = Tree(tuple(dep), root)

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