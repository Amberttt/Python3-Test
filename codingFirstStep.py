# Python3 编程第一步
# 在前面的教程中我们已经学习了一些 Python3 的基本语法知识，下面我们尝试来写一个斐波纳契数列。
# 实例(Python 3.0+)
#!/usr/bin/python3
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b
# 其中代码 a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：
# n = b
# b = a + b
# a = n
# 执行以上程序，输出结果为：
# 1
# 1
# 2
# 3
# 5
# 8
# 这个例子介绍了几个新特征。
# 第一行包含了一个复合赋值：变量 a 和 b 同时得到新值 0 和 1。最后一行再次使用了同样的方法，可以看到，右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。
# 输出变量值:
# >>> i = 256*256
# >>> print('i 的值为：', i)
# i 的值为： 65536
# end 关键字
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：
# 实例(Python 3.0+)
# #!/usr/bin/python3
# # Fibonacci series: 斐波纳契数列
# # 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a+b
# 执行以上程序，输出结果为：
# 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

# 5 篇笔记:
#    cnjc1855

#   133***31855@189.cn

# print() sep 参数使用：

# >>> a=10;b=388;c=98
# >>> print(a,b,c,sep='@')
# 10@388@98
# cnjc1855
#    cnjc1855

#   133***31855@189.cn

# 11个月前 (08-06)
#    hackmeng

#   715***8@qq.com

# 看了一下，目前还没有把递归单独拿出来讲解

# 下面使用递归方式求斐波纳契数列

# 其实递归就是函数内部调用自身。

# 使用 print(fab(num)) #num 是一个数字,可用递归方式求输入数字的斐波纳契结果

# def fab(n):
#     if n<1:
#         print('输入有误！')
#         return -1    
#     if n==1 or n==2:
#         return 1    
#     else:
#         return fab(n-1)+fab(n-2)
# hackmeng
#    hackmeng

#   715***8@qq.com

# 10个月前 (09-13)
#    月夜面尊

#   Han***Coding@foxmail.com

# 楼上说用递归的，单纯说递归还好，其实递归在很大程度上牺牲了空间换取了可读性。每次调用递归函数的时候都会创建一个函数栈，如果递归深度过大，则会造成溢出状况。原文中使用a,b = b,a+b 方法求斐波那契数列，占用空间少，来回只有两个变量的空间占用，很方便。

# 月夜面尊
#    月夜面尊

#   Han***Coding@foxmail.com

# 7个月前 (12-10)
#    leviyb

#   lev***@163.com

# 楼上给出了求取斐波那契数列第n项的方法,利用列表可以将前20项输出.但是递归算法重复计算太多,基本计算到第40项就卡住了,太浪费资源,利用列表记录n-1项,可以很大程度上减少重复计算量.利用字典记录也可以实现相同运算.

# n=int(input('请输入一个整数:'))
# def fab(n):
#     if n<1:
#         print('输入有误！')
#         return -1    
#     if n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# result=[]
# for i in range(1,n+1):
#     result.append(fab(i))

# print(result)

# n=int(input('请输入一个整数:')) 
# dic = {0:0,1:1}
# def fib(n):
#     if n in dic:
#         return dic[n]
#     else:
#         temp = fib(n-1)+fib(n-2)
#         dic[n] = temp
#         return temp
# for i in range(n):
#     print(fib(i),end=" " )
# leviyb
#    leviyb

#   lev***@163.com

# 5个月前 (01-28)
#    JasonLiu

#   wsl***un1@163.com

# # r.py
# import sys,getopt

# #递归算法 填充斐波拉契数列
# x,y=0,1
# f_len,f_max=[],[]
# f_len.append(x);f_len.append(y)
# f_max.append(x);f_max.append(y)

# #按最大个数填充
# def Fsqe_Len(n):
#     if len(f_len)<n:
#         Fsqe_Len(n-1)
#     m=f_len[n-1]+f_len[n-2]
#     f_len.append(m)
    
# #按最大值填充
# def Fsqe_Max(fmx):
#     fmlen=len(f_max)-1
#     if f_max[fmlen]>fmx:
#         del f_max[fmlen]
#     else:
#         m=f_max[fmlen-1]+f_max[fmlen]
#         f_max.append(m)
#         Fsqe_Max(fmx)
    
# lens=int(input('Fsqe_Len 输入最大个数：'))
# maxs=int(input('Fsqe_Max 输入最大值：'))
# if __name__ == '__main__':
#     Fsqe_Len(lens)
#     Fsqe_Max(maxs)
#     print(f_len)
#     print(f_max)