# Python 阶乘实例
# Document 对象参考手册 Python3 实例

# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。

# 实例
# #!/usr/bin/python3
 
# # Filename : test.py
# # author by : www.runoob.com
 
# # 通过用户输入数字计算阶乘
 
# # 获取用户输入的数字
# num = int(input("请输入一个数字: "))
# factorial = 1
 
# # 查看数字是负数，0 或 正数
# if num < 0:
#    print("抱歉，负数没有阶乘")
# elif num == 0:
#    print("0 的阶乘为 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("%d 的阶乘为 %d" %(num,factorial))
# 执行以上代码输出结果为：

# 请输入一个数字: 3
# 3 的阶乘为 6
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 3 篇笔记
#    shohong

#   210***6254@qq.com

# 参考方法：

# #!/usr/bin/python3

# from functools import reduce

# sum=reduce(lambda x,y:x*y,range(1,7))
# print(sum)
# shohong
#    shohong

#   210***6254@qq.com

# 1年前 (2017-06-07)
#    Pt

#   idi***g@qq.com

# 查了一下 math 库的帮助，发现自带阶乘函数。所以代码可以简洁一点。

# # -*- coding: UTF-8 -*-

# # Filename : factorial.py
# # author : Pt

# import math
# num = int(input("请输入一个数字："))
# if num < 0:
#     print("负数是没有阶乘的！")
# else:
#     print("{0} 的阶乘为 {1}".format(num, math.factorial(num)))
# Pt
#    Pt

#   idi***g@qq.com

# 9个月前 (10-04)
#    ben

#   bj0***0514@126.com

# 递归实现

# def factorial(n):
#     if n > 1:
#         return n*factorial(n-1)
#     return 1
# while True:
#     try:
#         n = input("请输入一个数字(输入 q 退出):")
#         if n == "q":
#             break
#         n = int(n)
#         if n < 1:
#             raise ValueError
#         x = factorial(n)
#         print(x)
#     except ValueError:
#         print("不是一个正数")
