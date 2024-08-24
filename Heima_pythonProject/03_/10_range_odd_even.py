num = int(input('Please input a number: '))
count = 0
for x in range(1, num):
    if (x % 2) == 0:
        # print("{0} 是偶数".format(x))
        count += 1
    else:
        count += 0
        # print("{0} 是奇数".format(x))
print(f"There are {count} even numbers in [1, {num}]")