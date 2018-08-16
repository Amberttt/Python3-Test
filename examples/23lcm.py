# Python 最小公倍数算法
# Document 对象参考手册 Python3 实例

# 以下代码用于实现最小公倍数算法：

# 实例(Python 3.0+)
# # Filename : test.py
# # author by : www.runoob.com
 
# # 定义函数
# def lcm(x, y):
 
#    #  获取最大的数
#    if x > y:
#        greater = x
#    else:
#        greater = y
 
#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1
 
#    return lcm
 
 
# # 获取用户输入
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
 
# print( num1,"和", num2,"的最小公倍数为", lcm(num1, num2))
# 执行以上代码输出结果为：

# 输入第一个数字: 54
# 输入第二个数字: 24
# 54 和 24 的最小公倍数为 216
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 7 篇笔记
#    HaydnLiao

#   Hay***iao@163.com

# 按以下思路可减少循环次数：

# 1.当最大值为最小公倍数时，返回最大值；

# 2.当最大值不为最小公倍数时，最小公倍数为最大值的倍数。

# 实例：

# # 最小公倍数
# def lcm(a, b):
#     if b > a:
#         a, b = b, a     # a为最大值
#     if a % b == 0:
#         return a        # 判断a是否为最小公倍数
#     mul = 2             # 最小公倍数为最大值的倍数
#     while a*mul % b != 0:
#         mul += 1
#     return a*mul

# while(True):
#     a = int(input("Input 'a':"))
#     b = int(input("Input 'b':"))
#     print(lcm(a, b))
# HaydnLiao
#    HaydnLiao

#   Hay***iao@163.com

# 1年前 (2017-07-02)
#    Joshua

#   cos***cosmos@163.com

# 参考方法:

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# def lcm(x, y): # very fast
#     s = x*y
#     while y: x, y = y, x%y
#     return s//x
# print(lcm(120, 123)) #result: 4920
# Joshua
#    Joshua

#   cos***cosmos@163.com

# 12个月前 (07-19)
#    旅行的意义

#   101***7869@qq.com

# 利用最大公约数，最小公倍数等于两个数的乘积除以最大公约数:

# def my_lcm():
#     n1 = int(input('请输入一个正整数：'))
#     n2 = int(input('请输入另一个正整数：'))
#     temp1 = n1
#     temp2 = n2
#     if n1 == 0:
#         n1, n2 = n2, n1
#     while n2 != 0:
#         n1, n2 = n2, n1 % n2
#     return int(temp1 * temp2 / n1)

# print(my_lcm())
# 旅行的意义
#    旅行的意义

#   101***7869@qq.com

# 5个月前 (02-05)
#    黄桃果捞

#   zhe***ao@126.com

# 可以借用前一个实例中求取最小公约数的代码来实现求解两个整数的最大公倍数，代码如下：

# #!/usr/bin/python3
# # -*- coding: UTF-8 -*-
# # find the Least Common Multiple of two integer

# def find_GCD(x, y):
#   find_GCD = y
#   while (x % y) != 0:
#     find_GCD = x % y
#     x, y = y, find_GCD
#   return find_GCD

# def find_LCM(x,y):
#     return int(x * y / find_GCD(x, y))

# int1 = int(input('Input 1st integer: '))
# int2 = int(input('Input 2nd integer: '))

# print('The least common multiple of {} and {} is {}'.format(int1, int2, find_LCM(int1, int2)))
# 代码运行结果如下：

# Input 1st integer: 54
# Input 2nd integer: 24
# The least common multiple of 54 and 24 is 216
# 黄桃果捞
#    黄桃果捞

#   zhe***ao@126.com

# 4个月前 (03-20)
#    星空中的鱼

#   357***689@qq.com

# 你这个实例的效率太慢了，这样写效率高些。

# def lcm(X,Y):
#     count=1;
#     if X > Y:
#         sample=X
#     else:
#         sample=Y
#     while True:
#         lcm=sample*count
#         if (lcm % X ==0)and( lcm % Y  ==0):
#             return lcm
#         else:
#             count+=1
# 星空中的鱼
#    星空中的鱼

#   357***689@qq.com

# 3个月前 (04-16)
#    gj

#   123***789@qq.com

# 使用 for 的方法：

# def lcm(x,y):
#     if x>y:
#         greater = x
#     else:
#         greater = y
#     for i in range(greater,x*y+1,1):
#         if(i%x==0) and (i%y==0):
#             lcm = i
#             break
#     return lcm   

# num1 = int(input('输入第一个数字：'))
# num2 = int(input('输入第二个数字：'))
# print(num1,'和',num2,'的最小公倍数为',lcm(num1,num2))
# gj
#    gj

#   123***789@qq.com

# 3周前 (06-12)
#    桃之夭夭

#   956***900@qq.com

# 求两个数之间的最小公倍数相对简单，用两个数的乘积对两个之间的最大公约数求商即可:

# def gcd(a,b):
#     while (a!=0) & (b!=0):
#         a,b = b,a%b
#     return a

# c = int(input('请输入第一个正整数: '))
# d = int(input('请输入第一个正整数:'))
# print('{}和{}的最小公倍数为: {}'.format(c,d,(c*d)//gcd(c,d)))