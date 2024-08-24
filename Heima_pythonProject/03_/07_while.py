'''
i = 0
sum = 0

while i <= 100:
    # print('Marie, ich liebe dich')
    sum += i
    i += 1

print(f'The sum of 1 to 100 cumulatively is {sum}' )
print('The sum of - 1 to 100 cumulatively is %d' % sum )
'''

# Basic example of while
'''
import random
num = random.randint(1, 100)

count = 0
# 通过一个布尔类型的变量，做循环是否继续的标记
# 如果下面猜中了，就将flag定义为false
flag = True
while flag:
    guess_num = int(input('input a number: '))
    count = count + 1
    if guess_num == num:
        print('It\'s right')
        # 猜中了，循环就可以停止了， False是循环终止的条件
        flag = False
    else:
        if guess_num > num:
            print('Too big!')
        else:
            print('Too small!')
print('You have guessed %d times in total.' % count)
'''

# Basic循环的嵌套应用
'''
i = 1
while i <= 10:
    print("今天是第 %d 天， 准备表白......" % i)
    i += 1
    j = 1
    while j <= 10:
        print('送给小美第 %d 枝玫瑰花' % j)
        j += 1
    print('小美，我喜欢你')
print('坚持到第 %d 天，表白成功' % (i-1))
'''

# while嵌套打印九九乘法表

i = 1
while i <= 9:
    j = 1
    while j <= i:
        # 内层循环的print语句不要换行，通过制表符\t进行对齐
        print(f'{j}x{i}={j * i}\t', end='')
        j += 1
    i += 1
    print() # print空内容就是换行的意思


# print('Hello', end='')
# print('World', end='')
# print('Hello\tWorld')
# print('itheima\tbest')


