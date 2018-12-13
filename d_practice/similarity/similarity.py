#/usr/bin/python3
#_*_ coding:utf-8 _*_

import pymongo
from gensim import corpora, models, similarities
from collections import defaultdict

client = pymongo.MongoClient()
collection = client.cishu.simdata
mentries = collection.find().sort("index")

entries = []
tentries = []
for mentry in mentries:
    tentries.append(mentry["tags"])
    entries.append(mentry)

# 建立语料库
dictionary = corpora.Dictionary(tentries)
corpus = [dictionary.doc2bow(tentry) for tentry in tentries]
print(corpus[0]) # [(0, 1), (1, 1), (2, 1), (3, 1)]
# 完成对corpus中出现的每一个特征的IDF值的统计工作
tfidf = models.TfidfModel(corpus)
# tfidf 用待检索的文档向量初始化一个相似度计算的对象
# index = similarities.MatrixSimilarity(tfidf)


# 构造LSI模型并将待检索的query和文本转化为LSI主题向量
# 转换之前的corpus和query均是BOW向量
# 需要将待检索的query和文本放在同一个向量空间里进行表达（以LSI向量空间为例）
lsi_model = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
documents = lsi_model[corpus]
query_vec = lsi_model[dictionary.doc2bow(tentries[5000])]

# 用待检索的文档向量初始化一个相似度计算的对象
index = similarities.MatrixSimilarity(documents)
sims = index[query_vec] # return: an iterator of tuple (idx, sim)

result = []
for index, sim in enumerate(sims):
    if sim > 0:
        item = entries[index]
        item["sim"] = sim
        result.append(entries[index])

result.sort(key=lambda x:x["sim"], reverse=True)
print("completed")