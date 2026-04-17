#Aim:Creating and manipulating array
#Name:Khan Tasneem
#date:15-04-2026
import numpy as np

array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(array_2d)

array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(array_3d)

reshaped_array = array_1d.reshape(5, 1)
print("\nReshaped 1D to 2D Array:")
print(reshaped_array)

sliced_array = array_2d[:, 1]
print("\nSliced 2D Array (second column):")
print(sliced_array)

indexed_value = array_3d[1, 0, 1]
print("\nIndexed value from 3D Array (array_3d[1, 0, 1]):")
print(indexed_value)
