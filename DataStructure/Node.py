
class Node:
    value = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Node Value:" + str(self.value)

    def __set_value(self, value):
        if not isinstance( value, int ):
            raise ValueError("Value must be int")
        self.__value = value

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
