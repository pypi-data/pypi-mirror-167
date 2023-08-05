import random


class RandomArray(object):

    @staticmethod
    def normalizedArray(itemCount: int) -> list:
        """
        The constructor of RandomNormalizedArray class gets an integer itemCount as an input. Creates a list of
        size itemCount and loops through each element of the list and initializes them with a random number by using
        random. Then, accumulates each element of the list and at the end divides each element with the resulting sum.
        :param itemCount: input defining array size.
        :return: Normalized array
        """
        total = 0.0
        array = []
        for i in range(itemCount):
            array.append(random.uniform(0, 1))
            total += array[i]
        for i in range(itemCount):
            array[i] /= total
        return array

    @staticmethod
    def indexArray(itemCount: int, seed: int) -> list:
        """
        Returns an array of array indexes but shuffled. For example, if n is 4, the method returns an array of indexes
        0, 1, 2, 3 but shuffled.
        :param itemCount: Number of elements in the array
        :param seed: Seed used to shuffle array.
        :return: Index array
        """
        array = [i for i in range(itemCount)]
        random.seed(seed)
        random.shuffle(array)
        return array
