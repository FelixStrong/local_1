"""
演示对表达式进行字符串格式化
"""

print("1 * 1 的结果是： %d" % (1 * 1))
print(f"1 * 2 的结果是： {1 * 2}")
print("字符串在Python中的类型名是： %s" % type("字符串"))
print(type("字符串"))

name = "传智播客"
set_up_year = 2006
stock_price = 19.99

# f: format
print(f"Ich bin {name}, ich wurde im Jahr {set_up_year} begründet, die heutige Stockpreise ist {stock_price}")

"""
股价计算小程序
"""
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
groth_days = 7
print(f"公司： {name}， "
      f"股票代码： {stock_code}， "
      f"当前股价： {stock_price}， "
      f"每日增长系数是： {stock_price_daily_growth_factor}， "
      f"经过{groth_days}天的增长后，"
      f"股价达到了： {stock_price * stock_price_daily_growth_factor ** groth_days}") # 两个*号代表的意思是幂次方
end_price = stock_price * stock_price_daily_growth_factor ** groth_days
print("公司： %s， 股票代码： %s， 当前股价： %.1f， 每日增长系数是： %s， 经过%s天的增长后，股价达到了： %7.2f"
      % (name, stock_code, stock_price, stock_price_daily_growth_factor, groth_days, end_price))





