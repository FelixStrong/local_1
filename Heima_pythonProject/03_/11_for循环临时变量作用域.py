for i in range(5):
    print(i)

print(i)  # 规范上不建议这样做

print()
i = 0
for i in range(5):
    print(i)

print(i)  # 如果想在for循环外部访问临时变量， 规范的做法是在for之前定义这个变量
