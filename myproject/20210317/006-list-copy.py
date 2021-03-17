list1 = [7, 3, 2, 5, 1, 6, 4]
print(list1)  # [7, 3, 2, 5, 1, 6, 4]
list2 = list1
list2[0] = 0
print(list1)  # [0, 3, 2, 5, 1, 6, 4]
print(list2)  # [0, 3, 2, 5, 1, 6, 4]
list3 = list1.copy()
list3[0] = 7
print(list1)  # [0, 3, 2, 5, 1, 6, 4]
print(list2)  # [0, 3, 2, 5, 1, 6, 4]
print(list3)  # [7, 3, 2, 5, 1, 6, 4]
