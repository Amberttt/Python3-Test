# Python 判断闰年
# Document 对象参考手册 Python3 实例

# 以下实例用于判断用户输入的年份是否为闰年：

# 实例(Python 3.0+)
# # -*- coding: UTF-8 -*-
 
# # Filename : test.py
# # author by : www.runoob.com
 
# year = int(input("输入一个年份: "))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
#        else:
#            print("{0} 不是闰年".format(year))
#    else:
#        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
# else:
#    print("{0} 不是闰年".format(year))
# 我们也可以使用内嵌 if 语句来实现：

# 执行以上代码输出结果为：

# 输入一个年份: 2000
# 2000 是闰年
# 输入一个年份: 2011
# 2011 不是闰年
# Document 对象参考手册 Python3 实例

#  Python3 标准库概览 Python3 正则表达式 
# 1 篇笔记
#    小白

#   531***669@qq.com

# 参考方法：

# #!/usr/bin/python3

# year = int(input("请输入一个年份："))
# if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
#     print("{0}是闰年".format(year))
# else:
#     print("{0}不是闰年".format(year))