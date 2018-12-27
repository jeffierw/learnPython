# coding: utf-8
# ex-20: 函数和文件

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)
#  seek() 方法是按字节而不是按行为处理单元的。代码 seek(0) 重新定位在文件的第0位（第一个字节处）。
def print_a_line(line_count,f):
    # readline() 内部代码是扫描文件的每一个字节，直到找到一个 \n 字符代码，然后停止阅读，并返回到此之前获得的
    # 所有内容。代码中f的责任是在每次调用 readline() 之后，维护“磁头”在文件中的位置，以保证继续读后面的每一行。
    print line_count, f.readline()


current_file = open(input_file)

print 'First let\'s print the whole file:\n'

print_all(current_file)

print 'Now let\'s rewind, kind of like a tape.'

rewind(current_file)

print 'Let\'s print three lines:'

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
