# Python 九九乘法表
# Document 对象参考手册 Python3 实例

# 以下实例演示了如何实现九九乘法表：

# 实例
# # -*- coding: UTF-8 -*-
 
# # Filename : test.py
# # author by : www.runoob.com
 
# # 九九乘法表
# for i in range(1, 10):
#         for j in range(1, i+1):
#             print('{}x{}={}\t'.format(i, j, i*j), end='')
#         print()
# 执行以上代码输出结果为：

# 1x1=1
# 2x1=2   2x2=4
# 3x1=3   3x2=6   3x3=9
# 4x1=4   4x2=8   4x3=12  4x4=16
# 5x1=5   5x2=10  5x3=15  5x4=20  5x5=25
# 6x1=6   6x2=12  6x3=18  6x4=24  6x5=30  6x6=36
# 7x1=7   7x2=14  7x3=21  7x4=28  7x5=35  7x6=42  7x7=49
# 8x1=8   8x2=16  8x3=24  8x4=32  8x5=40  8x6=48  8x7=56  8x8=64
# 9x1=9   9x2=18  9x3=27  9x4=36  9x5=45  9x6=54  9x7=63  9x8=72  9x9=81
# 通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。

# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 6 篇笔记
#    inernoro

#   ine***ro@163.com

# 乘法表左边的数要比右边的小，如下实例:

# #!/usr/bin/python3

# class multiplicationTable():
#     def paint(self,n=9): 
#         for row in range(1,n+1):  
#             for col in range(1,row+1):
#                 print("{1}x{0}={2}\t".format(row , col , row*col),end='')
#             print();

# table = multiplicationTable()
# table.paint()
# #table.paint(10) #打印 "10x10" 的乘法表
# inernoro
#    inernoro

#   ine***ro@163.com

# 1年前 (2017-05-31)
#    TwoIceBing

#   139***2736@qq.com

# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if i == j:
#             print('{1}×{0}={2}'.format(i, j, i * j))
#         else:
#             print('{1}×{0}={2}'.format(i, j, i * j), end='\t')
# 这样写可以有效去除每一行的最后一个空格,输出如下：

# TwoIceBing
#    TwoIceBing

#   139***2736@qq.com

# 7个月前 (12-07)
#    姬无命

#   305***5816@qq.com

# 一句话输出99乘法表，可以参考一下：

# print('\n'.join(' '.join("%dx%d=%-2d" % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)))
# 姬无命
#    姬无命

#   305***5816@qq.com

# 5个月前 (02-07)
#    Jim

#   wel***520@163.com

# 参考：

# for i in range(1,10):
#     for j in range(1,i):
#         print "%dx%d=%d" % (j,i,j*i),
#     print
# Jim
#    Jim

#   wel***520@163.com

# 2个月前 (05-08)
#    xjsnight

#   267***4445@qq.com

# 用列表生成器打印九九乘法表:
# >>> print '\n'.join(['\t'.join(['%d * %d = %d'%(y,x,x*y) for y in range(1,x+1)])for x in range(1,10)])
# 1 * 1 = 1
# 1 * 2 = 2    2 * 2 = 4
# 1 * 3 = 3    2 * 3 = 6    3 * 3 = 9
# 1 * 4 = 4    2 * 4 = 8    3 * 4 = 12    4 * 4 = 16
# 1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
# 1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
# 1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
# 1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
# 1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
# xjsnight
#    xjsnight

#   267***4445@qq.com

# 2个月前 (05-08)
#    门外汉

#   906***770@qq.com

# 分享给像我这种门外汉，稍微好理解一些，Python3 支持中文变量真好。

# for 行 in range(1,10):
#     for 列 in range(1,行+1):  # 内循环中，确保列 <= 行。
#         print("{}*{}={}\t".format(列,行,列*行),end="")   # 确保同一行内容连续
#     print()     # 另起一行！！！

# input() # 防止程序一闪而过，不在编译器中也能使用