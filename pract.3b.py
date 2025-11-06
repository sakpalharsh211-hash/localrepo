import array
import math

# Accept a list of numbers from the user (comma-separated)
input_str = input("Enter numbers separated by commas: ")

# Convert input string to a list of integers
num_list = [int(num.strip()) for num in input_str.split(',')]

# Create an array of integers
arr = array.array('i', num_list)

# Display the original array
print("\nOriginal array:", arr)

# Basic mathematical operations
total = sum(arr)
mean = total / len(arr)
maximum = max(arr)
minimum = min(arr)

# Standard deviation
variance = sum((x - mean) ** 2 for x in arr) / len(arr)
std_dev = math.sqrt(variance)

# Square and square root for each element
squares = array.array('f', [x**2 for x in arr])
square_roots = array.array('f', [math.sqrt(x) for x in arr])

# Display results
print("\n--- Mathematical Operations ---")
print("Sum:", total)
print("Mean:", mean)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Standard Deviation:", std_dev)
print("Squares:", squares)
print("Square Roots:", square_roots)




#Using Lists and User Input:
# Accept a list of numbers from the user (comma-separated)
input_str = input("Enter numbers separated by commas: ")

# Convert the input string to a list of integers
num_list = [int(num.strip()) for num in input_str.split(',')]

# Display the original list
print("\nOriginal list:", num_list)

# Mathematical functions
total = sum(num_list)
mean = total / len(num_list)
maximum = max(num_list)
minimum = min(num_list)

# Calculate standard deviation
variance = sum((x - mean) ** 2 for x in num_list) / len(num_list)
std_dev = variance ** 0.5

# Display results
print("\n--- Mathematical Operations ---")
print("Sum:", total)
print("Mean:", mean)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Standard Deviation:", std_dev)

# Square root and square (element-wise)
import math
squares = [x**2 for x in num_list]
square_roots = [math.sqrt(x) for x in num_list]

print("Squares:", squares)
print("Square roots:", square_roots)



'''#Using NumPy library

#pip install numpy
import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Display the original array
print("Original array:", arr)

# Mathematical operations
print("\n--- Mathematical Functions ---")
print("Sum of elements:", np.sum(arr))
print("Mean (average):", np.mean(arr))
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Standard deviation:", np.std(arr))
print("Square root of each element:", np.sqrt(arr))
print("Array squared:", np.power(arr, 2))
print("Sine of each element (in radians):", np.sin(arr))'''




