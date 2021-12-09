from termdep import Tree
from terms import Term
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
        self.assertEqual(tree.node_column, [1, 5, 8, 11, 16, 22])
        self.assertEqual(str(tree), pp_string)
        self.assertTrue(tree.is_projective())

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
        self.assertEqual(tree.node_column, [1, 6, 12, 18])
        self.assertEqual(str(tree), pp_string)
        self.assertTrue(tree.is_projective())

    def test_medium_text_tree_1(self):

        ex_tree = ((5, 0), (4, 1), (3, 2), (4, 3), (5, 4), (-1, 5))
        ex_sentence = "Jan Marie Wim lesen helfen sah"
        pp_string = \
            " ┏━━━━━━━━━━━━━━━━━━━━┳━━━━━O \n" + \
            " O    ┏━━━━━━━━━┳━━━━━O     ┆ \n" + \
            " ┆    O    ┏━━━━O     ┆     ┆ \n" + \
            " ┆    ┆    O    ┆     ┆     ┆ \n" + \
            " ┆    ┆    ┆    ┆     ┆     ┆ \n" + \
            "Jan Marie Wim lesen helfen sah\n"

        tree = Tree(ex_tree, -1, ex_sentence)
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.depth, 4)
        self.assertEqual(tree.text, ex_sentence)
        self.assertEqual(tree.node_column, [1, 6, 11, 16, 22, 28])
        self.assertEqual(str(tree), pp_string)
        self.assertTrue(tree.is_projective())

    def test_medium_text_tree_2(self):

        ex_tree = ((3, 0), (4, 1), (5, 2), (-1, 3), (3, 4), (4, 5))
        ex_sentence = "Jan Marie Wim zag helpen lezen"
        pp_string = \
            " ┏━━━━━━━━━━━━━O━━━━┓         \n" + \
            " O    ┏━━━━━━━━┿━━━━O━━━━━━┓  \n" + \
            " ┆    O    ┏━━━┿━━━━┿━━━━━━O  \n" + \
            " ┆    ┆    O   ┆    ┆      ┆  \n" + \
            " ┆    ┆    ┆   ┆    ┆      ┆  \n" + \
            "Jan Marie Wim zag helpen lezen\n"

        tree = Tree(ex_tree, -1, ex_sentence)
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.depth, 4)
        self.assertEqual(tree.text, ex_sentence)
        self.assertEqual(tree.node_column, [1, 6, 11, 15, 20, 27])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

    def test_easy_letter_tree(self):

        ex_tree = ((3, 0), (0, 1), (0, 2), (-1, 3), (5, 4), (3, 5))
        pp_string = \
            "┏━━━━━O━━━┓\n" + \
            "O━┳━┓ ┆ ┏━O\n" + \
            "┆ O O ┆ O ┆\n" + \
            "┆ ┆ ┆ ┆ ┆ ┆\n" + \
            "A B C D E F\n"

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.depth, 3)
        self.assertEqual(tree.text, "A B C D E F")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
        self.assertEqual(str(tree), pp_string)
        self.assertTrue(tree.is_projective())

    def test_easy_non_projective_tree(self):

        ex_tree = ((2, 0), (0, 1), (-1, 2), (0, 3), (5, 4), (2, 5))
        pp_string = \
            "┏━━━O━━━━━┓\n" + \
            "O━┳━┿━┓ ┏━O\n" + \
            "┆ O ┆ O O ┆\n" + \
            "┆ ┆ ┆ ┆ ┆ ┆\n" + \
            "A B C D E F\n"

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.depth, 3)
        self.assertEqual(tree.text, "A B C D E F")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

    def test_medium_non_projective_tree(self):

        ex_tree = ((2, 0), (0, 1), (-1, 2), (0, 3), (2, 4), (4, 5))
        pp_string = \
            "┏━━━O━━━┓  \n" + \
            "O━┳━┿━┓ O━┓\n" + \
            "┆ O ┆ O ┆ O\n" + \
            "┆ ┆ ┆ ┆ ┆ ┆\n" + \
            "A B C D E F\n"

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.depth, 3)
        self.assertEqual(tree.text, "A B C D E F")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

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

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.depth, 3)
        self.assertEqual(tree.text, "A B C D E F")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

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

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 6)
        self.assertEqual(tree.depth, 3)
        self.assertEqual(tree.text, "A B C D E F")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

    def test_hard_non_projective_tree_3(self):

        ex_tree = ((2, 0), (0, 1), (-1, 2), (4, 3),
                   (2, 4), (2, 5), (2, 6), (0, 7), (6, 8))
        pp_string = \
            "┏━━━O━━━┳━┳━┓    \n" + \
            "O━┳━┿━━━╋━╋━╋━┓  \n" + \
            "┆ O ┆   ┃ ┃ ┃ O  \n" + \
            "┆ ┆ ┆ ┏━O O O━┿━┓\n" + \
            "┆ ┆ ┆ O ┆ ┆ ┆ ┆ O\n" + \
            "┆ ┆ ┆ ┆ ┆ ┆ ┆ ┆ ┆\n" + \
            "A B C D E F G H I\n"

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 9)
        self.assertEqual(tree.depth, 3)
        self.assertEqual(tree.text, "A B C D E F G H I")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10, 12, 14, 16])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

    def test_hard_non_projective_tree_3(self):

        ex_tree = ((1, 0), (2, 1), (-1, 2), (4, 3),
                   (2, 4), (2, 5), (2, 6), (0, 7), (6, 8))
        pp_string = \
            "  ┏━O━━━┳━┳━┓    \n" + \
            "┏━O ┆   ┃ ┃ ┃    \n" + \
            "O━┿━┿━━━╋━╋━╋━┓  \n" + \
            "┆ ┆ ┆   ┃ ┃ ┃ O  \n" + \
            "┆ ┆ ┆ ┏━O O O━┿━┓\n" + \
            "┆ ┆ ┆ O ┆ ┆ ┆ ┆ O\n" + \
            "┆ ┆ ┆ ┆ ┆ ┆ ┆ ┆ ┆\n" + \
            "A B C D E F G H I\n"

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 9)
        self.assertEqual(tree.depth, 4)
        self.assertEqual(tree.text, "A B C D E F G H I")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10, 12, 14, 16])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

    def test_hard_non_projective_tree_4(self):

        ex_tree = ((1, 0), (2, 1), (-1, 2), (5, 3),
                   (7, 4), (2, 5), (2, 6), (0, 7), (6, 8))
        pp_string = \
            "  ┏━O━━━━━┳━┓    \n" + \
            "┏━O ┆     ┃ ┃    \n" + \
            "O━┿━┿━━━━━╋━╋━┓  \n" + \
            "┆ ┆ ┆   ┏━╋━╋━O  \n" + \
            "┆ ┆ ┆   O ┃ ┃ ┆  \n" + \
            "┆ ┆ ┆ ┏━┿━O O━┿━┓\n" + \
            "┆ ┆ ┆ O ┆ ┆ ┆ ┆ O\n" + \
            "┆ ┆ ┆ ┆ ┆ ┆ ┆ ┆ ┆\n" + \
            "A B C D E F G H I\n"

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 9)
        self.assertEqual(tree.depth, 5)
        self.assertEqual(tree.text, "A B C D E F G H I")
        self.assertEqual(tree.node_column, [0, 2, 4, 6, 8, 10, 12, 14, 16])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())

    def test_non_projectivity(self):

        ex_tree = ((3, 0), (3, 1), (0, 2), (-1, 3))
        pp_string = \
            "┏━┳━━━O\n" + \
            "O━╋━┓ ┆\n" + \
            "┆ ┃ O ┆\n" + \
            "┆ O ┆ ┆\n" + \
            "┆ ┆ ┆ ┆\n" + \
            "A B C D\n"

        tree = Tree(ex_tree)
        self.assertEqual(tree.size, 4)
        self.assertEqual(tree.depth, 3)
        self.assertEqual(tree.text, "A B C D")
        self.assertEqual(tree.node_column, [0, 2, 4, 6])
        self.assertEqual(str(tree), pp_string)
        self.assertFalse(tree.is_projective())


class TestTermPrint(unittest.TestCase):
    """Tests whether term pretty print works as expected. Terms do not necessarily make sense 
    mathematically but they still should be able to be printed
    """

    def _testCase(self, term, string):
        self.assertEqual(str(term), string)

    def test_easy_1(self):
        self._testCase(Term.inner([0, 1], []), '⟨01⟩')

    def test_easy_2(self):
        self._testCase(Term.inner([0, 1, 0], []), '⟨010⟩')

    def test_easy_3(self):
        self._testCase(Term.leaf(), '⟨0⟩')

    def test_easy_4(self):
        self._testCase(Term.inner([0, 1, 2, 3], []), '⟨0123⟩')

    def test_medium_1(self):
        self._testCase(
            Term.inner([[0, 1, 2, 1, 2], [3, 4, 5, 6]], [
                Term.leaf(),
                Term.leaf()
            ]),
            '⟨01212,3456⟩\n'
            '  ┌──┴──┐   \n'
            ' ⟨0⟩   ⟨0⟩  '
        )

    def test_medium_2(self):
        self._testCase(
            Term.inner([0, 1, 2, 3], [
                Term.inner([[0], [1]], []),
                Term.leaf(),
                Term.inner([[1], [0]], []),
            ]),
            '       ⟨0123⟩      \n'
            '  ┌──────┼──────┐  \n'
            '⟨0,1⟩   ⟨0⟩   ⟨1,0⟩'
        )

    def test_medium_3(self):
        self._testCase(
            Term.inner([0, 1, 2], [
                Term.leaf(),
                Term.inner([[0, 1, 2, 1, 2], [1, 2]],
                           [Term.leaf(), Term.leaf()])
            ]),
            '   ⟨012⟩        \n'
            ' ┌───┴────┐     \n'
            '⟨0⟩   ⟨01212,12⟩\n'
            '       ┌──┴──┐  \n'
            '      ⟨0⟩   ⟨0⟩ '
        )

    def test_medium_4(self):
        self._testCase(
            Term.inner([0, 1, 2, 1], [
                Term.inner([[0], [1]], [Term.leaf()]),
                Term.inner([0, 1], [Term.leaf()])
            ]),
            '   ⟨0121⟩   \n'
            '  ┌──┴───┐  \n'
            '⟨0,1⟩   ⟨01⟩\n'
            '  │      │  \n'
            ' ⟨0⟩    ⟨0⟩ '
        )

    def test_medium_5(self):
        self._testCase(
            Term.inner([0, 1, 2], [
                Term.inner([0, 1, 2], [
                    Term.inner([0, 1], [Term.leaf()]),
                    Term.leaf()
                ]),
                Term.leaf()
            ]),
            '       ⟨012⟩    \n'
            '    ┌────┴────┐ \n'
            '  ⟨012⟩      ⟨0⟩\n'
            ' ┌──┴───┐       \n'
            '⟨01⟩   ⟨0⟩      \n'
            ' │              \n'
            '⟨0⟩             '
        )

    def test_medium_6(self):
        self._testCase(
            Term.inner([0, 1, 2, 3], [
                Term.leaf(),
                Term.inner([1, 0, 2], [Term.leaf(), Term.leaf()]),
                Term.inner([0, 1, 2], [
                    Term.inner([1, 0, 1], [
                        Term.inner([[0], [1]], [Term.leaf()])
                    ]),
                    Term.leaf()
                ])
            ]),
            '          ⟨0123⟩             \n'
            ' ┌────────┬─┴──────────┐     \n'
            '⟨0⟩     ⟨102⟩        ⟨012⟩   \n'
            '       ┌──┴──┐      ┌──┴───┐ \n'
            '      ⟨0⟩   ⟨0⟩   ⟨101⟩   ⟨0⟩\n'
            '                    │        \n'
            '                  ⟨0,1⟩      \n'
            '                    │        \n'
            '                   ⟨0⟩       '
        )


if __name__ == '__main__':
    unittest.main()
