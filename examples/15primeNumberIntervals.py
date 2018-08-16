# Python 输出指定范围内的素数
# Document 对象参考手册 Python3 实例

# 素数（prime number）又称质数，有无限个。除了1和它本身以外不再被其他的除数整除。

# 以下实例可以输出指定范围内的素数：

# 实例(Python 3.0+)
# #!/usr/bin/python3
 
# # 输出指定范围内的素数
 
# # take input from the user
# lower = int(input("输入区间最小值: "))
# upper = int(input("输入区间最大值: "))
 
# for num in range(lower,upper + 1):
#     # 素数大于 1
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)
# 执行以上程序，输出结果为：

# $ python3 test.py 
# 输入区间最小值: 1
# 输入区间最大值: 100
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97

# 3 篇笔记
#    hizmz

#   hiz***sina.com

# 与前面判断是否是质数一样，作者算法中未使用到"开根号法"来节约时间复杂度，同时为加入个数等说明，因此我对其改进如下：

# import math

# # 输出指定范围内的素数
# # 用户输入范围
# lower = int(input("输入区间最小值: "))
# upper = int(input("输入区间最大值: "))
# print("素数结果如下：")
# print("="*10)
# pri_num = 0
# com_num = 0
# for num in range(lower, upper + 1):
#     # 找到其平方根（ √ ），减少算法时间
#     square_num = math.floor(num ** 0.5)
#     # 素数大于 1
#     if num > 1:
#         for i in range(2, (square_num + 1)):
#             if (num % i) == 0:
#                 com_num += 1
#                 break
#         else:
#             pri_num += 1
#             print(num)
# print("="*10)
# print(com_num,'个合数')
# print(pri_num,'个素数')
# hizmz
#    hizmz

#   hiz***sina.com

# 10个月前 (09-14)
#    Pt

#   idi***g@qq.com

# 先定义一个判断素数的函数，然后再输入范围去判断。

# # -*- coding: UTF-8 -*-

# # Filename : defprime.py
# # author ：Pt

# def isprime(x):
#     if x == 1:
#         return False
#     k = int(x**0.5)
#     for j in range(2, k + 1):
#         if x % j == 0:
#             return False
#     return True
# lower = int(input("请输入区间最小值："))
# upper = int(input("请输入区间最大值："))
# for i in range(lower, upper):
#     if isprime(i):
#         print(i, end = " ")
# Pt
#    Pt

#   idi***g@qq.com

# 9个月前 (10-04)
#    风林火山

#   dra***a_zby@163.com

# prime_number = [x for x in range(int(input('区间最小值：')), int(input('区间最大值：'))) if[] == [y for y in range(2, int(x ** 0.5) + 1) if x % y == 0]]

# print(prime_number)