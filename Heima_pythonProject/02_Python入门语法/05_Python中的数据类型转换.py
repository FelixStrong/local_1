# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str),num_str)  # 类型发生变化，并且内容不变
float_str = str(11.12)
print(type(float_str), float_str)

# 将字符串转换成数字
num = int("11")
print(type(num), "num = ", num)

num2 = float("11.345")
print(type(num2), "num2 = ", num2)

# 错误实例
"""
num3 = int("rjty") # 非数字内容的字符串无法转化成数字 
print(type(num3), num3)
"""

# 整数转浮点数
float_num = float(11)
print(type(float_num), "float_num = ",float_num)

# 浮点数转整数，会丢失精度
int_num = int(11.345)
print(type(int_num), int_num)

jinitaimei = "鸡你太美"
print(jinitaimei)
Class = 1
print(Class)
