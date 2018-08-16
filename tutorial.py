# 关于实例中第一行代码#!/usr/bin/python3 的理解：
# 分成两种情况：
# （1）如果调用python脚本时，使用:
# python script.py 
# #!/usr/bin/python 被忽略，等同于注释。
# （2）如果调用python脚本时，使用:
# ./script.py 
# #!/usr/bin/python 指定解释器的路径。

# helloworld
#    helloworld

#   229***137@qq.com

# 7个月前 (12-10)
#    Xander663

#   xan***1998@163.com

# 再解释一下第一行代码#!/usr/bin/python3

# 这句话仅仅在linux或unix系统下有作用，在windows下无论在代码里加什么都无法直接运行一个文件名后缀为.py的脚本，因为在windows下文件名对文件的打开方式起了决定性作用。

# Xander663
#    Xander663

#   xan***1998@163.com

# 6个月前 (12-29)
#    j88r

#   244***88@qq.com

# 再解释一下第一行代码 #!/usr/bin/python3

# 这句话仅仅在 linux 或 unix 系统下有作用，在 windows 下无论在代码里加什么都无法直接运行一个文件名后缀为 .py 的脚本，因为在 windows 下文件名对文件的打开方式起了决定性作用。

# 这个理论不完全正确，至少我知道的不是这样，我在WIN下安装了 64 位的 python,然后下载了 32 位的 embeddable 版，然后在第一行加了这个，把脚本指向 32 位 python 的位置，然后运行正常，是按 32 位版的运行。

# 至于原因，现在 python 安装的时候会在 windows 目录下放两个文件 py.exe 和 pyw.exe，然后文件类型指向这个这两个文件，可能是由这两个文件判断由哪个 python.exe 去执行脚本。