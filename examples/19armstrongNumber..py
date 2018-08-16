# Python 阿姆斯特朗数
# Document 对象参考手册 Python3 实例

# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

# 以下代码用于检测用户输入的数字是否为阿姆斯特朗数：

# 实例(Python 3.0+)
# # Filename : test.py
# # author by : www.runoob.com
 
# # Python 检测用户输入的数字是否为阿姆斯特朗数
 
# # 获取用户输入的数字
# num = int(input("请输入一个数字: "))
 
# # 初始化变量 sum
# sum = 0
# # 指数
# n = len(str(num))
 
# # 检测
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** n
#    temp //= 10
 
# # 输出结果
# if num == sum:
#    print(num,"是阿姆斯特朗数")
# else:
#    print(num,"不是阿姆斯特朗数")
# 执行以上代码输出结果为：

# $ python3 test.py 
# 请输入一个数字: 345
# 345 不是阿姆斯特朗数

# $ python3 test.py 
# 请输入一个数字: 153
# 153 是阿姆斯特朗数

# $ python3 test.py 
# 请输入一个数字: 1634
# 1634 是阿姆斯特朗数
# 获取指定期间内的阿姆斯特朗数
# 实例(Python 3.0+)
# # Filename ：test.py
# # author by : www.runoob.com
 
# # 获取用户输入数字
# lower = int(input("最小值: "))
# upper = int(input("最大值: "))
 
# for num in range(lower,upper + 1):
#    # 初始化 sum
#    sum = 0
#    # 指数
#    n = len(str(num))
 
#    # 检测
#    temp = num
#    while temp > 0:
#        digit = temp % 10
#        sum += digit ** n
#        temp //= 10
 
#    if num == sum:
#        print(num)
# 执行以上代码输出结果为：

# 最小值: 1
# 最大值: 10000
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# 1634
# 8208
# 9474
# 以上实例中我们输出了 1 到 10000 之间的阿姆斯特朗数。

# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 3 篇笔记
#    大庆

#   daq***.lee@hotmail.com

# 参考方法：

# # 获取小于指定数字的阿姆斯特朗数
# num = int(input("pleace input a number: "))
# sum=0
# i=0
# arr=[0,0,0,0,0]
# print(num)
# for k in range(1,num):
#     n = len(str(k))
#     m = n;
#     #print(m,"->",k,"\n");
#     i=0;
#     sum=0
#     while m > 0:
#         m -= 1
#         arr[i] = int(k / 10 ** m) % 10
#         sum += arr[i] **n
#         i += 1
#     if k==sum:
#         print(k,end=",")
# 大庆
#    大庆

#   daq***.lee@hotmail.com

# 11个月前 (07-27)
#    亻

#   728***567@qq.com

# 参考方法：

# #以下代码用于检测用户输入的数字是否为阿姆斯特朗数
# import math

# x=int(input('请输入一个正整数:'))
# x1=x
# n=len(str(x))
# p=0
# for i in range(1,n+1):
#     y=math.floor(x//pow(10,n-i))
#     print(y,end=',')
#     m=pow(y,n)# 也可以表达为:   m=y**n
#     p=m+p
#     x=x%pow(10,n-i)
# print(p)
# if p == x1:
#     print('输入的数字 %d 是一个阿姆斯特朗数'%x1)
# elif p!=x1:
#     print('输入的数字 %d 不是一个阿姆斯特朗数'%x1)
# 亻
#    亻

#   728***567@qq.com

# 11个月前 (08-14)
#    Santana

#   378***941@qq.com

# 获取指定期间内的阿姆斯特朗数

# lower=int(input("Please input a number: "))
# upper=int(input("Please input a number: "))
# sum=0
# for num in range(lower,upper):
#     l = len(str(num))
#     for n in str(num):
#         sum=sum+int(n)**l
#     if num==sum:
#         print(num)
#     sum=0
