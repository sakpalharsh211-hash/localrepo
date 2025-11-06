def common_element(list1,list2):
    result=False
    for i in list1:
        for j in list2:
            if i==j:
                result=True
    return result

lst1 = []
n = int(input("Enter the number of elements in list1: "))
for i in range(n):
    ele = int(input())
    lst1.append(ele)
print("list1 is: ",lst1)

lst2 = []
n = int(input("Enter the number of elements in list2: "))
for i in range(n):
    ele = int(input())
    lst2.append(ele)
print("list1 is: ",lst2) 


print(common_element(lst1,lst2))
#print(common_element([12,25,33,47,50], [50,60,70,80,90]))
#print(common_element([11,22,33,34,55], [66,77,88,99]))
