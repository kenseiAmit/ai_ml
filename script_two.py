"""
This is the practice file for the Book: 'Learning NumPy Arrays: Supercharge your scientific Python Computation by
understanding how to use NumPy library effectively' by Ivan Idris.
"""

"""
Chapter Two: NumPy Basics
Script Two: Adding arrays with Python and NumPy.
Notice the difference in time of execution using basic Python and NumPy.
"""
import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

lena = scipy.misc.lena()
lenaCopy = scipy.misc.lena()
lenaView = lena.view()

#
# plt.figure(figsize=(50,50))
# plt.subplot(2,2,1)
# plt.imshow(lena)
# plt.subplot(2,2,2)
# plt.imshow(lenaCopy)
# plt.subplot(2,2,3)
# plt.imshow(lenaView)
# lenaCopy.flat = 0
# plt.subplot(2,2,4)
# plt.imshow(lenaCopy)
# plt.savefig('lena.png')
#
# # Fancy indexing
#
# lenaCopy = scipy.misc.lena()
# lenaCopy[range(lenaCopy.shape[0]), range(lenaCopy.shape[1])] = 0
# lenaCopy[range(lenaCopy.shape[0]-1,-1,-1), range(lenaCopy.shape[1])] = 0
# plt.figure(figsize=(50,50))
# plt.subplot(2,2,1)
# plt.imshow(lena)
# plt.subplot(2,2,2)
# plt.imshow(lenaCopy)
# plt.subplot(2,2,3)
# plt.imshow(lenaView)
# plt.savefig('lenaCopy.png')
#
# # Shuffle array indices with shuffle function
# def shuffle_indices(size):
#     anArray = np.arange(size)
#     np.random.shuffle(anArray)
#     return anArray
#
# plt.figure()
# plt.imshow(lena[np.ix_(shuffle_indices(lena.shape[0]), shuffle_indices(lena.shape[1]))])
# plt.savefig("lenaShuffled.png")
#
#
# def get_indices(size):
#     return np.arange(size) % 4 == 0
#
# plt.figure()
# plt.subplot(211)
# plt.imshow(lena[np.ix_(get_indices(lena.shape[0]), get_indices(lena.shape[1]))])
# plt.subplot(212)
# lenaCopy[(lena > lena.max()/4) & (lena < 3 * lena.max()/4)] = 0
# plt.imshow(lenaCopy)
# plt.savefig('lenaMissing.png')

sudoku = np.array([
 [2, 8, 7, 1, 6, 5, 9, 4, 3],
 [9, 5, 4, 7, 3, 2, 1, 6, 8],
 [6, 1, 3, 8, 4, 9, 7, 5, 2],
 [8, 7, 9, 6, 5, 1, 2, 3, 4],
 [4, 2, 1, 3, 9, 8, 6, 7, 5],
 [3, 6, 5, 4, 2, 7, 8, 9, 1],
 [1, 9, 8, 5, 7, 3, 4, 2, 6],
 [5, 4, 2, 9, 1, 6, 3, 8, 7],
 [7, 3, 6, 2, 8, 4, 5, 1, 9]
 ])

shape = (3, 3, 3, 3)

strides = sudoku.itemsize * np.array(([27, 3, 9, 1]))

square = np.lib.stride_tricks.as_strided(sudoku, shape=shape, strides=strides)
print(square)
