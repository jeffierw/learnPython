# -*- coding: utf-8 -*-
# ex-8: 打印，打印

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
# 最后一次输出里第三个字符串内本身有单引号，输出时会用双引号加以区别，其他字符串都是单引号
