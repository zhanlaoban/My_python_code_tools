#将index,label,content形式转化成label\tcontent形式
#已注释代码表示创建一个pandas

import pandas as pd 

data = pd.read_csv('dev.csv')
#print(data)

labels = []
contents = []
fout = open('dev_new.csv', 'w+')

for i in range(len(data)):
	
	#labels.append(data.iloc[i]['label'])
	#contents.append(data.iloc[i]['content'])

	line = str(data.iloc[i]['label']) + '\t' + str(data.iloc[i]['content']) + '\n'
	#print(line)
	fout.write(line)

fout.close()

'''
data_final = {'labels': labels, 'contents': contents}
df = pd.DataFrame(data_final)
df.to_csv('train_new.csv')
'''


	