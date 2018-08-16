# Python3 条件控制
# Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
# if 语句
# Python中if语句的一般形式如下所示：
# if condition_1:
#     statement_block_1
# elif condition_2:
#     statement_block_2
# else:
#     statement_block_3
# 如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
# 如果 "condition_1" 为False，将判断 "condition_2"
# 如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
# 如果 "condition_2" 为False，将执行"statement_block_3"块语句
# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
# 注意：
# 1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
# 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
# 3、在Python中没有switch – case语句。

# 实例
# 以下是一个简单的 if 实例：
# #!/usr/bin/python3
# var1 = 100
# if var1:
#     print ("1 - if 表达式条件为 true")
#     print (var1)
# var2 = 0
# if var2:
#     print ("2 - if 表达式条件为 true")
#     print (var2)
# print ("Good bye!")
# 执行以上代码，输出结果为：
# 1 - if 表达式条件为 true
# 100
# Good bye!
# 从结果可以看到由于变量 var2 为 0，所以对应的 if 内的语句没有执行。
# 以下实例演示了狗的年龄计算判断：
# 实例
# #!/usr/bin/python3
# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age -2)*5
#     print("对应人类年龄: ", human)
# ### 退出提示
# input("点击 enter 键退出")
# 将以上脚本保存在dog.py文件中，并执行该脚本：
# $ python3 dog.py 
# 请输入你家狗狗的年龄: 1
# 相当于 14 岁的人。
# 点击 enter 键退出
# 以下为if中常用的操作运算符:
# 操作符	描述
# <	小于
# <=	小于或等于
# >	大于
# >=	大于或等于
# ==	等于，比较对象是否相等
# !=	不等于
# 实例
# #!/usr/bin/python3
# # 程序演示了 == 操作符
# # 使用数字
# print(5 == 6)
# # 使用变量
# x = 5
# y = 8
# print(x == y)
# 以上实例输出结果：
# False
# False
# high_low.py文件演示了数字的比较运算：
# 实例
# #!/usr/bin/python3 
# # 该实例演示了数字猜谜游戏
# number = 7
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

# 执行以上脚本，实例输出结果如下：
# $ python3 high_low.py 
# 数字猜谜游戏!
# 请输入你猜的数字：1
# 猜的数字小了...
# 请输入你猜的数字：9
# 猜的数字大了...
# 请输入你猜的数字：7
# 恭喜，你猜对了！
# if 嵌套
# 在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
# if 表达式1:
#     语句
#     if 表达式2:
#         语句
#     elif 表达式3:
#         语句
#     else:
#         语句
# elif 表达式4:
#     语句
# else:
#     语句
# 实例
# # !/usr/bin/python3
# num=int(input("输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print ("你输入的数字可以整除 2 和 3")
#     else:
#         print ("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num%3==0:
#         print ("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print  ("你输入的数字不能整除 2 和 3")
# 将以上程序保存到 test_if.py 文件中，执行后输出结果为：
# $ python3 test.py 
# 输入一个数字：6
# 你输入的数字可以整除 2 和 3

# 7 篇笔记:
#    小奈

#   734***009@qq.com

# 以下实例 x 为 0-99 取一个数，y 为 0-199 取一个数,如果 x>y 则输出 x，如果 x 等于 y 则输出 x+y，否则输出y。

# #!/usr/bin/python3
# import random

# x = random.choice(range(100))
# y = random.choice(range(200))
# if x > y:
#     print('x:',x)
# elif x == y:
#     print('x+y:', x + y)
# else:
#     print('y:',y)
# 小奈
#    小奈

#   734***009@qq.com

# 1年前 (2017-03-30)
#    kein

#   201***63.com

# #!/usr/bin/python3

# """对上面例子的一个扩展"""

# print("=======欢迎进入狗狗年龄对比系统========")
# while True:
#     try:
#         age = int(input("请输入您家狗的年龄:"))
#         print(" ")
#         age = float(age)
#         if age < 0:
#             print("您在逗我？")
#         elif age == 1:
#             print("相当于人类14岁")
#             break
#         elif age == 2:
#             print("相当于人类22岁")
#             break
#         else:
#             human = 22 + (age - 2)*5
#             print("相当于人类：",human)
#             break
#     except ValueError:
#         print("输入不合法，请输入有效年龄")
# ###退出提示
# input("点击 enter 键退出")
# kein
#    kein

#   201***63.com

# 1年前 (2017-06-14)
#    阿科

#   121***125@qq.com

# 数字猜谜游戏优化

# print('二、数字猜谜游戏')
# print('数字猜谜游戏！')

# a = 1
# i = 0
# while a != 20:
#    a = int (input ('请输入你猜的数字：'))
#    i += 1    
#    if a == 20:
#       if i<3:
#          print('真厉害，这么快就猜对了！')
#       else :
#          print('总算猜对了，恭喜恭喜！')
#    elif a < 20:
#       print('你猜的数字小了，不要灰心，继续努力！')
#    else :
#       print('你猜的数字大了，不要灰心，继续加油！')
# 阿科
#    阿科

#   121***125@qq.com

# 11个月前 (08-09)
#    小叶

#   shi***0415@163.com

# #!/usr/bin/python3

# # 继续扩展，加入用户提示判断是否退出还是继续

# print("=======欢迎进入狗狗年龄对比系统========")
# control = "N"
# while control=="N":
#     try:
#         age = int(input("请输入您家狗的年龄:"))
#         #print(" ")
#         age = float(age)
#         if age < 0:
#             print("您在逗我？")
#         elif age == 1:
#             print("相当于人类14岁")
#             #break
#         elif age == 2:
#             print("相当于人类22岁")
#             #break
#         else:
#             human = 22 + (age - 2)*5
#             print("相当于人类：",human)
#             #break
#     except ValueError:
#         print("输入不合法，请输入有效年龄")
#     print("")
#     control = input("退出(Y/N)？")
#     print("")
# ###退出提示
# input("点击 enter 键退出")
# 小叶
#    小叶

#   shi***0415@163.com

# 3个月前 (04-16)
#    米老鼠

#   468***534@qq.com

# 条件为假：0, false, '', None, 例子如下：

# >>> a=0
# >>> if a:
# ...     print(11)
# ... else:
# ...     print(22)
# ...
# 22

# >>> a=None
# >>> if a:
# ...     print(11)
# ... else:
# ...     print(22)
# ...
# 22
# >>>
# 条件为真：不为 0, True, 'None', 字符串不为空串

# >>> a=2
# >>> if a:
# ...     print(11)
# ... else:
# ...     print(22)
# ...
# 11
# >>> a="None"
# >>> if a:
# ...     print(11)
# ... else:
# ...     print(22)
# ...
# 11
# >>> a='bbbb'
# >>> if a:
# ...     print(11)
# ... else:
# ...     print(22)
# ...
# 11
# >>>
# 米老鼠
#    米老鼠

#   468***534@qq.com

# 2个月前 (04-22)
#    JIECAO

#   shi***lingmail@vip.qq.com

# 使用判断语句来实现 BMI 的计算。

# BMI 指数（即身体质量指数，简称体质指数又称体重，英文为 Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字

# #!/usr/bin/env python3

# print('----欢迎使用BMI计算程序----')
# name=input('请键入您的姓名:')
# height=eval(input('请键入您的身高(m):'))
# weight=eval(input('请键入您的体重(kg):'))
# gender=input('请键入你的性别(F/M)')
# BMI=float(float(weight)/(float(height)**2))
# #公式
# if BMI<=18.4:
#     print('姓名:',name,'身体状态:偏瘦')
# elif BMI<=23.9:
#     print('姓名:',name,'身体状态:正常')
# elif BMI<=27.9:
#     print('姓名:',name,'身体状态:超重')
# elif BMI>=28:
#     print('姓名:',name,'身体状态:肥胖')
# import time;
# #time模块
# nowtime=(time.asctime(time.localtime(time.time())))
# if gender=='F':
#     print('感谢',name,'先生在',nowtime,'使用本程序,祝您身体健康!')
# if gender=='M':
#     print('感谢',name,'女士在',nowtime,'使用本程序,祝您身体健康!')
# JIECAO
#    JIECAO

#   shi***lingmail@vip.qq.com

# 2周前 (06-21)
#    babeimi

#   xia***i3941@hotmail.com

#    参考地址

# 下表列出了不同数值类型的 true 和 false 情况：

# 类型	False	True
# 布尔	False(与0等价)	True(与1等价)
# 数值	0,   0.0	非零的数值
# 字符串	'',  ""(空字符串)	非空字符串
# 容器	[],  (),  {},  set()	至少有一个元素的容器对象
# None	None	非None对象