# Python 最大公约数算法
# Document 对象参考手册 Python3 实例

# 以下代码用于实现最大公约数算法：

# 实例(Python 3.0+)
# # Filename : test.py
# # author by : www.runoob.com
 
# # 定义一个函数
# def hcf(x, y):
#    """该函数返回两个数的最大公约数"""
 
#    # 获取最小值
#    if x > y:
#        smaller = y
#    else:
#        smaller = x
 
#    for i in range(1,smaller + 1):
#        if((x % i == 0) and (y % i == 0)):
#            hcf = i
 
#    return hcf
 
 
# # 用户输入两个数字
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
 
# print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))
# 执行以上代码输出结果为：

# 输入第一个数字: 54
# 输入第二个数字: 24
# 54 和 24 的最大公约数为 6
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 7 篇笔记
#    HaydnLiao

#   Hay***iao@163.com

# 可按以下思路减少循环次数：

# 1. 当最小值为最大公约数时，直接返回；

# 2. 当最小值不为最大公约数时，最大公约数不会大于最小值的1/2；

# 3. 求最大公约数理应从大到小循环递减求最大。

# 实例：

# def gcd(a, b):
#     if b > a:
#         a, b = b, a   # b为最小值
#     if a % b == 0:
#         return b      # 判断b是否为最大公约数
#     for i in range(b//2+1, 1, -1):    # 倒序求最大公约数更合理
#         if b % i == 0 and a % i == 0:
#             return i
#     return 0

# while(True):
#     a = int(input("Input 'a':"))
#     b = int(input("Input 'b':"))
#     print(gcd(a, b))
# HaydnLiao
#    HaydnLiao

#   Hay***iao@163.com

# 1年前 (2017-07-02)
#    Joshua

#   cos***cosmos@163.com

# 参考方法：

# def gcd(x, y): # very fast
#    return x if y == 0 else gcd(y, x%y)

# print(gcd(378, 5940))  # result: 54
# Joshua
#    Joshua

#   cos***cosmos@163.com

# 12个月前 (07-19)
#    thinrock

#   thi***cker@gmail.com

# 参考方法：

# x = int(input('请输入第一个数:'))
# y = int(input('请输入第二个数:'))
# for i in range(1,min(x,y) + 1):
#     if (y % i == 0) & (x % i == 0):
#         divisor = i
# print(divisor)
# thinrock
#    thinrock

#   thi***cker@gmail.com

# 11个月前 (08-17)
#    Santana

#   378***941@qq.com

# 从大到小一个一个计算：

# n1=int(input("input a number: "))
# n2=int(input("input another number: "))
# if n1<n2:
#     smaller=n1
# else:
#     smaller=n2
# while True:
#     if (n1%smaller==0) and (n2%smaller==0):
#         print(smaller)
#         break
#     smaller-=1
# Santana
#    Santana

#   378***941@qq.com

# 10个月前 (09-09)
#    susion

#   245***1461@qq.com

# 两个数的最大公约数可以使用 欧几里得算法实现。即两个数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数。

# def gcd(a, b):
#   if a == 0:
#     a, b = b, a
#   while b != 0:
#     a, b = b, a % b
#   return a

# print(gcd(54, 24))
# susion
#    susion

#   245***1461@qq.com

# 9个月前 (10-15)
#    黄桃果捞

#   zhe***ao@126.com

# 可以利用辗转相除的方法实现求两个正数的最大公约数，代码如下：

# #!/usr/bin/python3
# # -*- coding: UTF-8 -*-

# # find the greatest common divisor of two integer

# def find_GCD(x, y):
#   find_GCD = y
#   while (x % y) != 0:
#     find_GCD = x % y
#     x, y = y, find_GCD
#   return find_GCD

# int1 = int(input('Input 1st integer: '))
# int2 = int(input('Input 2nd integer: '))

# print('The greatest common divisor of {} and {} is {}'.format(int1, int2, find_GCD(int1, int2)))
# 代码运行结果如下：

# Input 1st integer: 54
# Input 2nd integer: 24
# The greatest common divisor of 54 and 24 is 6
# 黄桃果捞
#    黄桃果捞

#   zhe***ao@126.com

# 4个月前 (03-20)
#    桃之夭夭

#   956***900@qq.com

# 欧几得里算法的完善版，输入任意两个整数，求最大公约数。

# def gcd(a,b):
#     if a == 0:
#         a,b = b,a
#     while b != 0:
#         a,b = b,a%b
#     return a

# c = int(input('请输入第一个正整数: '))
# d = int(input('请输入第二个正整数: '))

# if c>d:
#    b = d
# else:
#    b = c

# print('{}和{}的最大公约数为: {}'.format(c,d,gcd(c,d)))