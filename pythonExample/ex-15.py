#coding: utf-8
# ex-15: 读文件

from sys import argv

script, filename = argv 

txt = open(filename)

print 'Here\'s your file %r:' % filename
print txt.read()

print 'Typethe filename again:'
file_again = raw_input('>')

txt_again = open(file_again)

print txt_again.read()