import re

f1 = open('finance.txt')
content = f1.read()
new = re.sub('\n\n', '\n', content)
f2 = open('finance_new.txt', 'w')
f2.write(new)

f1.close()
f2.close()
