print("[0]*3, 这样初始化是不是很简单:")
arr=[0]*3
print(arr)

print("每个成员的地址都一样，想想为何：")
a=0
print("变量a的地址：",id(a))
for i in range(len(arr)):
    print(f"第{i+1}元素地址:",id(arr[i]))

arr[1],arr[2]=3,7
print("此时每个成员的地址：")
for i in range(len(arr)):
    print(f"第{i+1}元素地址:",id(arr[i]))
