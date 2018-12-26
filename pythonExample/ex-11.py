# -*- coding: utf-8 -*-
# ex-11: 提问

# 终于不用一直打印了。。。

print "How old are you?"，
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." %(age, height, weight)
# print后的逗号，是为了不换行去做下面的输入
# raw_input()函数表示获取控制台的输入 并且都作为字符串看待 返回字符串类型
# raw_input() 括号内可以增加参数作为提示输入的作用