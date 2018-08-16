# Python 质数判断
# Document 对象参考手册 Python3 实例

# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。


# test.py 文件：
# # -*- coding: UTF-8 -*-
 
# # Filename : test.py
# # author by : www.runoob.com
 
# # Python 程序用于检测用户输入的数字是否为质数
 
# # 用户输入数字
# num = int(input("请输入一个数字: "))
 
# # 质数大于 1
# if num > 1:
#    # 查看因子
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"不是质数")
#            print(i,"乘于",num//i,"是",num)
#            break
#    else:
#        print(num,"是质数")
       
# # 如果输入的数字小于或等于 1，不是质数
# else:
#    print(num,"不是质数")
# 执行以上代码输出结果为：

# $ python3 test.py 
# 请输入一个数字: 1
# 1 不是质数
# $ python3 test.py 
# 请输入一个数字: 4
# 4 不是质数
# 2 乘于 2 是 4
# $ python3 test.py 
# 请输入一个数字: 5
# 5 是质数
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 6 篇笔记
#    hizmz

#   hiz***sina.com

# 原作者的算法基本正确，但时间复杂度较高，在判断一个大数是质数还是合数的情况下，应该在查看因子那里的循环中使用到平方根。代码如下：

# # Python 程序用于检测用户输入的数字是质数还是合数
# import math
# # 用户输入数字
# num = int(input("请输入一个数字: "))
# # 质数大于 1
# if num > 1:
#     # 找到其平方根（ √ ），减少算法时间
#     square_num = math.floor( num ** 0.5 )
#     # 查找其因子
#     for i in range(2, (square_num+1)): #将平凡根加1是为了能取到平方根那个值
#         if (num % i) == 0:
#             print(num, "是合数")
#             print(i, "乘于", num // i, "是", num)
#             break
#     else:
#         print(num, "是质数")
#         # 如果输入的数字小于或等于 1，不是质数
# else:
#     print(num, "既不是质数，也不是合数")
# 原理是用了开根号法：

# 假如一个数N是合数,它有一个约数a,那么有a×b=N

# 则a、b两个数中必有一个大于或等于根号N,一个小于或等于根号N。

# 因此,只要小于或等于根号N的数（1除外）不能整除N,则N一定是素数。

# hizmz
#    hizmz

#   hiz***sina.com

# 10个月前 (09-14)
#    cindyliu

#   916***457@qq.com

# # -*- coding: UTF-8 -*-
  
# #用while循环，进行质数判断
# #输入数字

# num = int(input("输入一个数字："))
# #定义i
# i = 2
# while i < num:
#     s = num % i
#     if s == 0:
#         print("{}能被除的数其中有{}".format(num,i))
#         break
#     else:
#         i += 1
# if num == i:
#     print("是质数")
# else:
#     print("不是质数")
# cindyliu
#    cindyliu

#   916***457@qq.com

# 7个月前 (12-07)
#    TwoIceBing

#   139***2736@qq.com

# 输出1-100以内的质数：

# count = 0
# for i in range(1, 101):
#     for j in range(1, i):
#         if j == i // 2 and i % j == 1 or (i <= 3 and i != 1):
#             if count == 4:
#                 print(i)
#                 count = 0
#             else:
#                 print(i, end='\t')
#                 count += 1
#             break
#         if i % j == 0 and j != 1:
#             break
# TwoIceBing
#    TwoIceBing

#   139***2736@qq.com

# 7个月前 (12-07)
#    zacharyvic

#   194***1924@qq.com

# 用质数表来判断是否为质数

# # -*- coding: UTF-8 -*-
# # Python 程序用于检测用户输入的数字是否为质数
# # 用户输入数字
# num = int(input("请输入一个数字: "))
# # 获取小于等于num平方根的质数表
# def getPrimeList(n, oldPrimeList):
#     for prime in oldPrimeList:
#         if (n % prime) == 0:
#             break
#     if prime == oldPrimeList[-1]:
#         oldPrimeList.append(n)
# # 2,3是质数
# if num == 2 or num == 3:
#     print(num, "是质数")
# # 对大于3的数用质数表来判断
# elif num > 3:
#     judge_num = int(num ** 0.5) + 1
#     primeList = [2]
#     for i in range(2, judge_num):
#         getPrimeList(i, primeList)
#     for i in primeList:
#         if (num % i) == 0:
#             print(num, "不是质数")
#             break
#     else:
#         print(num, "是质数")
# # 如果输入的数字小于或等于 1，不是质数
# else:
#     print(num, "不是质数")
# zacharyvic
#    zacharyvic

#   194***1924@qq.com

# 2个月前 (04-27)
#    freejustin

#   fre***stin@yeah.net

# 参考方法：

# # 用户输入数字
# num = int(input("请输入一个数字: "))
# # 质数大于 1
# if num > 1:
#    # 查看因子
#    for i in range(2, (int(num/2)+1) ):
#        if (num % i) == 0:
#            print(num,"不是质数")
#            print(i,"乘于",num//i,"是",num)
#            break
#    else:
#        print(num,"是质数")
# # 如果输入的数字小于或等于 1，不是质数
# else:
#    print(num,"不是质数")
# freejustin
#    freejustin

#   fre***stin@yeah.net

# 4周前 (06-09)
#    freejustin

#   fre***stin@yeah.net

# 参考方法：

# from math import sqrt

# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True

# # 用户输入数字
# num = int(input("请输入一个数字: "))
# if is_prime(num):
#     print(num,"是质数")
# else:
#     print(num,"不是质数")