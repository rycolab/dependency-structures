from __future__ import annotations
from typing import List


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

    def toHorizontalTreeString(self) -> str:
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

    def toVerticalTreeString(self) -> str:
        class Node:
            blank = ' '

            @staticmethod
            def leaf(label: str, depth=0) -> Node:
                n = len(label)
                return Node(label, (n - 1) // 2, 0, n, depth)

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
            # Leaf node
            if term.isLeaf():
                return Node.leaf(lbl, depth)
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
            return Node(lbl, m, 0, r, depth, children)

        def displayTreeToString(root: Node, depth: int) -> str:
            blank = ' '
            sym = {'h': '─', 'v': '│', 'bl': '┐',
                   'br': '┌', 'th': '┴', 'bh': '┬', 'vh': '┼'}

            class Brace:
                def __init__(self, d, top: int, bots: list[int]) -> None:
                    self.d = d
                    self.top = top
                    self.bots = bots

                def draw(self, canvas: list[list[str]]):
                    row = canvas[self.d * 2 + 1]
                    imin = min([self.top, *self.bots])
                    imax = max([self.top, *self.bots])
                    fill = sym['br'] + sym['h'] * \
                        (imax - imin - 1) + \
                        sym['bl'] if imin < imax else sym['v']
                    row[imin:imax+1] = fill
                    for i in self.bots[1:-1]:
                        row[i] = sym['bh']
                    botSameAsTop = any([x == self.top for x in self.bots])
                    top = sym['v'] if imin == imax else sym['vh'] if botSameAsTop else sym['th']
                    row[self.top] = top

            queue: list[Node] = [root]
            canvas: list[list[str]] = []
            for _ in range((depth + 1) * 2 - 1):
                canvas.append([blank] * root.r)
            while queue:
                node = queue.pop(0)
                n = len(node.lbl)
                lblleft = node.m - (n - 1) // 2
                lblright = node.m + n - ((n - 1) // 2)
                # Draw node label
                canvas[node.d * 2][lblleft:lblright] = list(node.lbl)
                # Draw brace
                if len(node.children) > 0:
                    brace = Brace(node.d, node.m, [x.m for x in node.children])
                    brace.draw(canvas)
                queue += node.children
            return '\n'.join([''.join(row) for row in canvas])

        displayTree = buildDisplayTree(self)
        depth = displayTree.getDepth()

        return displayTreeToString(displayTree, depth)

    def __str__(self):
        return self.toVerticalTreeString()

    def __repr__(self) -> str:
        return '\n' + str(self) + '\n'

    def __len__(self):
        return len(self.lst)
