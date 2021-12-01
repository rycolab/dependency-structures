# from _typeshed import Self
# from numpy.char import array
from numpy.lib.function_base import append
import pyconll
import numpy as np


class Tree(object):
    def __init__(self, tree: "tuple[tuple[int,int], ...]", root: int, text: str = None):
        """ `text` is used for pretty printing only. """
        self.tree = tree
        self.root = root

        # text preprocessesing and checks
        if text is None:
            # set "A B C ...", one letter per node
            text = " ".join([chr(i) for i in range(65, 65+self.size())])
        text = text.strip('. \t')

        # Make sure the text and node amount is equal
        words = text.count(" ") + 1
        if words != self.size():
            raise ValueError("Graph and text don't fit together.")
        
        self.node_column = []
        acc = -1 # start at -1 because index starts at 0, and ceil gives at least 1
        for word in text.split(' '):
            self.node_column.append(int(acc + np.ceil( len(word)/2 )))
            acc += len(word) + 1
        self.text = text

    @staticmethod
    def string_of_matrix(matrix: "np.array") -> str:
        """
        Generates a string from a matrix with every row as a line
        """
        string = ""
        for row in matrix[:]:
            string += ''.join(row) + "\n"
        return string

    def generate_matrix(self) -> "np.array":
        """
        Generate a suitable 2D matrix for pretty printing.
        `text` is already inserted as last row.
        """
        # rows: two per node, one for text
        depth = self.depth()
        m, l, r = self._tree_arr(depth)
        rows = depth + 2
        columns = len(self.text)
        matrix = np.full((rows, columns), ' ')
        for i in range(depth):
            matrix[i][l:r] = m[i][0:r-l]
        matrix[-2] = np.array(["┆" if c in self.node_column else " " for c in range(columns)])
        matrix[-1] = np.array(list(self.text))
        return matrix

    def size(self) -> int:
        """
        Works, because every vertex only has one inbound edge.
        """
        return len(self.tree)

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
        for parent, node in self.tree:
            if parent == root:
                partial_depth = self.__dfs(node)
                max_depth = max(max_depth, partial_depth)
        return max_depth + 1

    def _tree_arr(self, depth, root=None):
        """
        This function uses recursion to build each subtree from a given node.
        If no node is given, it is assumed that the root node is requested.
        This makes a matrix slightly bigger than it's children, checks if it is
        projective, and then returns a composite of the subtrees with the added symbols
        """
        # If no root is specified, get first node with parent -1 (root)
        if root is None: 
            root = [node for node in self.tree if node[0] == -1 ][0] 
        children = [node for node in self.tree if node[0] == root[1]]

        # get root position
        root_pos = self.node_column[root[1]]

        # check depth value
        if depth == 0:
            raise ValueError("Depth has wrong value")

        # If there are no children, then it is a leaf node
        if len(children) == 0: 
            matrix = np.full((depth, 1), '┆')
            matrix[0][0] = 'O'
            return matrix, self.node_column[root[1]], self.node_column[root[1]] + 1

        # get matrices of children and get columns of children
        children_arr = [self._tree_arr(depth - 1, node) for node in children]
        children_columns = [self.node_column[node] for _, node in children]

        # check that children fit side to side
        left_most = min(root_pos, children_arr[0][1])
        right_most = 0
        for _, left, right in children_arr:
            if left < right_most:
                raise ValueError("Only projetive trees have been implemented yet")
            right_most = right
        right_most = max(root_pos + 1, right_most)

        # create return matrix
        matrix = np.full((depth, int(right_most-left_most)), ' ')

        # put children subtrees into matrix
        for m, l, r in children_arr:
            for i in range(depth - 1):
                local_left = int(l - left_most)
                matrix[i+1][local_left:int(local_left + r-l)] = m[i][0:int(r-l)]

        # connect nodes:
        matrix[0] = np.full(int(right_most-left_most), '━') # horizontal lines
        for col in children_columns:
            matrix[0][col - left_most] = '┳' # node connectors
        if children_columns[0] < root_pos:
            matrix[0][children_columns[0] - left_most] = '┏' # leftmost connector
        if children_columns[-1] > root_pos:
            matrix[0][children_columns[-1] - left_most] = '┓' # rightmost connector

        # projection lines:
        for r in range(depth):
            matrix[r][root_pos-left_most] = '┆'
        
        # put in node
        matrix[0][root_pos-left_most] = 'O'

        return matrix, left_most, right_most

    def __str__(self):
        return self.string_of_matrix(self.generate_matrix())

    def __repr__(self):
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
