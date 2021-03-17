list1 = [1, 2, 3]
print(list1)  # [1, 2, 3]
list1.extend([10])
print(list1)  # [1, 2, 3, 10]
list1.extend([1, 2])
print(list1)  # [1, 2, 3, 10, 1, 2]
list1.extend(["hello"])
print(list1)  # [1, 2, 3, 10, 1, 2, 'hello']
