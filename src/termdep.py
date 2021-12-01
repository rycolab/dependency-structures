# from _typeshed import Self
# from numpy.char import array
from numpy.lib.function_base import append
import pyconll
import numpy as np


class Tree(object):

    sym_tbl = {
        "empty":                    ' ',
        "node":                     'O',
        "h_edge":                   '━',
        "v_edge":                   '┃',
        "l_corner":                 '┏',
        "t_intersection":           '┳',
        "r_corner":                 '┓',
        "projection":               '┆',
        "projection_intersection":  '┿'
    }

    def __init__(self, tree, root, text=None):
        """ `text` is used for pretty printing only. """
        self.tree = tree
        self.root = root

        # text preprocessesing and checks
        if text is None:  # If no text is given, set "A B C ...", one letter per node
            text = " ".join([chr(i) for i in range(65, 65+self.size)])
        self.text = text.strip('. \t')

        # Make sure the text and node amount is equal
        words = self.text.count(" ") + 1
        if words != self.size:
            raise ValueError("Graph and text don't fit together. " +
                             f"Expected {words} nodes but got {self.size}")

        self.node_column = []
        acc = -1  # start at -1 because index starts at 0, and ceil gives at least 1
        for word in self.text.split(' '):
            self.node_column.append(int(acc + np.ceil(len(word)/2)))
            acc += len(word) + 1

    def _generate_matrix(self) -> "np.array":
        """
        Generate a suitable 2D matrix for pretty printing.
        `text` is already inserted as last row.
        """
        depth = self.depth
        # Get tree part of the matrix in np.array form
        m, l, r, c = self._tree_matrix(depth)

        # make final matrix
        rows = depth + 2
        columns = len(self.text)
        matrix = np.full((rows, columns), self.sym_tbl["empty"])

        # insert top part of matrix with tree
        for i in range(depth):
            matrix[i][l:r] = m[i][0:r-l]

        # draw projection lines
        matrix = self._add_projection_lines(matrix, c, depth)

        # add text at the bottom
        matrix[-1] = np.array(list(self.text))

        return matrix

    @property
    def size(self) -> int:
        """
        Gives number of edges in tree
        Works, because every vertex only has one inbound edge.
        """
        return len(self.tree)

    @property
    def depth(self) -> int:
        """
        Return the depth of the tree (excluding artificial root node).
        Warning: Due to list representation of edges, this is slow.
        """
        res = self.__dfs(self.root)
        return res - 1

    def __dfs(self, root) -> int:
        """
        Internal method that gives depth starting from root node.
        Warning: Due to list representation of edges, this is slow. """
        max_depth = 0
        for parent, node in self.tree:
            if parent == root:
                partial_depth = self.__dfs(node)
                max_depth = max(max_depth, partial_depth)
        return max_depth + 1

    def _tree_matrix(self, depth, root=None):
        """
        This function uses recursion to build each subtree from a given node.
        If no node is given, it is assumed that the root node is requested.
        This makes a matrix slightly bigger than it's children, checks if it is
        projective, and then returns a composite of the subtrees with the added symbols
        """

        # If no root is specified, get first node with parent self.root
        if root is None:
            root = [node for node in self.tree if node[0] == self.root][0]
        # Get children of node
        children = [node for node in self.tree if node[0] == root[1]]

        # get root position
        root_pos = self.node_column[root[1]]

        # check depth value
        if depth == 0:
            raise ValueError("Depth has wrong value")

        # If there are no children, then it is a leaf node
        if len(children) == 0:
            # Generate node with prejectivity lines at correct depth
            matrix = np.full((depth, 1), '┆')
            matrix[0][0] = self.sym_tbl["node"]
            return (
                matrix,
                self.node_column[root[1]],
                self.node_column[root[1]] + 1,
                [(root[1], 0)])

        # get matrices of children and get columns of children
        children_arr = [self._tree_matrix(depth - 1, node)
                        for node in children]
        children_columns = [self.node_column[node] for _, node in children]

        # check that children fit side to side
        left_most = min(root_pos, children_arr[0][1])
        right_most = 0
        for _, left, right, _ in children_arr:
            if left < right_most:
                raise ValueError(
                    "Only projetive trees have been implemented yet")
            right_most = right
        right_most = max(root_pos + 1, right_most)

        # create return matrix
        matrix = np.full((depth, int(right_most-left_most)),
                         self.sym_tbl["empty"])

        # put children subtrees into matrix
        for m, l, r, _ in children_arr:
            for i in range(depth - 1):
                local_left = int(l - left_most)
                matrix[i+1][local_left:int(local_left + r-l)
                            ] = m[i][0:int(r-l)]

        # add all children in subtrees to an array
        all_children = []
        for _, l, _, c in children_arr:
            for node, node_row in c:
                all_children.append((node, node_row + 1))

        # connect nodes:
        matrix[0] = np.full(int(right_most-left_most),
                            self.sym_tbl["h_edge"])  # horizontal lines
        for col in children_columns:
            # node connectors
            matrix[0][col - left_most] = self.sym_tbl["t_intersection"]
        if children_columns[0] < root_pos:
            # leftmost connector
            matrix[0][children_columns[0] -
                      left_most] = self.sym_tbl["l_corner"]
        if children_columns[-1] > root_pos:
            # rightmost connector
            matrix[0][children_columns[-1] -
                      left_most] = self.sym_tbl["r_corner"]

        # put in node
        matrix[0][root_pos-left_most] = self.sym_tbl["node"]

        return matrix, left_most, right_most, [(root[1], 0)] + all_children

    def _add_projection_lines(self, matrix, nodes, depth):
        """
        Add projection lines for each node
        """
        # helper function to convert projection lines
        projection_lines = {
            self.sym_tbl["empty"]:      self.sym_tbl["projection"],
            self.sym_tbl["projection"]: self.sym_tbl["projection"],
            self.sym_tbl["h_edge"]:     self.sym_tbl["projection_intersection"]
        }

        def add_proj_line(row, col):
            matrix[row][col] = projection_lines[matrix[row][col]]

        # add projection lines downwards from each node
        for node, row in nodes:
            for i in range(row+1, depth):
                add_proj_line(i, self.node_column[node])

        # add buffer row of projection lines
        matrix[-2][self.node_column] = self.sym_tbl["projection"]

        return matrix

    def __str__(self):
        """
        Generates a string from a matrix with every row as a line
        """
        string = ""
        matrix = self._generate_matrix()
        for row in matrix:
            string += ''.join(row) + "\n"
        return string

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
