# Python 十进制转二进制、八进制、十六进制
# Document 对象参考手册 Python3 实例

# 以下代码用于实现十进制转二进制、八进制、十六进制：

# # -*- coding: UTF-8 -*-

# # Filename : test.py
# # author by : www.runoob.com

# # 获取用户输入十进制数
# dec = int(input("输入数字："))

# print("十进制数为：", dec)
# print("转换为二进制为：", bin(dec))
# print("转换为八进制为：", oct(dec))
# print("转换为十六进制为：", hex(dec))
# 执行以上代码输出结果为：

# python3 test.py 
# 输入数字：5
# 十进制数为：5
# 转换为二进制为： 0b101
# 转换为八进制为： 0o5
# 转换为十六进制为： 0x5
# python3 test.py 
# 输入数字：12
# 十进制数为：12
# 转换为二进制为： 0b1100
# 转换为八进制为： 0o14
# 转换为十六进制为： 0xc
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 1 篇笔记
#    Stack Overflow

#   530***193@qq.com

# 具体实现

# 十进制到二进制：

# def dec2bin(num):
#     l = []
#     if num < 0:
#         return '-' + dec2bin(abs(num))
#     while True:
#         num, remainder = divmod(num, 2)
#         l.append(str(remainder))
#         if num == 0:
#             return ''.join(l[::-1])
# 十进制到八进制：

# def dec2oct(num):
#     l = []
#     if num < 0:
#         return '-' + dec2oct(abs(num))
#     while True:
#         num, remainder = divmod(num, 8)
#         l.append(str(remainder))
#         if num == 0:
#             return ''.join(l[::-1])
# 十进制到十六进制：

# base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
# def dec2hex(num):
#     l = []
#     if num < 0:
#         return '-' + dec2hex(abs(num))
#     while True:
#         num,rem = divmod(num, 16)
#         l.append(base[rem])
#         if num == 0:
#             return ''.join(l[::-1])