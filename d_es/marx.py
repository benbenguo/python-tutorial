#/usr/bin/python3
#_*_ coding:utf-8 _*_

from elasticsearch import Elasticsearch
import csv
import re

def createCSV():
    es = Elasticsearch(["127.0.0.1:9200"])

    query = {
        "query": {
            "bool": {
                "should": [
                    {
                        "match_phrase": {
                            "name": {
                                "query": "马克思",
                                "slop": 0
                            }
                        }
                    },
                    {
                        "match_phrase": {
                            "comment": {
                                "query": "马克思",
                                "slop": 0
                            }
                        }
                    }
                ]
            }
        },
        "size": 10000
    }

    res = es.search(index="keyword1", body=query)
    # print("total: ", res['hits']['total'])
    # print("list size: ", len(res['hits']['hits']))

    rawLines = []
    for hit in res['hits']['hits']:
        rawLine = hit["_source"]
        name = rawLine['name']
        comment = rawLine['comment']
        item = {'name': name, 'comment': comment}
        if item not in rawLines:
            rawLines.append(item)

    with open('F:/Temp/python/marx/result.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
        dict_writer = csv.DictWriter(output_file, rawLines[0].keys())
        dict_writer.writeheader()
        # dict_writer = csv.writer(output_file)
        dict_writer.writerows(rawLines)

def filterCSV():
    lines = []
    with open('F:/Temp/python/marx/result.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=',')
        lines = list(reader)

        index = 0
        for item in lines:
            if len(item) < 3 or item[2].strip() == "":
                name = str(item[0]).strip()
                comment = str(item[1]).strip()

                # if name.endswith("主义"):
                #     item[2] = "主义"
                # else:
                #     match1 = re.match(r".*?编入《(.+?)》.*", comment, re.M | re.I)
                #     if (match1 != None):
                #         item[2] = match1.group(1)
                # if "书名" in comment:
                #     item[2] = "书名"
                if name.endswith("论"):
                    item[2] = "理论"
            index += 1

    with open('F:/Temp/python/marx/result.csv', 'w', newline='', encoding='utf-8-sig') as output_file:
        # dict_writer = csv.DictWriter(output_file, keys)
        # dict_writer.writeheader()
        dict_writer = csv.writer(output_file)
        dict_writer.writerows(lines)