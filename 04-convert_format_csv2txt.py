#将一个label\t\text的txt文本转化为label text格式的csv文件

import pandas as pd 

f = open('cnews.val.txt')

labels = []
texts = []
for line in f.readlines():
	label, text = line.split('\t')
	labels.append(label)
	texts.append(text)


data = {'label': labels, 'text': texts}
df = pd.DataFrame(data)
df.to_csv('cnews.val.csv', index=False)
