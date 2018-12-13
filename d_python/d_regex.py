#/usr/bin/python3
#_*_ coding:utf-8 _*_

import re

line = "年而写，发表于1913年3月。编入《列宁全集》第2版第23卷、《列宁选集》第3版第2卷。文章回顾和总结了《共产党宣言》发表以来马克思主义在同工人运动的结合中、在同各"
matchObj = re.match(r".*?编入《(.+?)》.*", line, re.M|re.I)
if (matchObj != None):
    print(matchObj.group(1))