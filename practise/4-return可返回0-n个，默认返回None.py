# 如果函数没有return 则返回None
a=print('abc')
print(a)

def test1():
    return [1,2,3],True,'a'
# 输出元组
print(test1())  #([1, 2, 3], True, 'a')