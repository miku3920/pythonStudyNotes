A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {1, 2}

# 差集 {1, 2}
print(A-B)
print(A.difference(B))
# 交集 {3, 4}
print(A & B)
print(A.intersection(B))
# 聯集 {1, 2, 3, 4, 5, 6}
print(A | B)
print(A.union(B))
# 對稱差集 {1, 2, 5, 6}
print(A ^ B)
print(A.symmetric_difference(B))
# 子集 True
print(C < A)
print(C.issubset(A))
# 父集 True
print(A > C)
print(A.issuperset(C))
