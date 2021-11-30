import pyconll

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

    def __len__(self):
        return len(self.tree)

    def __getitem__(self, i):
        return self.tree[i]


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

            dep = Tree(tuple(dep), root)

            if broken or root is None:
                continue

            yield dep

    
    input()