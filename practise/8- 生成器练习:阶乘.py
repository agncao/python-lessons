'''
计算 1!+2!+3!+4!
'''
def func(n):
    sum=0
    for i in range(1,n):
        current=1
        for j in range(1,i+1):
            current*=j
        sum+=current
    return sum

print("func: ", func(5))
print("=="*20,"\n")

def func2(n):
    i = 1
    j = 1
    while i<n:
        yield j
        print("yield j: ", j)
        i+=1
        j=j*i

print("type of func2: ", func2(5))
print("=="*20,"\n")

print("func2: ",sum(func2(5)))
print("=="*20,"\n")

s=0
for n in func2(5):
    # print("阶乘：",n)
    s+=n
print("sum: ", s)
