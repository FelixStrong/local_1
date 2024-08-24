'''
# 获取一个从1开始，到100结束的数字序列（不含100本身）
num = range(1, 100, 15)
for x in num:
    print(x)

# 获取一个从0开始，到5结束的数字序列（不含5本身）
print()
num = range(5)
for x in num:
    print(x)

# 获取一个从1开始，到5结束的数字序列（不含5本身）
print()
num = range(1, 5)
for x in num:
    print(x)
'''

i = 1
while i <= 5:
    print("送玫瑰花")
    i += 1
print()

# the same function
for x in range(5):
    print('送玫瑰花')
