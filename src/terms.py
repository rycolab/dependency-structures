from __future__ import annotations
from typing import List, Tuple


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

    def toString1(self):
        """Converts the term to a string representing a tree similar to bash's `tree` command
        """
        def aux(term: Term, level: int, lastSibling: bool):
            nodeStr = str(term.oa)
            childrenStr = ''
            for i, child in enumerate(term.lst):
                last = i == len(term.lst) - 1
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
        pass

    def __str__(self):
        return self.toString1()

    def __repr__(self) -> str:
        return '\n' * 2 + str(self)

    def __len__(self):
        return len(self.lst)
