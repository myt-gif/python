set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合
"""增"""
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

"""删"""
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # {1, 3}

my_set = {1, 2, 3}
my_set.discard(4)
print(my_set)  # {1, 2, 3}（不引发错误）

"""集合运算"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # {3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # {1, 2}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # {1, 2, 4, 5}

"""判断集合关系"""
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # True

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # True

set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # True

print(set1)
print(set2)