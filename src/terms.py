from __future__ import annotations
from printing.terms import TermPrettyPrinter


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
    def degK(*orders: list[int]) -> OrderAnnotation:
        """Create an order annotation of arbitrary block-degree. Orders are passed as lists of
        orders for each block.

        Returns:
            OrderAnnotation
        """
        return OrderAnnotation([*orders])

    def __init__(self, orders: list[list[int]]):
        """Creates a new instance of an order annotation with given orders.
        Order annotations are represented as a list of lists, where each list contains the order
        for the given block.

        You can use the factory methods `leaf`, `deg1` and `degK` to improve legibility.

        Args:
            orders (list[list[int]]): List of orders for each block
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
    def inner(oaList: list, lst: list[Term]) -> Term:
        """Creates a new inner term node

        Args:
            oaList (list): Either int list (implicit block degree 1) or list of int lists (general block degree)
            lst (List[Term]): List of child terms

        Raises:
            TypeError: If `oaList` is not of one of the valid types

        Returns:
            Term: New `Term` object
        """
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
        """Creates a leaf term node consisting of a single order annotation with just the root and 
        no children

        Returns:
            Term: New `Term` object
        """
        return Term(OrderAnnotation.leaf(), [])

    def __init__(self, oa: OrderAnnotation, lst: list[Term]):
        """Creates a new term instance

        Note that well-formedness is not checked

        Args:
            oa (OrderAnnotation): Order annotation of the term
            lst (list[Term]): List of child terms
        """
        # an order annotation serves as the functor of the term
        self.oa = oa
        # list of the children
        self.lst = lst

    def isLeaf(self) -> bool:
        """Returns true if the term is a leaf, i.e. has no children

        Returns:
            bool
        """
        return len(self.lst) == 0

    def __str__(self):
        return TermPrettyPrinter(self).string()

    def __repr__(self) -> str:
        return '\n' + str(self) + '\n'

    def __len__(self):
        return len(self.lst)
