#!/usr/bin/python3
#_*_ coding: utf8 _*_

import jieba
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, models, similarities
from collections import defaultdict
from datetime import datetime
from elasticsearch import Elasticsearch
import csv
import numpy as np

es = Elasticsearch(["127.0.0.1:9200"])

offset = 0
count = 5000
docs = []
keywords = []


while True:
    query = {
                "query": {
                    "match_all": {}
                },
                "sort": {
                    "index": {"order": "asc"}
                },
                "size": count,
                "from": offset
             }
    res = es.search(index="keyword1", body=query)

    for hit in res['hits']['hits']:
        keyword = hit["_source"]
        comment = keyword['comment']
        keywords.append(keyword['name'])

        data = jieba.cut(comment)

        data_line = ""
        for i in data:
            data_line += i + " "

        docs.append(data_line)

    offset = offset + count

    if offset >= res['hits']['total']:
        break

# query = {
#             "query": {
#                 "match_all": {}
#             },
#             "sort": {
#                 "index": {"order": "asc"}
#             },
#             "size": 10,
#             "from": 0
#          }
# res = es.search(index="keyword1", body=query)
#
# for hit in res['hits']['hits']:
#     keyword = hit["_source"]
#     comment = keyword['comment']
#     keywords.append(keyword['name'])
#
#     data = jieba.cut(comment)
#
#     data_line = ""
#     for i in data:
#         data_line += i + " "
#
#     docs.append(data_line)

t1 = [[word for word in doc.split()]
      for doc in docs]

# # frequence频率
freq = defaultdict(int)
for i in t1:
    for j in i:
        freq[j] += 1

# print("freq", freq)

# t2 = [[token for token in k if (token not in ["【", "】", '。', '(', ')', '，', '、', ] and freq[token] >= 3 and len(token) > 1)]
t2 = [[token for token in k if (token not in ["【", "】", '。', '(', ')', '，', '、', ] and len(token) > 1)]
      for k in t1]

# print("filtered", t2)

dic1 = corpora.Dictionary(t2)
dic1.save("F:/Temp/python/jieba/yuliaoku.txt")

target = u'马克思【】(Karl Marx, 1818—1883)无产阶级革命导师，马克思主义创始人。1818年5月5日生于德国特里尔市(时属普鲁士王国)一个律师家庭。先后进波恩大学和柏林大学法律系，先是攻读法学，后主要研究历史和哲学。参加青年黑格尔派。1841年大学毕业，同年由耶拿大学授予哲学博士学位。1842年4月起为《莱茵报》撰稿，同年10月起任该报编辑。在他影响下该报具有越来越鲜明的革命民主主义倾向。1843年3月该报被查封。同年6月与燕妮·冯·威斯特华伦结婚，10月迁居巴黎。1844年初创办《德法年鉴》杂志，在该杂志上发表了《论犹太人问题》和《〈黑格尔法哲学批判〉导言》等文章，阐明了消灭私有制、实现人的解放的思想，并指出只有无产阶级才是实现人的解放的社会革命力量。这期间马克思完成了从唯心主义向唯物主义、从革命民主主义向共产主义的转变。同年写的《一八四四年经济学哲学手稿》，从唯物主义和共产主义的立场出发，对资产阶级政治经济学和资本主义制度进行批判性研究，对共产主义作初步理论论证，并提出了异化劳动的理论。1844年8月底，马克思和恩格斯在巴黎会见，从此并肩战斗终生。这次历史性会见的第一个成果，就是他们合著的《神圣家族》，该书批判了青年黑格尔派的唯心主义哲学，阐明了物质生产对历史起决定作用和人民群众是历史创造者等历史唯物主义的基本原理。1845年2月，因从事革命活动被逐出法国，迁居比利时首都布鲁塞尔。在这里，写了著名的《关于费尔巴哈的提纲》，这是包含着新世界观的天才萌芽的第一个文献。1845—1846年，与恩格斯合写了《德意志意识形态》，进一步批判青年黑格尔派的唯心史观，揭露德国“真正的社会主义”的假社会主义面目及其哲学基础，指出了费尔巴哈唯物主义的不彻底性，第一次系统地阐述了唯物主义历史观。1846年和1847年，同恩格斯在布鲁塞尔先后建立了共产主义通讯委员会和德意志工人协会，在工人组织中宣传科学社会主义思想，清除蒲鲁东主义、魏特林平均共产主义和“真正的社会主义”的思想影响。1847年发表《哲学的贫困》，批判蒲鲁东的改良主义幻想和唯心主义的形而上学的方法，科学地论证了辩证唯物主义和历史唯物主义的一些基本原理。同年与恩格斯一起加入正义者同盟，并指导该同盟改组成共产主义者同盟。受同盟第二次代表大会的委托，1847年12月至1848年1月，同恩格斯一起起草了同盟的纲领，即1848年2月问世的《共产党宣言》。《共产党宣言》是科学社会主义的第一个纲领性文献，标志着马克思主义的诞生。1848年3月，共产主义者同盟新的中央委员会在巴黎成立，马克思被选为主席。1848年德国三月革命爆发，马克思和恩格斯拟定了《共产党在德国的要求》作为共产主义者在这次革命中的行动纲领。4月他们回国参加革命，在科隆筹办《新莱茵报》，该报于6月1日出版，马克思任主编。他们通过该报指导德国革命运动，声援各国人民的革命斗争。革命失败后，1849年5月马克思被逐出普鲁士，先到巴黎，后定居伦敦。到伦敦后，立即着手重建共产主义者同盟的地方组织和中央委员会。1850年夏，跟同盟内部维利希-沙佩尔冒险主义集团进行了斗争。1850—1852年，为总结1848年革命的经验，先后写了《一八四八年至一八五○年的法兰西阶级斗争》和《路易·波拿巴的雾月十八日》等重要著作，进一步阐发了马克思主义的国家学说，论述了无产阶级革命必须打碎旧的国家机器的思想，提出了无产阶级专政理论，阐述了不断革命和工农联盟的思想。从1851年开始，为美国《纽约每日论坛报》和英国及其他国家的一些报刊撰稿，评述了各种重大的国际问题，其中包括中国问题。在论述中国问题的文章中，分析了中国社会的特点，揭露和谴责英、法、俄、美等国对中国的侵略和掠夺，热情地颂扬中国人民的反侵略斗争，并指出了中国革命的光明前景。在50年代和60年代，马克思把主要精力用于研究政治经济学，写作经济学巨著《资本论》。《政治经济学批判(1857—1858年手稿)》可说是《资本论》的最初稿本。在这部手稿中完成了作为马克思经济学理论基石的剩余价值理论的创建。后来又写了一部新的手稿，即《政治经济学批判(1861—1863年手稿)》。它是《资本论》的第二个稿本，包括《资本论》第1卷的主要内容和第2、3卷的部分内容，其中历史文献部分被后人编为《剩余价值理论》出版。1863—1865年，写了《资本论》第1、2、3册即《资本论》第1、2、3卷的手稿。1867年9月《资本论》第1卷问世(第2、3卷在他逝世后经恩格斯整理，分别于1885年和1894年出版)。《资本论》对资本主义生产方式作了科学分析，揭示了资本主义社会经济运动规律，揭露了资本家剥削工人的秘密和资本主义的基本矛盾，论证了资本主义的必然灭亡和社会主义的必然胜利，从而为科学社会主义奠定了牢固的理论基础。50年代末60年代初，欧洲工人运动开始出现新高涨。1864年9月在伦敦成立了国际工人协会，即第一国际，马克思参加了第一国际的创建，是国际的灵魂和真正领袖。他为国际起草了成立宣言、章程和许多重要文件，为国际制定了斗争纲领、斗争策略和组织原则，通过国际指导各国工人运动，支持各被压迫民族的民族解放运动，领导了国际内部反对工联主义、蒲鲁东主义、拉萨尔主义和巴枯宁主义的斗争。1871年3月18日，巴黎工人举行武装起义，并于3月28日建立了人类历史上第一个无产阶级的政权——巴黎公社。马克思对巴黎无产阶级的革命首创精神作了高度评价，积极支持巴黎公社；公社失败后，写了《法兰西内战》一书，总结了公社的经验，进一步发展了马克思主义关于无产阶级革命和无产阶级专政的学说。在同年9月举行的国际工人协会伦敦代表会议上，马克思和恩格斯强调了组织工人阶级的独立政党对于保证革命胜利的必要性。在70—80年代初，马克思在继续写作《资本论》第2、3卷的同时，十分关心国际共产主义运动的发展。1875年2月德国社会民主工党(爱森纳赫派)同全德工人联合会(拉萨尔派)召开合并预备会议，并拟定了准备提交哥达合并大会通过的纲领草案。马克思抱病写了《哥达纲领批判》，批判了爱森纳赫派领导人向拉萨尔派的无原则妥协，批判了拉萨尔派机会主义的经济观点、政治观点和策略思想，第一次提出了共产主义社会分为第一阶段和高级阶段的学说，分析了共产主义社会两个阶段的基本特征和分配原则，指出在共产主义社会第一阶段只能实行按劳分配，只有到了高级阶段才能实行按需分配。他还提出了在资本主义社会和共产主义社会之间有个过渡时期的思想，指出这个时期的国家只能是无产阶级的革命专政。这些思想是对科学社会主义的新发展。1876—1878年，积极支持并参与恩格斯对德国折中主义哲学家、庸俗经济学家和小资产阶级社会主义者杜林的批判。1879年，同恩格斯合写了《给奥·倍倍尔、威·李卜克内西、威·白拉克等人的通告信》，批判赫希柏格、伯恩施坦、施拉姆(“三个苏黎世人”)妄图把德国党变成改良主义政党的机会主义观点。还同恩格斯一起对法、英、美等国工人运动内部的机会主义派别进行了揭露和批判。晚年为了探索俄国和东方落后国家的发展道路，用不少时间收集和研究有关俄国和其他地区的农村公社以及有关古代社会的资料，作了大量笔记。这些笔记为研究经济文化比较落后的国家的发展道路提供了宝贵材料。1883年3月14日在伦敦病逝。'
target_data = jieba.cut(target)

target_line = ""
for i in target_data:
    target_line += i + " "

new_doc = target_line
# doc2bow把文件变成一个稀疏向量
new_vec = dic1.doc2bow(new_doc.split())
# 对字典进行doc2bow处理，得到新语料库
new_corpor = [dic1.doc2bow(t3) for t3 in t2]
tfidf = models.TfidfModel(new_corpor)

# 特征数
featurenum = len(dic1.token2id.keys())

# similarities 相似之处
# SparseMatrixSimilarity 稀疏矩阵相似度
idx = similarities.SparseMatrixSimilarity(tfidf[new_corpor], num_features=featurenum)
sims = idx[tfidf[new_vec]]

print("")
# print(sims)

index = 0
result = []

for sim in sims:
    if sim > 0:
        item = [keywords[index], sim]
        result.append(item)
        index += 1

result.sort(key=lambda x:x[1], reverse=True)

# keys = result[0].keys()
with open('F:/Temp/python/jieba/result.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
    # dict_writer = csv.DictWriter(output_file, keys)
    # dict_writer.writeheader()
    dict_writer = csv.writer(output_file)
    dict_writer.writerows(result)

# print(result)
