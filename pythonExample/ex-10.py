# -*- coding: utf-8 -*-
# ex-10: 那是什么？ 

# 字符串扩展到多行的方法： 1.字符之间用\n隔开  
# 转义单引号和双引号： 
# "I am 6'2\" tall."  # 将字符串中的双引号转义
# 'I am 6\'2" tall.'  # 将字符串中的单引号转义
# 转义什么引号就把反斜杠放在引号前面

# 或者使用三引号 """ 在一组三引号中放入任意行的文字 '''单引号也是可以的


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 有意思的代码

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,
# 在这些符号中循环 鼠标点击 随机产生其中一个字符 不然会一直循环
# %r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容。