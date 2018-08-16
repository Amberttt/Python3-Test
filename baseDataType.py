# !/usr/bin/python3
# Python3 基本数据类型
# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：
# 实例(Python 3.0+)
#!/usr/bin/python3
# counter = 100          # 整型变量
# miles   = 1000.0       # 浮点型变量
# name    = "runoob"     # 字符串
# print (counter)
# print (miles)
# print (name)

# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：
# a = b = c = 1
# 以上实例，创建一个整型对象，值为 1，三个变量都指向同一个内存位置。
# 您也可以为多个对象指定多个变量。例如：
# a, b, c = 1, 2, "runoob"
# 以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

# 标准数据类型
# Python3 中有六个标准的数据类型：
# Number（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Set（集合）
# Dictionary（字典）
# Python3 的六个标准数据类型中：
# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

# Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
# 内置的 type() 函数可以用来查询变量所指的对象类型。
# >>> a, b, c, d = 20, 5.5, True, 4+3j
# >>> print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
# 此外还可以用 isinstance 来判断：
# 实例
# >>>a = 111
# >>> isinstance(a, int)
# True
# >>>

# isinstance 和 type 的区别在于：
# class A:
#     pass
# class B(A):
#     pass
# isinstance(A(), A)  # returns True
# type(A()) == A      # returns True
# isinstance(B(), A)    # returns True
# type(B()) == A        # returns False
# 区别就是:
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
# 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
# 当你指定一个值时，Number 对象就会被创建：
# var1 = 1
# var2 = 10
# 您也可以使用del语句删除一些对象引用。
# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]]
# 您可以通过使用del语句删除单个或多个对象。例如：
# del var
# del var_a, var_b

# 数值运算
# 实例
# >>>5 + 4  # 加法
# 9
# >>> 4.3 - 2 # 减法
# 2.3
# >>> 3 * 7  # 乘法
# 21
# >>> 2 / 4  # 除法，得到一个浮点数
# 0.5
# >>> 2 // 4 # 除法，得到一个整数
# 0
# >>> 17 % 3 # 取余 
# 2
# >>> 2 ** 5 # 乘方
# 32
# 注意：
# 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# 2、一个变量可以通过赋值指向不同类型的对象。
# 3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
# 4、在混合计算时，Python会把整型转换成为浮点数。

# 数值类型实例
# int	float	complex
# 10	0.0	3.14j
# 100	15.20	45.j
# -786	-21.9	9.322e-36j
# 080	32.3e+18	.876j
# -0490	-90.	-.6545+0J
# -0x260	-32.54e100	3e+26J
# 0x69	70.2E-12	4.53e-7j
# Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

# String（字符串）
# Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
# 字符串的截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。实例如下：
# #!/usr/bin/python3
# str = 'Runoob'
# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次
# print (str + "TEST") # 连接字符串
# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
# >>> print('Ru\noob')
# Ru
# oob
# >>> print(r'Ru\noob')
# Ru\noob
# >>> 
# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
# 实例
# >>>word = 'Python'
# >>> print(word[0], word[5])
# P n
# >>> print(word[-1], word[-6])
# n P
# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误。
# 注意：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用+运算符连接在一起，用*运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# 4、Python中的字符串不能改变。

# List（列表）
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号([])之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 列表截取的语法格式如下：
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号（+）是列表连接运算符，星号（*）是重复操作。如下实例：
# #!/usr/bin/python3
# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表
# 与Python字符串不一样的是，列表中的元素是可以改变的：
# 实例
# >>>a = [1, 2, 3, 4, 5, 6]
# >>> a[0] = 9
# >>> a[2:5] = [13, 14, 15]
# >>> a
# [9, 2, 13, 14, 15, 6]
# >>> a[2:5] = []   # 将对应的元素值设置为 [] 
# >>> a
# [9, 2, 6]
# List内置了有很多方法，例如append()、pop()等等，这在后面会讲到。
# 注意：
# 1、List写在方括号之间，元素用逗号隔开。
# 2、和字符串一样，list可以被索引和切片。
# 3、List可以使用+操作符进行拼接。
# 4、List中的元素是可以改变的。

# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
# 实例
# #!/usr/bin/python3
# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')
# print (tuple)             # 输出完整元组
# print (tuple[0])          # 输出元组的第一个元素
# print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple + tinytuple) # 连接元组
# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
# 其实，可以把字符串看作一种特殊的元组。
# 实例
# >>>tup = (1, 2, 3, 4, 5, 6)
# >>> print(tup[0])
# 1
# >>> print(tup[1:5])
# (2, 3, 4, 5)
# >>> tup[0] = 11  # 修改元组元素的操作是非法的
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>>
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
# tup1 = ()    # 空元组
# tup2 = (20,) # 一个元素，需要在元素后添加逗号
# string、list和tuple都属于sequence（序列）。
# 注意：
# 1、与字符串一样，元组的元素不能修改。
# 2、元组也可以被索引和切片，方法一样。
# 3、注意构造包含0或1个元素的元组的特殊语法规则。
# 4、元组也可以使用+操作符进行拼接

# Set（集合）
# 集合（set）是一个无序不重复元素的序列。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)
# 实例
# #!/usr/bin/python3
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)   # 输出集合，重复的元素被自动去掉
# # 成员测试
# if('Rose' in student) :
#     print('Rose 在集合中')
# else :
#     print('Rose 不在集合中')
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b)     # a和b的差集
# print(a | b)     # a和b的并集
# print(a & b)     # a和b的交集
# print(a ^ b)     # a和b中不同时存在的元素

# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。
# 实例
#!/usr/bin/python3
# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2]     = "2 - 菜鸟工具"
# tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
# print (dict['one'])       # 输出键为 'one' 的值
# print (dict[2])           # 输出键为 2 的值
# print (tinydict)          # 输出完整的字典
# print (tinydict.keys())   # 输出所有键
# print (tinydict.values()) # 输出所有值
# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
# 实例
# >>>dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {'Taobao': 3, 'Runoob': 1, 'Google': 2}
# >>> {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}
# >>> dict(Runoob=1, Google=2, Taobao=3)
# {'Taobao': 3, 'Runoob': 1, 'Google': 2}
# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
# 注意：
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。

# Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
# 函数	描述
# int(x [,base])
# 将x转换为一个整数
# float(x)
# 将x转换到一个浮点数
# complex(real [,imag])
# 创建一个复数
# str(x)
# 将对象 x 转换为字符串
# repr(x)
# 将对象 x 转换为表达式字符串
# eval(str)
# 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)
# 将序列 s 转换为一个元组
# list(s)
# 将序列 s 转换为一个列表
# set(s)
# 转换为可变集合
# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)
# 转换为不可变集合
# chr(x)
# 将一个整数转换为一个字符
# ord(x)
# 将一个字符转换为它的整数值
# hex(x)
# 将一个整数转换为一个十六进制字符串
# oct(x)
# 将一个整数转换为一个八进制字符串

# 笔记:
# 元组（小拓展）
# 一般来说，函数的返回值一般为一个。

# 而函数返回多个值的时候，是以元组的方式返回的。

# 示例（命令行下）：

# >>>def example(a,b):
# ...     return (a,b)
# ...
# >>>type(example(3,4))
# <class 'tuple'>
# >>>
# python中的函数还可以接收可变长参数，比如以 "*" 开头的的参数名，会将所有的参数收集到一个元组上。

# 例如：

# def test(*args):
#     print(args)
#     return args

# print(type(test(1,2,3,4)))    #可以看见其函数的返回值是一个元组
# 字典（小拓展）
# python中的字典是使用了一个称为散列表（hashtable）的算法（不具体展开），

# 其特点就是：不管字典中有多少项，in操作符花费的时间都差不多。

# 如果把一个字典对象作为for的迭代对象，那么这个操作将会遍历字典的键：

# def example(d):
#     # d 是一个字典对象
#     for c in d:
#         print(c)
#         #如果调用函数试试的话，会发现函数会将d的所有键打印出来;
#         #也就是遍历的是d的键，而不是值.
# 荆棘乱
#    荆棘乱

#   llc***n@gmail.com

# 1年前 (2017-05-05)
#    我去咬你啦

#   815***114@qq.com

# 针对楼上的 字典 拓展，做测试的时候，想要输出 kye:value的组合发现可以这样：

# for c in dict:
#     print(c,':',dict[c])
# 或者

# for c in dict:
#     print(c,end=':');
#     print(dict[c])
# 于是发现 print()函数 其实可以 添加多个参数，用逗号 隔开。

# 本来想要用

# for c in dict:
#     print(c+':');
#     print(dict[c])
# 这样的方式打印 key：value结果发现其实 key不一定是 string类型，所以 用+ 号会出问题。

# 我去咬你啦
#    我去咬你啦

#   815***114@qq.com

# 1年前 (2017-06-28)
#    愤怒的胸毛毛

#   zha***aijun2013@foxmail.com

# 在list的使用中，开始时很容易忽视的一点是：

# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# print (list[1:3])       # 从第二个开始输出到第三个元素
# list[1:3] 其实输出的只有两个变量，即list中第二个元素到第三个元素，并不是第1 第2 第3三个元素，而且要注意的是

# print (list[2])
# print (list[2:3])
# 这两句话打印的内容其实是一样的，

# 2.23
# [2.23]
# 但是第二句话有中括号

# 愤怒的胸毛毛
#    愤怒的胸毛毛

#   zha***aijun2013@foxmail.com

# 1年前 (2017-07-02)
#    hellowqp

#   wqp***a@foxmail.com

# python 与 C 语言和 Java 语言的一点不同，表现在它的变量不需要声明变量类型，这是因为像 C 语言和 Java 语言来说，它们是静态的，而 python 是动态的，变量的类型由赋予它的值来决定，例如：

# >>> a = 1
# >>> a = 1.001
# >>> a = "python"
# >>> print(a)
# python
# >>> 
# 第一次为变量 a 赋值为整型，第二次赋值是浮点数，第三次是一个字符串，最后输出时只保留了最后一次的赋值。

# hellowqp
#    hellowqp

#   wqp***a@foxmail.com

# 1年前 (2017-07-08)
#    燕春

#   zqs***306010@qq.com

#    参考地址

# type 是用于求一个未知数据类型对象，而 isinstance 是用于判断一个对象是否是已知类型。

# type 不认为子类是父类的一种类型，而isinstance会认为子类是父类的一种类型。

# 可以用 isinstance 判断子类对象是否继承于父类，type 不行。

# 综合以上几点，type 与 isinstance 虽然都与数据类型相关，但两者其实用法不同，type 主要用于判断未知数据类型，isinstance 主要用于判断 A 类是否继承于 B 类：

# # 判断子类对象是否继承于父类
# class father(object):
#     pass
# class son(father):
#     pass
# if __name__ == '__main__':
#     print (type(son())==father)
#     print (isinstance(son(),father))
#     print (type(son()))
#     print (type(son))
# 运行结果：

# False
# True
# <class '__main__.son'>
# <type 'type'>
# 燕春
#    燕春

#   zqs***306010@qq.com

#    参考地址

# 10个月前 (09-15)
#    妞妞

#   704***556@qq.com

# 字典（小拓展）

# 输入 dict 的键值对，可直接用 items() 函数：

# dict1 = {'abc':1,"cde":2,"d":4,"c":567,"d":"key1"}
# for k,v in dict1.items():
#     print(k,":",v)
# 妞妞
#    妞妞

#   704***556@qq.com

# 7个月前 (12-07)
#    hjc132

#   huj***heng132@gmail.com

# 字典（小拓展）

# 原文说 dict(d)创建一个字典。d 必须是一个序列 (key,value)元组。

# 其实d不一定必须为一个序列元组，如下：

# >>> dict_1 = dict([('a',1),('b',2),('c',3)]) #元素为元组的列表
# >>> dict_1
# {'a': 1, 'b': 2, 'c': 3}
# >>> dict_2 = dict({('a',1),('b',2),('c',3)})#元素为元组的集合
# >>> dict_2
# {'b': 2, 'c': 3, 'a': 1}
# >>> dict_3 = dict([['a',1],['b',2],['c',3]])#元素为列表的列表
# >>> dict_3
# {'a': 1, 'b': 2, 'c': 3}
# >>> dict_4 = dict((('a',1),('b',2),('c',3)))#元素为元组的元组
# >>> dict_4
# {'a': 1, 'b': 2, 'c': 3}
# hjc132
#    hjc132

#   huj***heng132@gmail.com

# 7个月前 (12-10)
#    好好学习天天向上

#   522***154@qq.com

# 集合与字典

# 无序：集合是无序的，所以不支持索引；字典同样也是无序的，但由于其元素是由键（key）和值（value）两个属性组成的键值对，可以通过键（key）来进行索引

# 元素唯一性：集合是无重复元素的序列，会自动去除重复元素；字典因为其key唯一性，所以也不会出现相同元素

# 好好学习天天向上
#    好好学习天天向上

#   522***154@qq.com

# 4个月前 (03-01)
#    Lonapse

#   270***302@qq.com

#    参考地址

# #coding=utf8  
# ''''' 
# 复数是由一个实数和一个虚数组合构成，表示为：x+yj 
# 一个负数时一对有序浮点数(x,y)，其中x是实数部分，y是虚数部分。 
# Python语言中有关负数的概念： 
# 1、虚数不能单独存在，它们总是和一个值为0.0的实数部分一起构成一个复数 
# 2、复数由实数部分和虚数部分构成 
# 3、表示虚数的语法：real+imagej 
# 4、实数部分和虚数部分都是浮点数 
# 5、虚数部分必须有后缀j或J 
 
# 复数的内建属性： 
# 复数对象拥有数据属性，分别为该复数的实部和虚部。 
# 复数还拥有conjugate方法，调用它可以返回该复数的共轭复数对象。 
# 复数属性：real(复数的实部)、imag(复数的虚部)、conjugate()（返回复数的共轭复数） 
# '''  
# class Complex(object):  
#     '''''创建一个静态属性用来记录类版本号'''  
#     version=1.0  
#     '''''创建个复数类，用于操作和初始化复数'''  
#     def __init__(self,rel=15,img=15j):  
#         self.realPart=rel  
#         self.imagPart=img  
         
#     #创建复数  
#     def creatComplex(self):  
#         return self.realPart+self.imagPart  
#     #获取输入数字部分的虚部  
#     def getImg(self):  
#         #把虚部转换成字符串  
#         img=str(self.imagPart)  
#         #对字符串进行切片操作获取数字部分  
#         img=img[:-1]   
#         return float(img)    
                         
# def test():  
#     print "run test..........."  
#     com=Complex()  
#     Cplex= com.creatComplex()  
#     if Cplex.imag==com.getImg():  
#         print com.getImg()  
#     else:  
#         pass  
#     if Cplex.real==com.realPart:  
#         print com.realPart  
#     else:  
#         pass  
#     #原复数  
#     print "the religion complex is :",Cplex  
#     #求取共轭复数  
#     print "the conjugate complex is :",Cplex.conjugate()  
      
# if __name__=="__main__":  
#     test()
# Lonapse
#    Lonapse

#   270***302@qq.com

#    参考地址

# 4个月前 (03-11)
#    符号

#   974***897@QQ.com

# 切片还可以设置步长

# demo = [1,2,3,4,5,6]

# new_demo = demo[1::2]  # 2 就是步长 意思是从索引为 1 的元素开始 每隔2个元素取一次元素
# new_demo = [2,4,6] 

# # 以索引为列  [索引] 和 [索引:索引:步长] 的区别
# # demo[索引] 取出的原列表中索引对应的元素
# # demo[索引:索引:步长] 切片得到的是一个新列表