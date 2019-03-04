from gensim.models import word2vec
import os, fnmatch
import numpy as np

model = word2vec.Word2Vec.load("twitter_model.model")
#print(list(model.wv.vocab))
#print(len(list(model.wv.vocab)))
#print(model['우울증'])

cates = []
pass_cates = ["행복"]
listOfFiles = os.listdir('./cates')
pattern = "*.txt"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        cate = entry[8:entry.index(".txt")]
        if cate not in pass_cates :
            cates.append(cate)

result = {}
word_list = {}
for cate in cates :
    lst_tmp = {cate : 10}
    #print(cate, " : " ,model.most_similar(positive=[cate], topn=10))
    for item in model.most_similar(positive=[cate], topn=100) :
        if round(item[1]*10,4) > 3.5 :
            lst_tmp[item[0]] = round(item[1]*10,4)
            if item[0] not in word_list.keys() :
                word_list[item[0]] = 1
            else :
                word_list[item[0]] += 1
    result[cate] = lst_tmp

# for word in word_list :
#     if word_list[word] >= 2 :
#         print(word, word_list[word])


for item in result :
    print(item, result[item])

# Save
#np.save('twitter_result_by_similar.npy', result)
def myconverter(o):
    if isinstance(o, np.float32):
        return float(o)

import json
with open('data.json', 'w', encoding="utf-8") as outfile:
    json.dump(result, outfile, default=myconverter)