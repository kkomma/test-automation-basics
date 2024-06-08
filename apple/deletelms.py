list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5]

for element in list2:
    if element in list1:
        list1.remove(element)

print(list1)  # Output: [2, 4]