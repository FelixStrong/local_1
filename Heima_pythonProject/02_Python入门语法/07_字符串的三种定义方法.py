# 单引号定义法
name = '黑马程序员'
print(type(name))
# 双引号定义法
name = "黑马程序员"
print(type(name))
# 三引号定义法，写法和多行注释是一样的
name = """
我   是
黑马
程序员
"""
print("三引号定义法:", name)
print(type(name))

# 字符串内包含双引号
name = '"黑马程序员"'
print("字符串内包含双引号:", name)
# 在字符串内包含单引号
name = "'黑马程序员'"
print("在字符串内包含单引号:", name)
# 使用转义字符\解除引号的效用
name = "\"黑马程序员\""
print("使用转义字符解除双引号效用:", name)
name = '\'黑马程序员\''
print("使用转义字符解除单引号效用:", name)