import unittest
from terms import Term


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
