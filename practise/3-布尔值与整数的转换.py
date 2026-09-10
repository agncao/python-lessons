"""
求 两个集合的交集并集和差集

set1={2,2.2,True,4+3j}
set2={1,2.2,False,4+3j}
"""

set1={2,2.2,True,4+3j}
set2={1,2.2,False,4+3j}
# print(set1.intersection(set2))
print("1.", set1&set2)
print("2.", set2&set1)

print("3.", set1|set2)
print("4.", set2|set1)
# print(set1.union(set2))

print("5.", set1^set2)
print("6.", set2^set1)