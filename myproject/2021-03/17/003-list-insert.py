list1 = [1, 2, 3]
print(list1)  # [1, 2, 3]
list1.insert(2, 10)
print(list1)  # [1, 2, 10, 3]
list1.insert(1, 2)
print(list1)  # [1, 2, 2, 10, 3]
list1.insert(1, ["hello"])
print(list1)  # [1, ['hello'], 2, 2, 10, 3]
