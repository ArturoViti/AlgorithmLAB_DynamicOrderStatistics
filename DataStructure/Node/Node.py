
class Node:
    """
        Class to represent a Node that stores an integer value.
    """
    def __init__( self, value: int ):
        self.__set_value(value)

    def __str__(self):
        return "Node Value:" + str(self.__value)

    def __set_value( self, value: int ):
        if not isinstance(value, int):
            raise ValueError("Value must be int")
        self.__value = value

    def setValue( self, value: int ):
        self.__set_value(value)

    def getValue(self):
        return self.__value

    # Enables intuitive comparison between Node instances using <, >, and == operators
    def __lt__( self, other ):
        if isinstance(other, Node):
            return self.__value < other.__value
        return NotImplemented

    def __gt__( self, other ):
        if isinstance(other, Node):
            return self.__value > other.__value
        return NotImplemented

    def __eq__( self, other ):
        if isinstance(other, Node):
            return self.__value == other.__value
        return NotImplemented
