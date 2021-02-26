"""
This is the practice file for the Book: 'Learning NumPy Arrays: Supercharge your scientific Python Computation by
understanding how to use NumPy library effectively' by Ivan Idris.
"""

"""
Chapter One: Getting Started with NumPy
Script One: Adding arrays with Python and NumPy.
Notice the difference in time of execution using basic Python and NumPy.
"""

import numpy as np
from datetime import datetime


# Adding arrays
def pythonSum(n) -> list:
    """
    The function adds entries in two arrays and stores them in a third array using basic python data structures and
    methods.

    :param n: The size of the arrays to be added.
    :return: An array whose elements are the sum of corresponding elements in the first two arrays.
    """
    # Setting up variables
    firstList = range(n)
    secondList = range(n, 2 * n)

    return [one + two for (one, two) in zip(firstList, secondList)]


def numpySum(n) -> np.array:
    """
    This function adds elements of two NumPy arrays into a third array using NunmPy.
    :param n:
    :return: A NunmPy array whose elements are the sum of corresponding elements in the first two arrays.
    """

    # Creating NumPy arrays
    firstArray = np.arange(n)
    secondArray = np.arange(n)

    return firstArray + secondArray

size = int(input("Enter the size of the arrays to be added: "))
start = datetime.now()
firstArray = pythonSum(size)
delta = datetime.now() - start
print("Elapsed time in microseconds: ", delta.microseconds)
start = datetime.now()
secondArray = numpySum(size)
delta = datetime.now() - start
print("Elapsed time in microseconds: ", delta.microseconds)
