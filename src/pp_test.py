from termdep import Tree
import unittest

class TestPrettyPrint(unittest.TestCase):

    def test_easy_tree(self):
      
      ex_tree = ((2, 0), (2, 1), (-1, 2), (5, 3), (5, 4), (2, 5))
      ex_sentence = "This is a text with words"
      pp_string = \
      " ┏━━━┳━━O━━━━━━━━━━━━━┓  \n" + \
      " O   O  ┆  ┏━━━━┳━━━━━O  \n" + \
      " ┆   ┆  ┆  O    O     ┆  \n" + \
      " ┆   ┆  ┆  ┆    ┆     ┆  \n" + \
      "This is a text with words\n"
      
      tree = Tree(ex_tree, -1, ex_sentence)
      size = tree.size()
      depth = tree.depth()
      pp_matrix = Tree.string_of_matrix(tree.generate_matrix())
      self.assertEqual(size, 6)
      self.assertEqual(depth, 3)
      self.assertEqual(ex_sentence, tree.text)
      self.assertEqual([1,5,8,11,16,22], tree.node_column)
      self.assertEqual(pp_string, pp_matrix)

if __name__ == '__main__':
    unittest.main()