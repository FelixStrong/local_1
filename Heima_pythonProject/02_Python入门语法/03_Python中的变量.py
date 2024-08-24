"""
演示Python中变量的相关操作
"""

# 定义一个变量，用来记录钱包余额
money = 50
# 通过print语句，输出变量记录的内容
print("钱包还有： ", money)
# 10 Euro für Icecream
money = money - 10
print("10 Euro für Icecream ausgegeben, übrig geblieben: ", money, "Euro")

# 每隔一小时输出一下钱包的余额
print("现在是下午1点， 钱包余额是：", money)
print("现在是下午2点， 钱包余额是：", money)
print("现在是下午3点， 钱包余额是：", money)
print("现在是下午4点， 钱包余额是：", money)
cola = 5
print("购买了可乐花费",cola,"Euro")
money = money - cola
print("现在剩余",money,"Euro")




