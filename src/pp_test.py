from src.termdep import Tree


def main():
    treeList = ((2, 0), (2, 1), (-1, 2), (5, 3), (5, 4), (2, 5), (2, 6))
    tree = Tree(treeList, -1)
    size = tree.size()
    print("size: " + str(size))

if __name__ == "__main__":
    main()
