import pyconll


class Tree(object):
    def __init__(self, tree: "tuple[tuple[int,int], ...]", root: int, text: str = ""):
        """ `text` is used for pretty printing only. """
        self.tree = tree
        self.root = root
        # text preprocessesing and checks
        text = text.strip('. \t')
        if text == "":
            # set "A B C ...", one letter per node
            text = " ".join([chr(i) for i in range(65, 65+self.size())])
        words = text.count(" ") + 1
        if words != self.size():
            raise ValueError("Graph and text don't fit together.")
        self.text = text

    @staticmethod
    def string_of_matrix(matrix: "list[list[str]]") -> str:
        # rows: two per node, one for text
        # return (*matrix)
        # return matrix
        string = ""
        for row in matrix:
            string += ''.join(row)
            string += "\n"
        return string

    def generate_matrix(self) -> "list[list[str]]":
        """
        Generate a suitable 2D matrix for pretty printing.
        `text` is already inserted as last row.
        """
        # rows: two per node, one for text
        rows = 2 * self.depth() + 1
        columns = len(self.text)
        matrix = [['.' for _ in range(columns)] for _ in range(rows)]
        matrix[rows-1] = self.text
        return matrix

    def size(self) -> int:
        """
        Size without artificial root.
        Works, because every vertex only has one inbound edge.
        """
        return len(self.tree) - 1

    def depth(self) -> int:
        """
        Return the depth of the tree (excluding artificial root node).
        Warning: Due to list representation of edges, this is slow.
        """
        res = self.__dfs(self.root)
        return res - 1

    def __dfs(self, root: int) -> int:
        """ Warning: Due to list representation of edges, this is slow. """
        max_depth = 0
        for pair in self.tree:
            if pair[0] == root:
                partial_depth = self.__dfs(pair[1])
                max_depth = max(max_depth, partial_depth)
        return max_depth + 1

    def __str__(self):
        """ TODO: add proper tree visualization here """
        return str(self.tree)

    def __repr__(self):
        """ TODO: add proper tree visualization here """
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
