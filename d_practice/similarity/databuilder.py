#/usr/bin/python3
#_*_ coding:utf-8 _*_

import psycopg2
import pymongo

"""
    获取 PG 数据库连接
"""
def connect():
    try:
        conn = psycopg2.connect("dbname='cishu' user='devuser' host='localhost' password='devuser'")
        return conn
    except:
        print("I am unable to connect to the database")

"""
    生成分词数组
"""
def makeData(conn):
    cur = conn.cursor()
    cur.execute("""SELECT id, title from cishu_bas_entry""")
    rows = cur.fetchall()

    tags = []
    entries = []
    index = 0
    for row in rows:
        # print("id: %s, title: %s" % (row[0], row[1]))
        tags.clear()

        cur.execute("""SELECT author.name, dynasty.name, type.cst_code_desc 
                       FROM cishu_bas_entry as entry, 
                            cishu_article as article, 
                            cishu_author as author, 
                            cishu_author_dynasty as dynasty, 
                            cishu_cst_info as type 
                       WHERE 
                            entry.id=article.article_id 
                            AND 
                            article.author_id = author.id 
                            AND 
                            dynasty.id = author.dynasty_id 
                            AND 
                            entry.type_key = type.cst_type 
                            AND 
                            entry.type_code = type.cst_code 
                            AND 
                            type.cst_type = {0} 
                            AND 
                            entry.id='{1}' """.format(10002, row[0]))

        authorOrDynasty = cur.fetchall()
        if (len(authorOrDynasty) > 0):
            tags.append(authorOrDynasty[0][0])
            tags.append(authorOrDynasty[0][1])
            tags.append(authorOrDynasty[0][2])

        cur.execute(""" SELECT book.name  
                        FROM cishu_bas_entry as entry, 
                             cishu_article_book as ab, 
                             cishu_book as book 
                         WHERE 
                             entry.id = ab.article_id 
                             AND 
                             ab.book_id = book.id 
                             AND 
                             entry.id='{}' """.format(row[0]))

        books = cur.fetchall()
        for book in books:
            tags.append(book[0])

        entries.append({
            "id": row[0],
            "index": index,
            "title": row[1],
            "tags": tags[:]
        })

        index += 1

    return entries

def save2mongo(entries):
    client = pymongo.MongoClient("192.168.1.46")
    client.cishu.simdata.insert_many(entries)
    return


conn = connect()
entries = makeData(conn)
save2mongo(entries)