import array

#Create an array of integers
original = array.array('i', [1, 2, 3, 4, 5])

print("Original array:", original)

#Aliasing:both variables point to the same array
alias = original

# Copying: create a new independent copy of the array
copy = original[:]

#Modify original array
original[0] = 100

#Display all arrays
print("\n---After modifying original[0] = 100 ---")
print("Original array:",original)
print("Alias array (same object) :", alias)
print("Copied array (independent):", copy)

# Check identity
print("\n--- Identity Check ---")
print("original is original :",id(original))
print("original is alias :",id(alias))
print("original is copy :",id(copy))
print("original is alias:", original is alias) #True
print("original is copy:", original is copy)  #False
