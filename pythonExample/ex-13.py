# -*- coding: utf-8 -*-
# ex-13: 参数，解包，变量

# argv 表示参数变量：argument variable

from sys import argv

#下面这行代码表示解包，把所有的参数依次赋予左边的变量名
'''
script, first, second, third = argv

print 'The script is called:', script
print 'Your first variable is:', first
print 'your second variable is:', second
print 'Your third variable is:', third
'''
# 这种导入进来的功能叫做模块，也叫做库。

#接受更少的参数 ex-13-1.py

from sys import argv

script, first = argv

first = raw_input('your first variable is:')

print 'your first variable is: ',  first