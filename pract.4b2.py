import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Display the array
print("Array:\n", arr)

# Analyze dimensions and attributes
print("\n--- Array Attributes ---")
print("Number of dimensions (ndim):", arr.ndim)
print("Shape (rows, columns):", arr.shape)
print("Total number of elements (size):", arr.size)
print("Data type of elements (dtype):", arr.dtype)
print("Item size (bytes per element):", arr.itemsize)
print("Total memory used (in bytes):", arr.nbytes)
print("Type of object:", type(arr))
