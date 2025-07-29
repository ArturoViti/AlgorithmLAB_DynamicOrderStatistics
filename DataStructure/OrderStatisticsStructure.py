from abc import ABC, abstractmethod

from DataStructure.Node.Node import Node


class OrderStatisticStructure(ABC):
    @abstractmethod
    def OSSelect( self, node: Node, i: int ) -> Node:
        """
            Returns the i-th element in order
        """
        pass

    @abstractmethod
    def OSRank( self, x: Node ) -> int:
        """
            Returns the rank (position) of element x
        """
        pass