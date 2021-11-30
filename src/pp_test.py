from termdep import Tree


def main():
    """
    example tree:
    ((2, 0), (2, 1), (-1, 2), (5, 3), (5, 4), (2, 5), (2, 6))
      -1
       |
       2 --\ 
     / | \ |
     0 1 5 6
        / \ 
        3 4
    """
    tree_list = ((2, 0), (2, 1), (-1, 2), (5, 3), (5, 4), (2, 5), (2, 6))
    tree = Tree(tree_list, -1, "This is a text with words.")
    size = tree.size()
    depth = tree.depth()
    matrix = tree.generate_matrix()
    print("vertices: " + str(size))
    print("depth:    " + str(depth))
    print("test:     " + tree.text)
    print("matrix:   " + str(matrix))
    print("matrix pp:\n" + Tree.string_of_matrix(matrix))


if __name__ == "__main__":
    main()
