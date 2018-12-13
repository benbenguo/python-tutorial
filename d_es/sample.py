#!/usr/bin/python3
#_*_ coding: utf8 _*_

from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(["127.0.0.1:9200"])

query = {
    "query": {
        "match_phrase": {
            "name": {
                "query": "马克思",
                "slop": 0
            }
        }
    },
    "size": 50
}

res = es.search(index="keyword1", body=query)
print("total: ", res['hits']['total'])
print("list size: ", len(res['hits']['hits']))


for hit in res['hits']['hits']:
    # print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    print( hit["_source"])