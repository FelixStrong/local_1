# 通过占位的方式完成拼接
name = "黑马程序员"
msg = "学IT就来 %s" % name # %表示我要占位，s表示将变量变成字符串放入占位的地方
print(msg)

# 通过占位的方式，完成数字和字符串的拼接
class_num = 57
avg_salary = 16781
msg = "Python大数据学科，北京%s期，毕业平均工资：%s" % (class_num, avg_salary)
print(msg)

"""
%s 将内容转换成字符串，放入占位位置 
%d 将内容转换成整数，放入占位位置 
%f 将内容转换成浮点型，放入占位位置 
"""
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
message = "我是： %s， 我成立于： %d， 我今天的股价是： %f" % (name, set_up_year, stock_price)
print(message)
message = "我是： %s， 我成立于： %s， 我今天的股价是： %s" % (name, set_up_year, stock_price)
print(message)

"""
演示第二种字符串格式化的方法
可以通过 
   f"{变量} {变量}" 的方式进行快速格式化

这种方式：
   - 不理会类型
   - 不做精度控制

适合对精度没有要求的时候快速使用

"""
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
# f: format
print(f"我是{name}， 我成立于： {set_up_year}年， 我今天的股价是： {stock_price}")


