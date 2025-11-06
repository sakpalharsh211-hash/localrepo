import array

arr = array.array('i', [10, 20, 30, 40, 50])

print("orginal array:", arr)

print("\n--- Basic operations ---")
arr.append(60)                          
print("After append(60) :", arr)

arr.insert(2, 25)                      
print("After insert(2, 25):" , arr)

arr.remove(40)
print("After remove(40):", arr)

arr.pop()
print("After pop():",arr)

print("Length of array:", len(arr))

print("\n--- Indexing ---")
print("Element at index 0:",arr[0])
print("Element at index -1 (last):", arr[-1])

print("\n--- Slicing ---")
print("arr[1:4]:", arr[1:4])
print("arr[:3]:", arr[:3])
print("arr[2:]:", arr[2:])
print("arr[::-1]:", arr[::-1])



