funcs = [lambda x=i:x for i in range(3)]
print("\n==================\n")
print(funcs[i]() for i in range(3))
print(f"2. {[funcs[i]() for i in range(3)]}")
print("3. ",*(funcs[i]() for i in range(3)))


print(f"4. {[i for i in range(3)]}")