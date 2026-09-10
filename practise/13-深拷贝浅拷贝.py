# 浅拷贝
import copy

print("浅拷贝==========")
arr1=['a',('t1','t2'),[1,2]]
arr2=arr1.copy()
print("arr1和arr2地址不一样")
print("arr1的地址:",id(arr1),", arr2的地址:",id(arr2))
print("但是arr1元素和arr2元素地址一样，即使是可变数据类型")
for index,item in enumerate(arr1):
    print(f"arr1[{index}]的地址:",id(arr1[index]),f", arr2[{index}]的地址:",id(arr2[index]))

print("修改arr1中的元素值，就是修改了arr2的元素值")
arr1[2].append(2)
print("arr1 元素:",arr1,", arr2 元素:",arr2)

print("但是向arr1中追加元素，并没有向arr2追加元素")
arr1.append(2)
print("arr1 元素:",arr1,", arr2 元素:",arr2)
# 浅拷贝：拷贝父对象，但不会拷贝子对象，子对象是共用的

print("深拷贝==========")
arr3=copy.deepcopy(arr1)
print("arr1的地址:",id(arr1),", arr3的地址:",id(arr3))

for index,item in enumerate(arr1):
    print(f"arr1[{index}]的地址:",id(arr1[index]),f", arr3[{index}]的地址:",id(arr3[index]))