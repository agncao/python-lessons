"""
字典根据值从小到大排序

map={"k1":48,"k2":1209,"k3":998,"k4":29}
"""

map={"k1":48,"k2":1209,"k3":998,"k4":29}

print("用lambda表达式:sorted(map,key=lambda x:map[x]) 得到根据value排序好的key数组:")
ll = sorted(map,key=lambda x:map[x])
map1= {key:map[key] for key in ll}
print(map1)


print("字典转元祖数组后再排序")
list1=map.items()
ll = sorted(list1,key=lambda x:x[0],reverse=True)
map2={k:v for k,v in ll}
print(map2)