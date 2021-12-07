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
    def inner(oa: OrderAnnotation, lst: List[Term]):
        return Term(oa, lst)

    @staticmethod
    def leaf(oa: OrderAnnotation):
        return Term(oa, [])

    @staticmethod
    def fromTuples(tup: Tuple[OrderAnnotation, list]):
        node = tup[0]
        children = map(Term.fromTuples, tup[1])
        return Term(node, list(children))

    def __init__(self, oa: OrderAnnotation, lst: List[Term]):
        # an order annotation serves as the functor of the term
        self.oa = oa
        # list of the children
        self.lst = lst

    def __str__(self):
        def aux(term: Term, level: int):
            return '│ ' * (level - 1) + \
                ('├─' if level > 0 else '') + str(term.oa) + \
                '\n'.join([''] + [aux(x, level + 1) for x in term.lst])

        return aux(self, 0)

    def __len__(self):
        return len(self.lst)
