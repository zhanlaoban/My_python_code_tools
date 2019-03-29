import re

f = open("02_in.txt")
f_out = open("02_out.txt", "w")

for line in f.readlines():
    part = line.split("\t")
    f_out.write(re.sub("\s+", "", part[1]))    #re.sub不会对原part做出改变
    f_out.write("\n")

f.close()
f_out.close()


###details
'''
\s匹配任意的空白符，包括空格、制表符(TAB)、换行符、中文全角空格
'''
