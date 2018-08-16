# Python if 语句
# Document 对象参考手册 Python3 实例

# 以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：

# 实例(Python 3.0+)
# # Filename : test.py
# # author by : www.runoob.com
 
# # 用户输入数字
 
# num = float(input("输入一个数字: "))
# if num > 0:
#    print("正数")
# elif num == 0:
#    print("零")
# else:
#    print("负数")
# 执行以上代码输出结果为：

# 输入一个数字: 3
# 正数
# 我们也可以使用内嵌 if 语句来实现：

# 实例(Python 3.0+)
# # Filename ：test.py
# # author by : www.runoob.com
 
# # 内嵌 if 语句
 
# num = float(input("输入一个数字: "))
# if num >= 0:
#    if num == 0:
#        print("零")
#    else:
#        print("正数")
# else:
#    print("负数")
# 执行以上代码输出结果为：

# 输入一个数字: 0
# 零
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 1 篇笔记
#    yao_yaofu

#   522***154@qq.com

# 优化增加输入字符的判断以及异常输出:

# while True:
#     try:
#         num=float(input('请输入一个数字：'))
#         if num==0:
#             print('输入的数字是零')
#         elif num>0:
#             print('输入的数字是正数')
#         else:
#             print('输入的数字是负数')
#         break
#     except ValueError:
#         print('输入无效，需要输入一个数字')
