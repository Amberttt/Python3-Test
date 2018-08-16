#!/usr/bin/python3

# 编码
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：
# # -*- coding: cp-1252 -*-
# 上述定义允许在源文件中使用 Windows-1252 字符集中的字符编码，对应适合语言为保加利亚语、白罗斯语、马其顿语、俄语、塞尔维亚语。

# 标识符
# 第一个字符必须是字母表中字母或下划线 _ 。
# 标识符的其他的部分由字母、数字和下划线组成。
# 标识符对大小写敏感。
# 在 Python 3 中，非 ASCII 标识符也是允许的了。

# Python保留字
# 保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
# import keyword
# keyword.kwlist

# 注释
# Python中单行注释以 # 开头，实例如下：
# 第一个注释
print("Hello, World!")  # 第二个注释
# 多行注释可以用多个 # 号，还有 ''' 和 """：
'''
第三注释
第四注释
'''
"""
第五注释
第六注释
"""

# 行与缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} 。
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
# if True:
#     print("True")
# else:
#     print("False")
# 缩进不一致，会导致运行错误

# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
# total = 1 + \
#     2 + \
#     3
# print("total =",total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
# arr = ['item_one',
#     'item_two',
#     'item_three',
#     'item_four',
#     'item_five']
# print(arr)

# 数字(Number)类型
# python中数字有四种类型：整数、布尔型、浮点数和复数。
# int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# bool (布尔), 如 True。
# float (浮点数), 如 1.23、3E-2
# complex (复数), 如 1 + 2j、 1.1 + 2.2j

# 字符串(String)
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
# 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
# Python中的字符串不能改变。
# Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
# 字符串的截取的语法格式如下：变量[头下标:尾下标]
# word = '字符串'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落，
# 可以由多行组成"""

# str='Runoob'
# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符，不包括第二个index
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第五个的字符
# print(str[2:])             # 输出从第三个开始的后的所有字符
# print(str * 2)             # 输出字符串两次
# print(str + '你好')        # 连接字符串
# print('------------------------------')
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。
# 记住：空行也是程序代码的一部分。

# 等待用户输入
# 执行下面的程序在按回车键后就会等待用户输入：
# 实例(Python 3.0+)
# #!/usr/bin/python3
# input("\n\n按下 enter 键后退出。")
# 以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
# 实例(Python 3.0+)
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 执行以上代码，输出结果为：
# runoob

# 多个语句构成代码组
# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 我们将首行及后面的代码组称为一个子句(clause)。
# 如下实例：
# if expression : 
#    suite
# elif expression : 
#    suite 
# else : 
#    suite

# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
# 实例(Python 3.0+)
# #!/usr/bin/python3
# x="a"
# y="b"
# # 换行输出
# print( x )
# print( y )
# print('---------')
# # 不换行输出
# print( x, end=" " )
# print( y, end=" " )
# print()

# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# 导入 sys 模块
# import sys
# print('================Python import mode==========================');
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)
# 导入 sys 模块的 argv,path 成员
# from sys import argv,path  #  导入特定的成员
# print('================python from import===================================')
# print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

# 命令行参数
# 很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息：
# $ python -h
# usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
# Options and arguments (and corresponding environment variables):
# -c cmd : program passed in as string (terminates option list)
# -d     : debug output from parser (also PYTHONDEBUG=x)
# -E     : ignore environment variables (such as PYTHONPATH)
# -h     : print this help message and exit
# [ etc. ]
# 在使用脚本形式执行 Python 时，可以接收命令行输入的参数，具体使用可以参照 Python 3 命令行参数。

# Python3 命令行参数
# Python3 基础语法 Python3 基础语法
# Python 提供了 getopt 模块来获取命令行参数。
# $ python test.py arg1 arg2 arg3
# Python 中也可以所用 sys 的 sys.argv 来获取命令行参数：
# sys.argv 是命令行参数列表。
# len(sys.argv) 是命令行参数个数。
# 注：sys.argv[0] 表示脚本名。
# 实例
# test.py 文件代码如下：
# #!/usr/bin/python3
# import sys
# print ('参数个数为:', len(sys.argv), '个参数。')
# print ('参数列表:', str(sys.argv))
# 执行以上代码，输出结果为：
# $ python3 test.py arg1 arg2 arg3
# 参数个数为: 4 个参数。
# 参数列表: ['test.py', 'arg1', 'arg2', 'arg3']
# getopt模块
# getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。命令行选项使得程序的参数更加灵活。支持短选项模式（-）和长选项模式（--）。
# 该模块提供了两个方法及一个异常处理来解析命令行参数。
# getopt.getopt 方法
# getopt.getopt 方法用于解析命令行参数列表，语法格式如下：
# getopt.getopt(args, options[, long_options])
# 方法参数说明：
# args: 要解析的命令行参数列表。
# options: 以字符串的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
# long_options: 以列表的格式定义，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
# 该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数。
# 另外一个方法是 getopt.gnu_getopt，这里不多做介绍。
# Exception getopt.GetoptError
# 在没有找到参数列表，或选项的需要的参数为空时会触发该异常。
# 异常的参数是一个字符串，表示错误的原因。属性 msg 和 opt 为相关选项的错误信息。
# 实例
# 假定我们创建这样一个脚本，可以通过命令行向脚本文件传递两个文件名，同时我们通过另外一个选项查看脚本的使用。脚本使用方法如下：
# usage: test.py -i <inputfile> -o <outputfile>
# test.py 文件代码如下所示：
# #!/usr/bin/python3

# import sys, getopt

# def main(argv):
#    inputfile = ''
#    outputfile = ''
#    try:
#       opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#    except getopt.GetoptError:
#       print ('test.py -i <inputfile> -o <outputfile>')
#       sys.exit(2)
#    for opt, arg in opts:
#       if opt == '-h':
#          print ('test.py -i <inputfile> -o <outputfile>')
#          sys.exit()
#       elif opt in ("-i", "--ifile"):
#          inputfile = arg
#       elif opt in ("-o", "--ofile"):
#          outputfile = arg
#    print ('输入的文件为：', inputfile)
#    print ('输出的文件为：', outputfile)
# if __name__ == "__main__":
#    main(sys.argv[1:])
# 执行以上代码，输出结果为：
# $ python3 test.py -h
# usage: test.py -i <inputfile> -o <outputfile>
# $ python3 test.py -i inputfile -o outputfile
# 输入的文件为： inputfile
# 输出的文件为： outputfile

# 在 Windows 下可以不写第一行注释:
# #!/usr/bin/python3
# 第一行注释标的是指向 python 的路径，告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
# 此外还有以下形式（推荐写法）：
# #!/usr/bin/env python3
# 这种用法先在 env（环境变量）设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。

# 关于注释，也可以使用 ''' ''' 的格式在三引号之间书写较长的注释；
# ''' ''' 还可以用于在函数的首部对函数进行一个说明：
# def example(anything):
#     '''形参为任意类型的对象，
#        这个示例函数会将其原样返回。
#     '''
#     return anything
# help() 函数
# 调用 python 的 help() 函数可以打印输出一个函数的文档字符串：
# # 如下实例，查看 max 内置函数的参数列表和规范的文档
# >>> help(max)
# ……显示帮助信息…… 按下 : q 两个按键即退出说明文档
# 如果仅仅想得到文档字符串：
# >>> print(max.__doc__)    # 注意，doc的前后分别是两个下划线
# max(iterable, *[, default=obj, key=func]) -> value
# max(arg1, arg2, *args, *[, key=func]) -> value
# With a single iterable argument, return its biggest item. The
# default keyword-only argument specifies an object to return if
# the provided iterable is empty.
# With two or more arguments, return the largest argument.

# 在 print 打印的时候双引号与单引号都可以当做定界符使用，且可以嵌套。
# 被嵌套的会被解释成为标点符号，反之一样。
# 代码实例：
# print("Hello'World!")
# 这句代码执行时，外侧的双引号为定界符，里面的那个单引号为标点符号。
# 输出：
# Hello'World!
# print('Hello"World!')
# 这句代码执行时，外侧的单引号为定界符，里面的那个双引号为标点符号。
# 输出：
# Hello"World!