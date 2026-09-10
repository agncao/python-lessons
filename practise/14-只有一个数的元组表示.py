t1=()
print(t1)
print(type(t1))

# ()
# <class 'tuple'>

t2=(10)
print(t2)
print(type(t2))
# 10
# <class 'int'>
# 这个不是个tuple，因为括号() 既可以表示tuple，又可以表示数学公式中的小括号，在这里是数学公式，计算结果是10
# 要定义1个元素的tuple必须加一个逗号, 如下:
t3=(10,)
print(t3)
print(type(t3))
# (10,)
# <class 'tuple'>
t4=(10,2)
print(t4)
print(type(t4))
# (10, 2)
# <class 'tuple'>

t5=(10,2,)
print(t5)
print(type(t5))
# (10, 2)
# <class 'tuple'>