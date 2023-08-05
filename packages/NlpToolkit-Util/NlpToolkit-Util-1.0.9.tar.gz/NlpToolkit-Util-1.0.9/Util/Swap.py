class Swap(object):

    @staticmethod
    def swap(array: list, i: int, j: int):
        """
        The swap method takes a list and two integer numbers i, j. And interchange the given array's
        items at index i and index j.
        :param array: Array of elements
        :param i: first index to swap.
        :param j: second index to change.
        """
        t = array[i]
        array[i] = array[j]
        array[j] = t
