# Python3 实例
# 以下实例在 Python3.4.3 版本下测试通过：

# Python Hello World 实例
# Python 数字求和
# Python 平方根
# Python 二次方程
# Python 计算三角形的面积
# Python 随机数生成
# Python 摄氏温度转华氏温度
# Python 交换变量
# Python if 语句
# Python 判断字符串是否为数字
# Python 判断奇数偶数
# Python 判断闰年
# Python 获取最大值函数
# Python 质数判断
# Python 输出指定范围内的素数
# Python 阶乘实例
# Python 九九乘法表
# Python 斐波那契数列
# Python 阿姆斯特朗数
# Python 十进制转二进制、八进制、十六进制
# Python ASCII码与字符相互转换
# Python 最大公约数算法
# Python 最小公倍数算法
# Python 简单计算器实现
# Python 生成日历
# Python 使用递归斐波那契数列
# Python 文件 IO
# Python 字符串判断
# Python 字符串大小写转换
# Python 计算每个月天数
# Python 获取昨天日期
# Python list 常用操作
#  Python3 标准库概览 Python3 正则表达式 
# 1 篇笔记
#    连少华

#   cla***class@163.com

#    参考地址

# Python 计算笛卡尔积

# 计算多个集合的笛卡尔积，有规律可循，算法和代码也不难，但是很多语言都没有提供直接计算笛卡尔积的方法，需要自己写大段大段的代码计算笛卡尔积，python 提供了一种最简单的计算笛卡称积的方法(只需要一行代码)，详见下面的代码：

# #!/usr/bin/python3
# # -*- coding: utf-8 -*-
# # @file   : Cartesian.py
# # @author : shlian
# # @date   : 2018/5/29
# # @version: 1.0
# # @desc   : 用python实现求笛卡尔积
# import itertools

# class cartesian(object):
#     def __init__(self):
#         self._data_list=[]

#     def add_data(self,data=[]): #添加生成笛卡尔积的数据列表
#         self._data_list.append(data)

#     def build(self): #计算笛卡尔积
#         for item in itertools.product(*self._data_list):
#             print(item)

# if __name__=="__main__":
#     car=cartesian()
#     car.add_data([1,2,3,4])
#     car.add_data([5,6,7,8])
#     car.add_data([9,10,11,12])
#     car.build()