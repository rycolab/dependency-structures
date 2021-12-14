from __future__ import annotations
from typing import Literal
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from terms import Term


class _DisplayNode:
    blank = ' '

    @staticmethod
    def leaf(label: str, depth=0) -> _DisplayNode:
        n = len(label)
        return _DisplayNode(label, (n - 1) // 2, 0, n, depth)

    @property
    def labelLeft(self):
        n = len(self.label)
        return self.m - (n - 1) // 2

    @property
    def labelRight(self):
        n = len(self.label)
        return self.m + n - ((n - 1) // 2)

    @property
    def isLeaf(self):
        return len(self.children) == 0

    @property
    def isInner(self):
        return not self.isLeaf

    def __init__(self, label: str, m: int, l: int, r: int, d: int, children: list[_DisplayNode] = []):
        self.label = label
        self.m = m
        self.l = l
        self.r = r
        self.d = d
        self.children = children

    def getHeight(self):
        return self.d + 1 if self.isLeaf else max([x.getHeight() for x in self.children])

    def shiftRight(self, amt: int):
        if amt <= 0:
            return self.r
        self.l += amt
        self.m += amt
        self.r += amt
        if len(self.children) == 0:
            return self.r
        else:
            return max(self.r, *[child.shiftRight(amt) for child in self.children])

    def __str__(self) -> str:
        sym = {'h': '─', 'v': '│', 'bl': '┐',
               'br': '┌', 'th': '┴', 'bh': '┬', 'vh': '┼'}
        h = self.getHeight()
        canvas = [[self.blank] * self.r for _ in range(h * 2 - 1)]

        def drawBrace(d: int, top: int, bots: list[int]):
            row = canvas[d * 2 + 1]
            l = min(top, *bots)
            r = max(top, *bots)
            if l == r:
                row[l] = sym['v']
            else:
                row[l:r+1] = sym['br'] + sym['h'] * \
                    (r - l - 1) + sym['bl']
                row[top] = sym['th']
                for i in bots[1:-1]:
                    row[i] = sym['vh'] if i == top else sym['bh']

        def drawNode(node: _DisplayNode):
            # Draw node label
            canvas[node.d * 2][node.labelLeft:node.labelRight] = node.label
            if node.isLeaf:
                return
            # Draw brace
            childMs = [x.m for x in node.children]
            drawBrace(node.d, node.m, childMs)
            for child in node.children:
                drawNode(child)

        drawNode(self)
        return '\n'.join([''.join(row) for row in canvas])


class TermPrettyPrinter:
    def __init__(self, term, style: Literal["vTree", "hTree"] = "vTree") -> None:
        self.term = term
        self.style = style
        self.methods = {
            'vTree': self.vTree,
            'hTree': self.hTree
        }

    @property
    def method(self):
        return self.methods[self.style]

    def string(self):
        return self.method()

    def print(self):
        print(self.string())

    def hTree(self) -> str:
        """Converts the term to a string representing a tree similar to bash's `tree` command
        """
        def aux(term: Term, level: int, lastSibling: bool):
            nodeStr = str(term.oa)
            childrenStr = ''
            for i, child in enumerate(term.lst):
                last = i == len(term) - 1
                prefix = ('    ' if lastSibling else '│   ') * level
                connector = '└── ' if last else '├── '
                childrenStr += '\n' + prefix + \
                    connector + aux(child, level + 1, last)
            return nodeStr + childrenStr
        return aux(self.term, 0, True)

    def vTree(self) -> str:
        def buildDisplayTree(term: Term, depth=0) -> _DisplayNode:
            lbl = str(term.oa)
            # Leaf node
            if term.isLeaf():
                return _DisplayNode.leaf(lbl, depth)
            # Inner node
            children = [buildDisplayTree(x, depth + 1) for x in term.lst]
            # Put children next to eachother
            spacing = 3
            r = 0
            for i, child in enumerate(children):
                r = child.shiftRight(r + spacing * (i > 0))
            # Update parent midpoint
            m1 = (children[0].m + children[-1].m) // 2
            m2 = (len(lbl) - 1) // 2
            m = max(m1, m2)
            # Shift children if necessary (if children width < parent width)
            shamt = max(0, m2 - m1)
            for child in children:
                child.shiftRight(shamt)
            # Get correct r-value
            r = max(len(lbl), r)
            return _DisplayNode(lbl, m, 0, r, depth, children)

        displayTree = buildDisplayTree(self.term)

        return str(displayTree)
