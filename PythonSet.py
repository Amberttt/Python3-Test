# Python3 集合
# 集合（set）是一个无序不重复元素的序列。

# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# 创建格式：

# parame = {value01,value02,...}
# 或者
# set(value)
# 实例(Python 3.0+)
# >>>basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# >>> print(basket)                      # 这里演示的是去重功能
# {'orange', 'banana', 'pear', 'apple'}
# >>> 'orange' in basket                 # 快速判断元素是否在集合内
# True
# >>> 'crabgrass' in basket
# False
 
# >>> # 下面展示两个集合间的运算.
# ...
# >>> a = set('abracadabra')
# >>> b = set('alacazam')
# >>> a                                  
# {'a', 'r', 'b', 'c', 'd'}
# >>> a - b                              # 集合a中包含元素
# {'r', 'd', 'b'}
# >>> a | b                              # 集合a或b中包含的所有元素
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# >>> a & b                              # 集合a和b中都包含了的元素
# {'a', 'c'}
# >>> a ^ b                              # 不同时包含于a和b的元素
# {'r', 'd', 'b', 'm', 'z', 'l'}
# 类似列表推导式，同样集合支持集合推导式(Set comprehension):

# 实例(Python 3.0+)
# >>>a = {x for x in 'abracadabra' if x not in 'abc'}
# >>> a
# {'r', 'd'}
# 集合的基本操作
# 1、添加元素
# 语法格式如下：

# s.add( x )
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao"))
# >>> thisset.add("Facebook")
# >>> print(thisset)
# {'Taobao', 'Facebook', 'Google', 'Runoob'}
# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：

# s.update( x )
# x 可以有多个，用逗号分开。

# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao"))
# >>> thisset.update({1,3})
# >>> print(thisset)
# {1, 3, 'Google', 'Taobao', 'Runoob'}
# >>> thisset.update([1,4],[5,6])  
# >>> print(thisset)
# {1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
# >>>
# 2、移除元素
# 语法格式如下：

# s.remove( x )
# 将元素 x 添加到集合 s 中移除，如果元素不存在，则会发生错误。

# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao"))
# >>> thisset.remove("Taobao")
# >>> print(thisset)
# {'Google', 'Runoob'}
# >>> thisset.remove("Facebook")   # 不存在会发生错误
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Facebook'
# >>>
# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：

# s.discard( x )
# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao"))
# >>> thisset.discard("Facebook")  # 不存在不会发生错误
# >>> print(thisset)
# {'Taobao', 'Google', 'Runoob'}
# 我们也可以设置随机删除集合中的一个元素，语法格式如下：

# s.pop() 
# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
# >>> thisset.pop()
# 'Taobao'
# >>> print(thisset)
# {'Facebook', 'Google', 'Runoob'}
# >>>
# 3、计算集合元素个数
# 语法格式如下：

# len(s)
# 计算集合 s 元素个数。

# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao"))
# >>> len(thisset)
# 3
# 4、清空集合
# 语法格式如下：

# s.clear()
# 清空集合 s。

# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao"))
# >>> thisset.clear()
# >>> print(thisset)
# set()
# 4、判断元素是否在集合中存在
# 语法格式如下：

# x in s
# 判断元素 s 是否在集合 x 中存在，存在返回 True，不存在返回 False。

# 实例(Python 3.0+)
# >>>thisset = set(("Google", "Runoob", "Taobao"))
# >>> "Runoob" in thisset
# True
# >>> "Facebook" in thisset
# False
# >>>

# s.update( "字符串" ) 与 s.update( {"字符串"} ) 含义不同:

#  s.update( {"字符串"} ) 将字符串添加到集合中。
#  s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
# >>> thisset = set(("Google", "Runoob", "Taobao"))
# >>> print(thisset)
# {'Google', 'Runoob', 'Taobao'}
# >>> thisset.update({"Facebook"})
# >>> print(thisset) 
# {'Google', 'Runoob', 'Taobao', 'Facebook'}
# >>> thisset.update("Yahoo")
# >>> print(thisset)
# {'h', 'o', 'Facebook', 'Google', 'Y', 'Runoob', 'Taobao', 'a'}
# >>>

# set() 中参数注意事项

# 1.创建一个含有一个元素的集合

# >>> my_set = set(('apple',))
# >>> my_set
# {'apple'}
# 2.创建一个含有多个元素的集合

# >>> my_set = set(('apple','pear','banana'))
# >>> my_set
# {'apple', 'banana', 'pear'}
# 3.如无必要，不要写成如下形式

# >>> my_set = set('apple')
# >>> my_set
# {'l', 'e', 'p', 'a'}
# >>> my_set1 = set(('apple'))
# >>> my_set1
# {'l', 'e', 'p', 'a'}