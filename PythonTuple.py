# Python3 元组
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。

# 元组使用小括号，列表使用方括号。

# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

# 实例(Python 3.0+)
# >>>tup1 = ('Google', 'Runoob', 1997, 2000);
# >>> tup2 = (1, 2, 3, 4, 5 );
# >>> tup3 = "a", "b", "c", "d";   #  不需要括号也可以
# >>> type(tup3)
# <class 'tuple'>
# 创建空元组

# tup1 = ();
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：

# 实例(Python 3.0+)
# >>>tup1 = (50)
# >>> type(tup1)     # 不加逗号，类型为整型
# <class 'int'>
 
# >>> tup1 = (50,)
# >>> type(tup1)     # 加上逗号，类型为元组
# <class 'tuple'>
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合等。

# 访问元组
# 元组可以使用下标索引来访问元组中的值，如下实例:

# 实例(Python 3.0+)
# #!/usr/bin/python3
 
# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
# print ("tup1[0]: ", tup1[0])
# print ("tup2[1:5]: ", tup2[1:5])
# 以上实例输出结果：

# tup1[0]:  Google
# tup2[1:5]:  (2, 3, 4, 5)
# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:

# 实例(Python 3.0+)
# #!/usr/bin/python3
 
# tup1 = (12, 34.56);
# tup2 = ('abc', 'xyz')
 
# # 以下修改元组元素操作是非法的。
# # tup1[0] = 100
 
# # 创建一个新的元组
# tup3 = tup1 + tup2;
# print (tup3)
# 以上实例输出结果：

# (12, 34.56, 'abc', 'xyz')
# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

# 实例(Python 3.0+)
# #!/usr/bin/python3
 
# tup = ('Google', 'Runoob', 1997, 2000)
 
# print (tup)
# del tup;
# print ("删除后的元组 tup : ")
# print (tup)
# 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：

# 删除后的元组 tup : 
# Traceback (most recent call last):
#   File "test.py", line 8, in <module>
#     print (tup)
# NameError: name 'tup' is not defined
# 元组运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

# Python 表达式	结果	描述
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print (x,)	1 2 3	迭代
# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：

# 元组：

# L = ('Google', 'Taobao', 'Runoob')
# Python 表达式	结果	描述
# L[2]	'Runoob'	读取第三个元素
# L[-2]	'Taobao'	反向读取；读取倒数第二个元素
# L[1:]	('Taobao', 'Runoob')	截取元素，从第二个开始后的所有元素。
# 运行实例如下：

# >>> L = ('Google', 'Taobao', 'Runoob')
# >>> L[2]
# 'Runoob'
# >>> L[-2]
# 'Taobao'
# >>> L[1:]
# ('Taobao', 'Runoob')
# 元组内置函数
# Python元组包含了以下内置函数

# 序号	方法及描述	实例
# 1	len(tuple)
# 计算元组元素个数。	
# >>> tuple1 = ('Google', 'Runoob', 'Taobao')
# >>> len(tuple1)
# 3
# >>> 
# 2	max(tuple)
# 返回元组中元素最大值。	
# >>> tuple2 = ('5', '4', '8')
# >>> max(tuple2)
# '8'
# >>> 
# 3	min(tuple)
# 返回元组中元素最小值。	
# >>> tuple2 = ('5', '4', '8')
# >>> min(tuple2)
# '4'
# >>> 
# 4	tuple(seq)
# 将列表转换为元组。	
# >>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
# >>> tuple1=tuple(list1)
# >>> tuple1
# ('Google', 'Taobao', 'Runoob', 'Baidu')

# 5 篇笔记:
#    heisenbug601

#   601***902@qq.com

#    参考地址

# tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

# 代码如下：

# >>> classmates = ('Michael', 'Bob', 'Tracy')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：

# 代码如下：

# >>> t = (1, 2)
# >>> t
# (1, 2)
# 如果要定义一个空的tuple，可以写成()：

# 代码如下：

# >>> t = ()
# >>> t
# ()
# 但是，要定义一个只有1个元素的tuple，如果你这么定义：

# 代码如下：

# >>> t = (1)
# >>> t
# 1
# 定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

# 所以，只有1个元素的tuple定义时必须加一个逗号 ,来消除歧义：

# 代码如下:

# >>> t = (1,)
# >>> t
# (1,)
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

# 在来看一个"可变的"tuple：

# 代码如下:

# >>> t = ('a', 'b', ['A', 'B'])
# >>> t[2][0] = 'X'
# >>> t[2][1] = 'Y'
# >>> t
# ('a', 'b', ['X', 'Y'])
# 这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？

# 别急，我们先看看定义的时候tuple包含的3个元素：当我们把list的元素'A'和'B'修改为'X'和'Y'后，tuple变为：表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的"不变"是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！理解了"指向不变"后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

# heisenbug601
#    heisenbug601

#   601***902@qq.com

#    参考地址

# 8个月前 (11-04)
#    run

#   hdr***11@gmail.com

# tuple元素不可变有一种特殊情况，当元素是可变对象时。对象内部属性是可以修改的！tuple的不可变限制只是在一个纬度上：元素的类型。实现理解，tuple的元素所保存的内容（数值或内存地址）是不允许修改的，但地址映射的对象自身是可以修改的。

# >>> a = (1,[3,2])
# >>> a[1][0] = 1
# >>> a
# (1, [1, 2])
# >>> a[1].append(3)
# >>> a
# (1, [1, 2, 3])
# >>> del a[1][2]
# >>> a
# (1, [1, 2])
# >>> del a[1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object doesn't support item deletion
# >>> del a[1][1]
# >>> del a[1][0]
# >>> a
# (1, [])
# >>>
# 字符串是一种特殊的tuple,支持部分tuple的运算符

# >>> a = '12345'
# >>> a[2]
# '3'
# >>> a[3:]
# '45'
# >>> type(a)
# <class 'str'>
# >>> a*2
# '1234512345'
# >>> 6 in a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'in <string>' requires string as left operand, not int
# >>> a
# '12345'
# >>> for x in a: print(x)
# ... 
# 1
# 2
# 3
# 4
# 5
# run
#    run

#   hdr***11@gmail.com

# 6个月前 (12-26)
#    mqslllduoduo

#   494***660@qq.com

# Python元组的升级版本 -- namedtuple(具名元组)

# 因为元组的局限性：不能为元组内部的数据进行命名，所以往往我们并不知道一个元组所要表达的意义，所以在这里引入了 collections.namedtuple 这个工厂函数，来构造一个带字段名的元组。具名元组的实例和普通元组消耗的内存一样多，因为字段名都被存在对应的类里面。这个类跟普通的对象实例比起来也要小一些，因为 Python 不会用 __dict__ 来存放这些实例的属性。

# namedtuple 对象的定义如以下格式：

# collections.namedtuple(typename, field_names, verbose=False, rename=False) 
# 返回一个具名元组子类 typename，其中参数的意义如下：

#  typename：元组名称
#  field_names: 元组中元素的名称
#  rename: 如果元素名称中含有 python 的关键字，则必须设置为 rename=True
#  verbose: 默认就好
# 下面来看看声明一个具名元组及其实例化的方法：

# import collections

# # 两种方法来给 namedtuple 定义方法名
# #User = collections.namedtuple('User', ['name', 'age', 'id'])
# User = collections.namedtuple('User', 'name age id')
# user = User('tester', '22', '464643123')

# print(user)
# collections.namedtuple('User', 'name age id') 创建一个具名元组，需要两个参数，一个是类名，另一个是类的各个字段名。后者可以是有多个字符串组成的可迭代对象，或者是有空格分隔开的字段名组成的字符串（比如本示例）。具名元组可以通过字段名或者位置来获取一个字段的信息。

# 输出结果：

# User(name='tester', age='22', id='464643123')
# 具名元组的特有属性:

# 类属性 _fields：包含这个类所有字段名的元组 类方法 _make(iterable)：接受一个可迭代对象来生产这个类的实例 实例方法 _asdict()：把具名元组以 collections.OrdereDict 的形式返回，可以利用它来把元组里的信息友好的展示出来
# from collections import namedtuple

# # 定义一个namedtuple类型User，并包含name，sex和age属性。
# User = namedtuple('User', ['name', 'sex', 'age'])

# # 创建一个User对象
# user = User(name='Runoob', sex='male', age=12)

# # 获取所有字段名
# print( user._fields )

# # 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
# user = User._make(['Runoob', 'male', 12])

# print( user )
# # User(name='user1', sex='male', age=12)

# # 获取用户的属性
# print( user.name )
# print( user.sex )
# print( user.age )

# # 修改对象属性，注意要使用"_replace"方法
# user = user._replace(age=22)
# print( user )
# # User(name='user1', sex='male', age=21)

# # 将User对象转换成字典，注意要使用"_asdict"
# print( user._asdict() )
# # OrderedDict([('name', 'Runoob'), ('sex', 'male'), ('age', 22)])
# 以上实例输出结果为：

# ('name', 'sex', 'age')
# User(name='Runoob', sex='male', age=12)
# Runoob
# male
# 12
# User(name='Runoob', sex='male', age=22)
# OrderedDict([('name', 'Runoob'), ('sex', 'male'), ('age', 22)])
# mqslllduoduo
#    mqslllduoduo

#   494***660@qq.com

# 3个月前 (03-30)
#    章鱼二哥

#   490***6@qq.com

# 元组的一些特殊需求实现

# 1、定义元组后，根据不同的情形增加新的元组内容

# t1=(1,2,3)
# for i in range(1,5):
#     t2=(i,)
#     t1=t1+t2
# print(t1)
# 输出为：

# (1, 2, 3, 1, 2, 3, 4)
# 2、修改元组内的特定位置的值

# t1=(1,2,3)
# for i in range(1,5):
#     t2=(i,)
#     t1=t1+t2
# print(t1)

# l1=list(t1)
# print(l1)

# l1[0]=9
# print(l1)

# t1=tuple(l1)
# print(t1)
# 输出为：

# (1, 2, 3, 1, 2, 3, 4)
# [1, 2, 3, 1, 2, 3, 4]
# [9, 2, 3, 1, 2, 3, 4]
# (9, 2, 3, 1, 2, 3, 4)
# 章鱼二哥
#    章鱼二哥

#   490***6@qq.com

# 6天前
#    tt

#   308***149@qq.com

# 元组所指向的内存实际上保存的是元组内数据的内存地址集合（即 t[0], t[1]...t[n] 的内存地址），且元组一旦建立，这个集合就不能增加修改删除，一旦集合内的地址发生改变，必须重新分配元组空间保存新的地址集（元组类似 C 语言里的指针数组，只不过这个数组不能被修改）。

# 测试下面代码：

# print("连接前：")
# t1=(1,2,"3")
# t2=("4",5,["d1","d2"])
# print("t1=",t1);
# print("t2=",t2);
# print("t1:",id(t1))
# print("t2:",id(t2))
# print("t1[0]:",id(t1[0]))
# print("t1[1]:",id(t1[1]))
# print("t1[2]:",id(t1[2]))
# print("t2[0]:",id(t2[0]))
# print("t2[1]:",id(t2[1]))
# print("t2[2]:",id(t2[2]))
# print("连接后：")
# t1= t1+t2
# print("t1(t1+t2):",id(t1))
# print("t1[0]:",id(t1[0]))
# print("t1[1]:",id(t1[1]))
# print("t1[2]:",id(t1[2]))
# print("t1[3]:",id(t1[3]))
# print("t1[4]:",id(t1[4]))
# print("t1[5]:",id(t1[5]))
# t1[5].append("d3")
# print("t1[5]增加d3:")
# print("t1[5]=",t1[5])
# print("t1[5]:",id(t1[5]))
# print("t2=",t2);
# 输出：

# 连接前：
# t1= (1, 2, '3')
# t2= ('4', 5, ['d1', 'd2'])
# t1: 1719219799168
# t2: 1719219799528
# t1[0]: 1378249760
# t1[1]: 1378249792
# t1[2]: 1719200188208
# t2[0]: 1719199042336
# t2[1]: 1378249888
# t2[2]: 1719219441608
# 连接后：
# t1(t1+t2): 1719222365256
# t1[0]: 1378249760
# t1[1]: 1378249792
# t1[2]: 1719200188208
# t1[3]: 1719199042336
# t1[4]: 1378249888
# t1[5]: 1719219441608
# t1[5]增加d3:
# t1[5]= ['d1', 'd2', 'd3']
# t1[5]: 1719219441608
# t2= ('4', 5, ['d1', 'd2', 'd3'])
# 测试结论：元组 t1 跟 t2 连接并赋值 t1 后，t1 地址发生变化（因地址集合变化），t1[0], t1[1], t1[2], t2[0], t2[1], t2[2] 地址不变且保存在连接后的 t1，元组内数据根据自身类型确定是否可修改值（t1[0]..t1[4] 分别为不可修改的数据类型，t1[5] 为可修改的列表），连接后 t1[5] 跟 t2[2] 地址一样，t1[5] 变化将会导致 t2[2] 变化。