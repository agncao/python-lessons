list1=[2,4,12,54,1]

# 推导式 —— “表达式 +for 子句”必须被[]、{} 或 () 包起来，整体才是一个合法的表达式, 如下写法是错的
# print((list1.index(i),i)) for i in list1
print("1. 列表推导式写法（不推荐这样用）:")
[print((list1.index(i), i)) for i in list1]  # 列表推导式（不推荐这样用）

# 更好的写法
print("2. 遍历enumerate(list1): ")
for idx, val in enumerate(list1):
    print((idx, val))

# 更简单的写法
print("3. 最简单的写法是用list(enumerate(list1))生成新的元祖list: ")
ll = list(enumerate(list1)) # 枚举对象转换成list
print(ll)

print("4. 遍历range(0,len(list1):")
for i in range(0,len(list1)):
    print((i, list1[i]))

print("5. list1.index(i)来获得元素的索引号:")
for i in list1:
    print((list1.index(i), i))

print("="*20)
dd=dir(list1)
print(dd)