class Interval(object):

    __list: list

    def __init__(self):
        """
        A constructor of Interval class which creates a new list.
        """
        self.__list = []

    def add(self, start: int, end: int):
        """
        The add method adds a new Tuple with given inputs to the list.
        :param start: first element of Tuple.
        :param end: second element of Tuple.
        """
        self.__list.append((start, end))

    def getFirst(self, index: int) -> int:
        """
        The getFirst method returns the first element at the list list's given index.
        :param index: to use at getting tuple from list.
        :return: the first element at the list list's given index.
        """
        return self.__list[index][0]

    def getLast(self, index: int) -> int:
        """
        The getLast method returns the last element at the list list's given index.
        :param index: to use at getting tuple from list.
        :return: the last element at the list list's given index.
        """
        return self.__list[index][1]

    def size(self) -> int:
        """
        The size method returns the size of the list list.
        :return: size of the list list.
        """
        return len(self.__list)
