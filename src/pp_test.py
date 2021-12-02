from termdep import Tree
import unittest

class TestPrettyPrint(unittest.TestCase):

    def test_easy_text_tree_1(self):
      
      ex_tree = ((2, 0), (2, 1), (-1, 2), (5, 3), (5, 4), (2, 5))
      ex_sentence = "This is a text with words"
      pp_string = \
      " ┏━━━┳━━O━━━━━━━━━━━━━┓  \n" + \
      " O   O  ┆  ┏━━━━┳━━━━━O  \n" + \
      " ┆   ┆  ┆  O    O     ┆  \n" + \
      " ┆   ┆  ┆  ┆    ┆     ┆  \n" + \
      "This is a text with words\n"
      
      tree = Tree(ex_tree, -1, ex_sentence)
      self.assertEqual(tree.size, 6)
      self.assertEqual(tree.depth, 3)
      self.assertEqual(tree.text, ex_sentence)
      self.assertEqual(tree.node_column, [1,5,8,11,16,22])
      self.assertEqual(str(tree), pp_string)

    def test_easy_text_tree_2(self):

      ex_tree = ((1, 0), (-1, 1), (3, 2), (1, 3))
      ex_sentence = "Dan likes fresh fruit"
      pp_string = \
      " ┏━━━━O━━━━━━━━━━━┓  \n" + \
      " O    ┆     ┏━━━━━O  \n" + \
      " ┆    ┆     O     ┆  \n" + \
      " ┆    ┆     ┆     ┆  \n" + \
      "Dan likes fresh fruit\n"
      
      tree = Tree(ex_tree, -1, ex_sentence)
      self.assertEqual(tree.size, 4)
      self.assertEqual(tree.depth, 3)
      self.assertEqual(tree.text, ex_sentence)
      self.assertEqual(tree.node_column, [1,6,12,18])
      self.assertEqual(str(tree), pp_string)

    def test_easy_letter_tree(self):

      ex_tree = ((3, 0), (0, 1), (0, 2), (-1, 3), (5, 4), (3, 5))
      pp_string = \
      "┏━━━━━O━━━┓\n" + \
      "O━┳━┓ ┆ ┏━O\n" + \
      "┆ O O ┆ O ┆\n" + \
      "┆ ┆ ┆ ┆ ┆ ┆\n" + \
      "A B C D E F\n"

      tree = Tree(ex_tree, -1)
      self.assertEqual(tree.size, 6)
      self.assertEqual(tree.depth, 3)
      self.assertEqual(tree.text, "A B C D E F")
      self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
      self.assertEqual(str(tree), pp_string)

    def test_easy_non_projective_tree(self):

      ex_tree = ((2, 0), (0, 1), (-1, 2), (0, 3), (5, 4), (2, 5))
      pp_string = \
      "┏━━━O━━━━━┓\n" + \
      "O━┳━┿━┓ ┏━O\n" + \
      "┆ O ┆ O O ┆\n" + \
      "┆ ┆ ┆ ┆ ┆ ┆\n" + \
      "A B C D E F\n"

      tree = Tree(ex_tree, -1)
      self.assertEqual(tree.size, 6)
      self.assertEqual(tree.depth, 3)
      self.assertEqual(tree.text, "A B C D E F")
      self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
      self.assertEqual(str(tree), pp_string)

    def test_medium_non_projective_tree(self):

      ex_tree = ((2, 0), (0, 1), (-1, 2), (0, 3), (2, 4), (4, 5))
      pp_string = \
      "┏━━━O━━━┓  \n" + \
      "O━┳━┿━┓ O━┓\n" + \
      "┆ O ┆ O ┆ O\n" + \
      "┆ ┆ ┆ ┆ ┆ ┆\n" + \
      "A B C D E F\n"

      tree = Tree(ex_tree, -1)
      self.assertEqual(tree.size, 6)
      self.assertEqual(tree.depth, 3)
      self.assertEqual(tree.text, "A B C D E F")
      self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
      self.assertEqual(str(tree), pp_string)

    def test_hard_non_projective_tree_1(self):

      ex_tree = ((2, 0), (0, 1), (-1, 2), (5, 3), (0, 4), (2, 5))
      pp_string = \
      "┏━━━O━━━━━┓\n" + \
      "O━┳━┿━━━┓ ┃\n" + \
      "┆ O ┆   O ┃\n" + \
      "┆ ┆ ┆ ┏━┿━O\n" + \
      "┆ ┆ ┆ O ┆ ┆\n" + \
      "┆ ┆ ┆ ┆ ┆ ┆\n" + \
      "A B C D E F\n"

      tree = Tree(ex_tree, -1)
      self.assertEqual(tree.size, 6)
      self.assertEqual(tree.depth, 3)
      self.assertEqual(tree.text, "A B C D E F")
      self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
      self.assertEqual(str(tree), pp_string)

    def test_hard_non_projective_tree_2(self):

      ex_tree = ((2, 0), (0, 1), (-1, 2), (4, 3), (2, 4), (0, 5))
      pp_string = \
      "┏━━━O━━━┓  \n" + \
      "O━┳━┿━━━╋━┓\n" + \
      "┆ O ┆   ┃ O\n" + \
      "┆ ┆ ┆ ┏━O ┆\n" + \
      "┆ ┆ ┆ O ┆ ┆\n" + \
      "┆ ┆ ┆ ┆ ┆ ┆\n" + \
      "A B C D E F\n"

      tree = Tree(ex_tree, -1)
      print("from here:")
      print(tree)
      self.assertEqual(tree.size, 6)
      self.assertEqual(tree.depth, 3)
      self.assertEqual(tree.text, "A B C D E F")
      self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
      self.assertEqual(str(tree), pp_string)

if __name__ == '__main__':
    unittest.main()