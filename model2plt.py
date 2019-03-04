# 참고 https://stackoverflow.com/questions/43776572/visualise-word2vec-generated-from-gensim
from sklearn.manifold import TSNE
import matplotlib as mpl
import matplotlib.pyplot as plt
import gensim
import gensim.models as g
from gensim.models import word2vec
import numpy as np




# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

model_name = 'twitter_model.model'
#model = g.Doc2Vec.load(model_name)
model = word2vec.Word2Vec.load("twitter_model.model")

vocab = list(model.wv.vocab)
X = model[vocab]

print(len(X))
#print(X[0][:10])
#tsne = TSNE(n_components=2)

# 100개의 단어에 대해서만 시각화
#X_tsne = tsne.fit_transform(X[:200,:])
#X_tsne = tsne.fit_transform(X)



#df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])
#print("set dataframe")

#print(df.shape)
#print(df.values)
#print(df.to_dict('index'))
#all_dict = df.to_dict('index')
#print("set dict")

import os, fnmatch
cates = []
pass_cates = []
listOfFiles = os.listdir('./cates')
pattern = "*.txt"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        cate = entry[8:entry.index(".txt")]
        if cate not in pass_cates :
            cates.append(cate)

result = {}
cnt = 0

for word1 in vocab :
    #print(word1, end=' ')
    print(cnt)
    cnt += 1
    if word1 not in cates :
        continue
    tmp = []
    result_tmp = {}
    for word2 in vocab :
        #d = math.sqrt((all_dict[word1]['x'] - all_dict[word2]['x'])**2+ (all_dict[word1]['y'] - all_dict[word2]['y'])**2)
        #print("%.2lf"%(d), end=' ')
        dist = np.linalg.norm(model[word1] - model[word2])
        tmp.append(dist)
    #print("\n분산 = ",np.var(tmp))
    #print("\n",math.exp(-d/(2*(np.var(tmp)**2))))
    #print()
    for d, word2 in zip(tmp, vocab) :
        #print(math.exp(-(d/(2*(np.var(tmp)**2)))),end = ' ')
        #result_tmp[word2] = math.exp(-(d**2/(2*(np.var(tmp)**2))))
        result_tmp[word2] = d
        #print("%.2lf" % (math.exp(-d/(2*(np.var(tmp)**2)))), end=' ')

    result[word1] = result_tmp
    #print()

# Save
#np.save('twitter_result.npy', result)

# Load
#read_dictionary = np.load('twitter_result.npy').item()
#print(read_dictionary['디자인'])

def myconverter(o):
    if isinstance(o, np.float32):
        return float(o)


import json
with open('data.json', 'w', encoding="utf-8") as outfile:
    json.dump(result, outfile, default=myconverter)
