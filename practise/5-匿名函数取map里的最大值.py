map={"k1":48,"k2":1209,"k3":998,"k4":29}

# 默认比较的是key值
print(max(map)) #k4
#print(max(map.keys()))

def getvalue(name):
    return map[name]
# 取value最大的那个key
res = max(map,key=getvalue)
# 或者
r = max(map,key=lambda x:map[x])
print(res)
print(r)


# max 源码大致如下：
def my_max(*args, key=None):
    if not args:
        raise TypeError("max expected at least 1 argument, got 0")
    it = iter(args[0]) if len(args) == 1 else iter(
        args)  # 兼容两种调用形式
    key = key if key is not None else (lambda
                                           x: x)  # 没传 key 就用元素自身
    try:
        best = next(
            it)  # 第一个元素直接当选
    except StopIteration:
        raise ValueError("max() arg is an empty sequence")
    best_key = key(best)
    for x in it:
        x_key = key(x)
        if x_key > best_key:  # 严格 >：并列时保留先出现的那个
            best, best_key = x, x_key
    return best

res = my_max(map,key=getvalue)
print(res)