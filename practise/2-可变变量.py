l1=[]
for i in range(3):
    l1.append({"num":i})

print("1. ",l1)

l2=[]
a={"num":0}
for i in range(3):
    a["num"]=i
    l2.append(a)
    print(f"{i+2}",l2)
    print(f"{i+2}",id(a),id(l2[i]))
print(l2)