# Python 获取最大值函数
# Document 对象参考手册 Python3 实例

# 以下实例中我们使用max()方法求最大值：

# 实例(Python 3.0+)
# # -*- coding: UTF-8 -*-
 
# # Filename : test.py
# # author by : www.runoob.com
 
# # 最简单的
# print(max(1, 2))
# print(max('a', 'b'))
 
# # 也可以对列表和元组使用
# print(max([1,2]))
# print(max((1,2)))
 
# # 更多实例
# print("80, 100, 1000 最大值为: ", max(80, 100, 1000))
# print("-20, 100, 400最大值为: ", max(-20, 100, 400))
# print("-80, -20, -10最大值为: ", max(-80, -20, -10))
# print("0, 100, -400最大值为:", max(0, 100, -400))
# 执行以上代码输出结果为：

# 2
# b
# 2
# 2
# 80, 100, 1000 最大值为:  1000
# -20, 100, 400最大值为:  400
# -80, -20, -10最大值为:  -10
# 0, 100, -400最大值为: 100
# max() 函数介绍：Python max()函数。

# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 2 篇笔记
#    小辉

#   447***407@qq.com

# # 对比任意多个数字的大小
# 参考：

# N = int(input('输入需要对比大小数字的个数：'))
# print("请输入需要对比的数字：")
# num = []
# for i in range(1,N+1):
#     temp = int(input('输入第 %d 个数字' % i))
#     num.append (temp)

# print('您输入的数字为：',num)
# print('最大值为：',max(num))
# 小辉
#    小辉

#   447***407@qq.com

# 6个月前 (12-23)
#    mahu

#   wuc***gang66@163.com

# 参考方法：

# N = int(input('输入需要对比大小数字的个数：\n'))

# num=[ int(input('请输入第 %d 个对比数字 \n'%(i)))for i in range(1,N+1)]

# print('您输入的数字为:',list(num))
# print('最大值为: ',max(num))