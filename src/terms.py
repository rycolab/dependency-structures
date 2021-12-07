from typing import Iterable, Union
from typing_extensions import Self


class OrderAnnotation(object):

    @staticmethod
    def leaf() -> Self:
        """Creates an order annotation with just the root in the order list

        Returns:
            OrderAnnotation: New order annotation of block-degree 1
        """
        return OrderAnnotation([[0]])

    @staticmethod
    def degree1(*order: Iterable[int]) -> Self:
        """Creates an order annotation with block-degree 1 and given order

        Args:
            order (list): Single int-list representing this OA's order

        Returns:
            OrderAnnotation
        """
        return OrderAnnotation([[*order]])

    @staticmethod
    def degreeK(*orders: Iterable[Iterable[int]]) -> Self:
        return OrderAnnotation([*orders])

    def __init__(self, orders: Union[Iterable[Iterable[int]], Iterable[int]]):
        """Creates a new order annotation instance with given order annotations

        Args:
            orders (list): Single order (for block-degree 1) or list of orders (for block-degree k > 1)
        """
        # INVARIANT: self.orders is always a list of lists
        if len(orders) == 0:
            # Empty order annotation
            self.degree = 0
            self.orders = []
        elif all([isinstance(x, int) for x in orders]):
            # Block-degree 1 order annotation, implicitly treat orders as first block
            self.degree = 1
            self.orders = [orders]
        elif all([isinstance(x, list) for x in orders]):
            # Block-degree > 1, every sublist is an order annotation for a block
            self.degree = len(orders)
            self.orders = orders
        else:
            raise TypeError("Cannot interpret argument as order annotation: " +
                            str(orders))

    def __str__(self):
        return '⟨' + ','.join([''.join([str(x) for x in order]) for order in self.orders]) + '⟩'

    def __repr__(self):
        return str(self)

    def __getitem__(self, i):
        return self.orders[i]


class Term(object):

    def __init__(self, oa, lst):
        # an order annotation serves as the functor of the term
        self.oa = oa
        # list of the children
        self.lst = lst

    def __str__(self):
        # TODO: visualization of the terms
        return str(self.oa)

    def __len__(self):
        return len(self.lst)
