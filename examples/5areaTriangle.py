# Python 计算三角形的面积
# Document 对象参考手册 Python3 实例

# 以下实例为通过用户输入三角形三边长度，并计算三角形的面积：

# 实例(Python 3.0+)
# # -*- coding: UTF-8 -*-
 
# # Filename : test.py
# # author by : www.runoob.com
 
 
# a = float(input('输入三角形第一边长: '))
# b = float(input('输入三角形第二边长: '))
# c = float(input('输入三角形第三边长: '))
 
# # 计算半周长
# s = (a + b + c) / 2
 
# # 计算面积
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print('三角形面积为 %0.2f' %area)
# 执行以上代码输出结果为：

# $ python test.py 
# 输入三角形第一边长: 5
# 输入三角形第二边长: 6
# 输入三角形第三边长: 7
# 三角形面积为 14.70
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 4 篇笔记
#    除了0还有1吖

#   138***83182@163.com

# 加上判断三角形能否构成的条件：

# #实例四：计算三角形面积

# a = float (input ('输入三角形第一边长：'))
# b = float (input ('输入三角形第二边长：'))
# c = float (input ('输入三角形第三边长：'))
# while a+b<c or a+c<b or b+c<a:
#     print ('输入的边构不成三角形，请重新输入！')
#     a = float (input ('输入三角形第一边长：'))
#     b = float (input ('输入三角形第二边长：'))
#     c = float (input ('输入三角形第三边长：'))

# s = (a+b+c) /2
# area = (s*(s-a)*(s-b)*(s-c))**0.5
# print ('三角形面积为：%0.2f'%area)
# 除了0还有1吖
#    除了0还有1吖

#   138***83182@163.com

# 10个月前 (09-22)
#    liZONLi

#   104***5705@qq.com

# 参考方法：

# #计算三角形面积
# while(True):
#     triangle = input('输入三角形三边(如10,6,8):')
#     sides = [int(side) for side in triangle.split(',')]
#     a,b,c = sides

# #判断输入的三角形是否合法
#     if a + b > c and a + c > b and b + c > a :
#        s = a * b * (1-((a**2 + b**2 - c**2)/(2*a*b))**2) ** 0.5/2
#        print('三角形({0[0]},{0[1]},{0[2]})的面积是：{1}'.format(sides,s))
#        break
#     else:
#        print('三角形不合法')
# liZONLi
#    liZONLi

#   104***5705@qq.com

# 9个月前 (09-24)
#    ryan

#   lia***35@163.com

# Python3 下测试：

# while True:
#     triangle = input('输入三角形三边(如10,6,8):')
#     sides = [float(side) for side in triangle.split(',')]
#     a,b,c = sides
    
# #判断输入的三角形是否合法
#     if a + b > c and a + c > b and b + c > a :
#        l = (a + b + c)/2
#        s = (l*(l-a)*(l-b)*(l-c))** 0.5
#        print('三角形({0[0]},{0[1]},{0[2]})的面积是：{1:.2f}'.format(sides,s))
#        break
#     else:
#        print('三角形不合法')
# ryan
#    ryan

#   lia***35@163.com

# 3个月前 (04-11)
#    傻瓜+笨蛋

#   271***345@qq.com

# 参考方法：

# # 通过用户输入三角形三边长度，并计算三角形的面积
# # 已知三角形三边a,b,c，则
# # （海伦公式）（p=(a+b+c)/2）
# # S=sqrt[p(p-a)(p-b)(p-c)]
# # =sqrt[(1/16)(a+b+c)(a+b-c)(a+c-b)(b+c-a)]
# # =1/4sqrt[(a+b+c)(a+b-c)(a+c-b)(b+c-a)]

# import math
# import unicodedata
# # 定义函数判断输入数据是否为数字
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#         unicodedata.digit(s)    # digit 把一个合法的数字字符串转换为数字值
#         return True
#     except (TypeError, ValueError):
#         pass
#     return False
# def calculate(a, b, c):
#     if is_number(a) and is_number(b) and is_number(c):
#         a = float(a)
#         b = float(b)
#         c = float(c)
#         if a > 0  and b > 0 and c >0:
#             while a+b<=c or a+c<=b or b+c<=a:
#                 print("输入的边长无法构成三角形！！！")
#                 a = input('输入三角形边长a: ')
#                 b = input('输入三角形边长b: ')
#                 c = input('输入三角形边长c: ')
#                 calculate(a,b,c)
#             p = (a+b+c)/2
#             area = math.sqrt(p*(p - a)*(p - b)*(p - c))
#             print("三角形面积为：%0.2f" %area)
#         else:
#             print("三角形的边长必须大于0，请输入大于0的数！！！")
#     else:
#         print('请输入数字类型！！！')
# a = input('输入三角形边长a: ')
# b = input('输入三角形边长b: ')
# c = input('输入三角形边长c: ')
# calculate(a,b,c)