l1 = [1, 2, [3, 4]]

# l2 = l1


# (1) 浅拷贝
l2 = l1.copy()  # l2 = l1[:]

# l1[0] = 100
# print(l2)

# l1[2][0] = 300
# print(l2)

# l1[2] = [5, 6]
# print(l2)


# （2）深拷贝
import copy

l3 = copy.deepcopy(l1)
l1[2][0] = 300
print(l3)


