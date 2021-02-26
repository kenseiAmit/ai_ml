"""
This is the practice file for the Book: 'Learning NumPy Arrays: Supercharge your scientific Python Computation by
understanding how to use NumPy library effectively' by Ivan Idris.
"""

"""
Chapter One: Getting Started with NumPy
"""
"""
Chapter 2: NumPy Basics
"""
# Import all necessary libraries at one place
import numpy as np
import scipy.io.wavfile

# Advantages of using NumPy arrays
# NumPy offers homogeneous arrays accessed with optimized C API
# -------------------------------------------------------------------------------------#
#
# # The default data type of an array is int64
# numpyArray = np.arange(10)
# print(numpyArray.dtype)
#
# # ---------------------------------------------------------------------------------------#
#
# # The shape of the array is a tuple that contains its dimensions
# numpyArray = np.arange(10)
# print(numpyArray.shape, type(numpyArray.shape))
#
# # -----------------------------------------------------------------------------------------#
#
# # Multidimensional array in NumPy
# multiArray = np.array([np.arange(5), np.arange(5), np.arange(5), np.arange(5), np.arange(5)])
# print(multiArray)
#
# # Shape of the array
# print(multiArray.shape)
#
# # Arary indexing in NumPy
# print(multiArray[0][0])
# print(multiArray[3][3])
#
# # ------------------------------------------------------------------------------------------#
#
# # Data type of an array can be specified
# numpyArray = np.arange(9, dtype=np.uint64)
# print(numpyArray)
# numpyArray = np.arange(5, dtype='D')
#
# # The size of an item in an array
# print(numpyArray.dtype.itemsize)
#
# # -------------------------------------------------------------------------------------------#
#
# # Data types in NumPy
# print(np.dtype)
# print(np.float64(45))
#
# # Data type constructors and objects
# numpyDataType = np.dtype("D")
# print(numpyDataType)
#
# # Attributes of the datatype objects
# print(numpyDataType.char)
# print(numpyDataType.str)
#
# # Making datatype object using shorthands
# print((np.dtype('float64')))
# print((np.dtype('f8')))
#
# # List of all available datatype in NumPy
# for key, value in np.sctypeDict.items():
#     print('key: ', key, '\n value: ', value)
#
# # Creating a record datatype
# numpyDataTypes = np.dtype([('name', str, 20), ('age', 'i'), ('income', 'd')])
# print(numpyDataTypes)
# print(numpyDataTypes['name'])
#
# # Heterogeneous arrays of custom made datatype
# numpyItems = np.array([('Meaning of life', 5, 43.67), ('No meaning of life', 6, 32.5)])
# print(numpyItems)
#
# # -------------------------------------------------------------------------------------------#
#
# # Slicing and Indexing
# numpyArray = np.arange(216)
# print(numpyArray[5:67])
# print(numpyArray[:7:2])
# print(numpyArray[-5:-10:-2])
#
# # -----------------------------------------------------------------------------------------#
#
# # Manipulating array shapes
# print(multiArray)
#
# # Opening up an array with ravel
# # Ravel only returns a view of the array
# print(multiArray.ravel())
#
# # Opening up an array with flatten
# # flatten allocates new memory
# print((multiArray.flatten()))
# print(multiArray)
#
# # Shape of an array can be changed
# numpyArray.shape = (6, 6, 6)
# print(numpyArray)
#
# # Transposing an array
# print(multiArray.transpose())
# print(multiArray)
#
# # Resize method modifies the aray
# multiArray.resize((6, 6))
# print(multiArray)
#
# # -----------------------------------------------------------------------------------------#
#
# # Stacking arrays
#
# firsArray = np.arange(9).reshape(3, 3)
# secondArray = firsArray ** 2
#
# # Horizontal staking
# stackedArray = np.hstack((firsArray, secondArray))
# print(stackedArray)
# # Or
# stackedArray = np.concatenate((firsArray, secondArray), axis=1)
# print(stackedArray)
#
# # Vertical stacking
# stackedArray = np.vstack((firsArray, secondArray))
# print(stackedArray)
# # Or
# stackedArray = np.concatenate((firsArray, secondArray), axis=0)
# print(stackedArray)
#
# # Depth stacking
# stackedArray = np.dstack((firsArray, secondArray))
# print(stackedArray)
#
# # Column stacking
# stackedArray = np.column_stack((firsArray, secondArray))
# print(stackedArray)
#
# # Row stacking
# stackedArray = np.row_stack((firsArray, secondArray))
# print(stackedArray)
#
# # Splitting arrays
#
# # Horizontal splitting
# [splitAraryOne, splitArrayTwo] = np.hsplit(multiArray, 2)
# print(splitArrayTwo)
# print(splitAraryOne)
#
# # Vertical splitting
# [splitAraryOne, splitArrayTwo] = np.vsplit(multiArray, 2)
# print(splitAraryOne)
# print(splitArrayTwo)
#
# # Depth-wise splitting
# [splitAraryOne, splitArrayTwo] = np.dsplit(numpyArray, 2)
# print(splitAraryOne)
# print(splitArrayTwo)
#
# #----------------------------------------------------------------------------------------#
#
# # Array attributes
#
# # Getting the dimensions of an array
# print(numpyArray.ndim)
#
# # Getting the size of the array
# print(numpyArray.size)
#
# # The size of the array elements in memory
# print(numpyArray.itemsize)
#
# # The total size of array in memory
# print(numpyArray.nbytes)
# # Which is the same as
# print(numpyArray.itemsize*numpyArray.size)
#
# # Complex arrays
# complexArray = np.arange(5, dtype='D')
# print(complexArray.real)
# print(complexArray.imag)
#
# # Flat an array, notice that flat gives a shallow copy
# flatObject = multiArray.flat
# print(flatObject)
# print(flatObject[3])
# multiArray.flat[-1] = -333
# print(multiArray)
#
# #----------------------------------------------------------------------------------------#
#
# # Converting arrays
#
# # Array to list conversion
# print(multiArray.tolist())
# print(type(multiArray.tolist()[0]))
# print(type(multiArray[0]))
#
# #--------------------------------------------------------------------------------------------#
#
# # Indexing with a list of locations
#
# # ix_ is used to crate a mesh of coordinates
# mesh = np.ix_([0, 1], [2, 3])
# multiArary = np.arange(36).reshape(6,6)
# print(multiArary[mesh])

# sudoku = np.array([
#  [2, 8, 7, 1, 6, 5, 9, 4, 3],
#  [9, 5, 4, 7, 3, 2, 1, 6, 8],
#  [6, 1, 3, 8, 4, 9, 7, 5, 2],
#  [8, 7, 9, 6, 5, 1, 2, 3, 4],
#  [4, 2, 1, 3, 9, 8, 6, 7, 5],
#  [3, 6, 5, 4, 2, 7, 8, 9, 1],
#  [1, 9, 8, 5, 7, 3, 4, 2, 6],
#  [5, 4, 2, 9, 1, 6, 3, 8, 7],
#  [7, 3, 6, 2, 8, 4, 5, 1, 9]
#  ])
#
#
# shape = (3, 3, 3, 3)
#
# strides = sudoku.itemsize * np.array(([27, 3, 9, 1]))
#
# square = np.lib.stride_tricks.as_strided(sudoku, shape=shape, strides=strides)
# print(square)

# Broadcasting arrays
# sample_rate, data = scipy.io.wavfile.read('wavfile.wav')


