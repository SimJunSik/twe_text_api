from gensim.models import word2vec, Word2Vec
#data = word2vec.Text8Corpus("twitter.wakati")
data = word2vec.LineSentence("twitter.wakati")
embedding_model = Word2Vec(data, size=130, window=2, min_count=50, workers=4, sg=1, iter=100)
embedding_model.save("twitter_model.model")
print("ok")
#print(embedding_model.most_similar(positive=["디자인"], topn=100))