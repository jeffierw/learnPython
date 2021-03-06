# coding: utf-8
# ex-18: 命名，变量，代码，函数

# this one is like your scripts with argv
# 与变量命名规则相同，不能以数字开头，并且只能包含字母数字和下划线
def print_two(*args):# *args 表示把函数所有参数组织在一个列表里 类似解包
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."



print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()