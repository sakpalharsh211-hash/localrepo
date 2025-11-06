import numpy as np
#create a numpy array
arr=np.array([[10, 20, 30],
            [40, 50, 60], 
            [70, 80, 90]])
print("original array:\n", arr)
import numpy as np

# Create a NumPy array
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original Array:\n", arr)

# --- Basic Indexing ---
print("\n--- Basic Indexing ---")
print("Element at (0, 1):", arr[0][1])    # 20
print("Element at (2, 2):", arr[2, 2])    # 90

# --- Slicing ---
print("\n--- Slicing ---")
print("First two rows:\n", arr[:2])               # Rows 0 and 1
print("Last column:\n", arr[:, -1])               # Last column
print("Middle elements (1:3, 0:2):\n", arr[1:3, 0:2])  # Rows 1-2, Columns 0-1

# --- Advanced Indexing ---
print("\n--- Advanced Indexing ---")
# Selecting specific elements using arrays of indices
rows = np.array([0, 1, 2])
cols = np.array([2, 0, 1])
print("Elements at (0,2), (1,0), (2,1):", arr[rows, cols])

# Boolean indexing: Get elements greater than 50
print("Elements greater than 50:", arr[arr > 50])

# Fancy indexing: select rows out of order
print("Rows 2 and 0:\n", arr[[2, 0]])
