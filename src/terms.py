from __future__ import annotations
from os import chdir
from typing import Iterable, List, Optional, Union
from functools import reduce


class OrderAnnotation(object):

    @staticmethod
    def leaf():
        """Creates an order annotation with just the root in the order list

        Returns:
            OrderAnnotation: New order annotation of block-degree 1
        """
        return OrderAnnotation([[0]])

    @staticmethod
    def deg1(*order: int) -> OrderAnnotation:
        """Create an order annotation of block-degree 1

        Returns:
            OrderAnnotation
        """
        return OrderAnnotation([[*order]])

    @staticmethod
    def degK(*orders: List[int]) -> OrderAnnotation:
        """Create an order annotation of arbitrary block-degree. Orders are passed as lists of
        orders for each block.

        Returns:
            OrderAnnotation
        """
        return OrderAnnotation([*orders])

    def __init__(self, orders: List[List[int]]):
        """Creates a new instance of an order annotation with given orders.
        Order annotations are represented as a list of lists, where each list contains the order
        for the given block.

        You can use the factory methods `leaf`, `deg1` and `degK` to improve legibility.

        Args:
            orders (List[List[int]]): List of orders for each block
        """
        self.orders = orders

    def __str__(self):
        return '⟨' + ','.join([''.join([str(x) for x in order]) for order in self.orders]) + '⟩'

    def __repr__(self):
        return str(self)

    def __getitem__(self, i):
        return self.orders[i]


class Term(object):

    @staticmethod
    def inner(oaList: list, lst: List[Term]) -> Term:
        oa = None
        if all([isinstance(x, list) for x in oaList]):
            # Block-degree k
            oa = OrderAnnotation(oaList)
        elif all([isinstance(x, int) for x in oaList]):
            # Block-degree 1
            oa = OrderAnnotation([oaList])
        else:
            raise TypeError(
                'Invalid type for order annotation list: ' + str(type(oaList)))
        return Term(oa, lst)

    @staticmethod
    def leaf() -> Term:
        return Term(OrderAnnotation.leaf(), [])

    def __init__(self, oa: OrderAnnotation, lst: List[Term]):
        # an order annotation serves as the functor of the term
        self.oa = oa
        # list of the children
        self.lst = lst

    def isLeaf(self):
        return len(self.lst) == 0

    def toString1(self):
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
        return aux(self, 0, True)

    def toString2(self):
        """Converts the term to a string representing a tree similar to Kuhlmann's representation in
        his book
        """
        def maxLineWidth(s: str):
            return max(map(len, s.splitlines()))

        def concatLines(s1: str, s2: str, pad=0):
            lines1 = s1.splitlines()
            lines2 = s2.splitlines()
            lwidth = max(map(len, lines1)) if len(lines1) > 0 else 0
            res = []
            for i in range(max(len(lines1), len(lines2))):
                line1 = lines1[i] if i < len(lines1) else ''
                line2 = lines2[i] if i < len(lines2) else ''
                res.append(line1.ljust(lwidth + pad, ' ') + line2)
            return '\n'.join(res)

        def concatLinesMany(strings: Iterable[str], pad=0):
            start = True

            def f(l, r):
                nonlocal start
                res = concatLines(l, r, 0 if start else pad)
                start = False
                return res

            return reduce(f, strings, '')

        def aux(term: Term):
            node = str(term.oa)
            if term.isLeaf():
                # Leaf node
                return node
            # Inner node
            pad = 2
            children = map(aux, term.lst)
            cstr = concatLinesMany(children, pad)
            maxchildwidth = maxLineWidth(cstr)
            lpad = (maxLineWidth(cstr) - len(node)) // 2
            print(f'{term.oa}: maxchildwidth: {maxchildwidth}')
            return (' ' * lpad) + node + '\n\n' + cstr
        return aux(self)

    def toString3(self):
        class Node:
            blank = ' '

            @staticmethod
            def leaf(label: str, depth=0) -> Node:
                n = len(label)
                return Node(label, n // 2, 0, n, depth)

            @property
            def lblIndent(self):
                return self.m - len(self.lbl) // 2

            def __init__(self, lbl: str, m: int, l: int, r: int, d: int, children: List[Node] = []):
                self.lbl = lbl
                self.m = m
                self.l = l
                self.r = r
                self.d = d
                self.children = children

            def getDepth(self):
                if len(self.children) == 0:
                    return self.d
                else:
                    return max([x.getDepth() for x in self.children])

            def shiftRight(self, amt: int):
                self.l += amt
                self.m += amt
                self.r += amt
                if len(self.children) == 0:
                    return self.r
                else:
                    return max(self.r, *[child.shiftRight(amt) for child in self.children])

            def __str__(self) -> str:
                def aux(node: Node, level: int = 0):
                    childrenStr = ''
                    indent = '  ' * level * 2
                    if len(node.children) > 0:
                        childrenStr = (
                            '{indent}  children = [\n' +
                            '{children}\n' +
                            '{indent}  ]\n'
                        ).format(
                            indent=indent, children=",\n".join(
                                map(lambda x: aux(x, level + 1), node.children))
                        )
                    else:
                        childrenStr = '{indent}  children = []\n'.format(
                            indent=indent)
                    return ((
                        '{indent}{lbl} {{\n' +
                        '{indent}  l = {l}, r = {r}, m = {m}, d = {d}\n' +
                        '{children}' +
                        '{indent}}}')
                        .format(
                            indent=indent,
                            lbl=node.lbl,
                            l=node.l, r=node.r, m=node.m, d=node.d,
                            children=childrenStr
                    ))
                return aux(self) + '\n'

        def buildDisplayTree(term: Term, depth=0) -> Node:
            lbl = str(term.oa)
            if term.isLeaf():
                # Leaf node
                return Node.leaf(lbl, depth)
            # Inner node
            # Put children side by side
            children = list(
                map(lambda x: buildDisplayTree(x, depth + 1), term.lst))
            r = 0
            spacing = 2
            for child in children:
                r = child.shiftRight(r) + spacing
            # Adjust r in case the label is wider than the children
            r = max(r, len(lbl))
            m = r // 2
            return Node(lbl, m, 0, r, depth, children)

        def displayTreeToString(root: Node, depth: int) -> str:
            blank = ' '
            sym = {'blank': blank, 'h': '─', 'v': '│', 'tl': '┘', 'tr': '└', 'bl': '┐',
                   'br': '┌', 'vl': '┤', 'vr': '├', 'th': '┴', 'bh': '┬', 'vh': '┼'}

            class Brace:
                def __init__(self, d, top: int, bots: list[int]) -> None:
                    self.d = d
                    self.top = top
                    self.bots = bots

                def draw(self, canvas: list[list[str]]):
                    row = canvas[self.d * 2 + 1]
                    imin = min([self.top, *self.bots])
                    imax = max([self.top, *self.bots])
                    fill = sym['br'] + sym['h'] * (imax - imin - 1) + sym['bl']
                    row[imin:imax+1] = fill
                    row[self.top] = sym['th']
                    for i in self.bots[1:-1]:
                        row[i] = sym['bh']

            queue: list[Node] = [root]
            canvas: list[list[str]] = []
            for _ in range((depth + 1) * 2):
                canvas.append([blank] * root.r)
            while queue:
                node = queue.pop(0)
                n = len(node.lbl)
                lblleft = node.m - n // 2
                lblright = node.m + n - (n // 2)
                # Draw node label
                canvas[node.d * 2][lblleft:lblright] = list(node.lbl)
                # Draw brace
                if len(node.children) > 0:
                    brace = Brace(node.d, node.m, [x.m for x in node.children])
                    brace.draw(canvas)
                queue += node.children
            return '\n'.join([''.join(row) for row in canvas])

        displayTree = buildDisplayTree(self)
        # displayTree = Node('⟨01212,12⟩', 4, 0, 10, 0)
        # n0 = Node('⟨012⟩', 2, 0, 5, 0)
        # n1 = Node('⟨0⟩', 1, 0, 3, 0)
        # n2 = Node('⟨01212,12⟩', 5, 0, 10, 0)
        # n2.shiftRight(3 + 2)
        # n1.d = n2.d = 1
        # n0.children = [n1, n2]
        # n0.r = n2.r
        # n0.m = n2.r // 2
        # r = n0.shiftRight(4)
        # displayTree = n0
        # displayTree = Node('⟨12345678⟩', 5, 0, 10, 0)
        depth = displayTree.getDepth()
        print(displayTree)
        print('Depth: ', depth)
        print('-----------------')

        return displayTreeToString(displayTree, depth)

    def __str__(self):
        return self.toString3()

    def __repr__(self) -> str:
        return '\n' + str(self) + '\n'

    def __len__(self):
        return len(self.lst)
