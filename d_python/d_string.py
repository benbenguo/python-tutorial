#_*_ coding:utf-8 _*_

# 字符串截取
vstr = 'python'
print("字符串截取")
print(vstr[2:])
print(vstr[:2])
print(len(vstr))

print("字符串前加r，将忽略转移字符")
# 字符串前加r，将忽略转移字符
print(r'E:\temp\dean\material\natural')

print("字符串首字母大写 capitalize")
vstr = 'python'
print(vstr.capitalize())

# reference: https://www.cnblogs.com/zhanmeiliang/p/5988207.html
print("字符串全小写，且对Unicode有效 casefold")
vstr = "I'm Dean"
print(vstr.casefold())

# center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
print(vstr.center(20))

# Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
print(vstr.count("m"))

# 元组字符串
value = ('www.opennews.com.cn', 'visit count', 100)
result = str(value)
# result = str(1/7)
sentence = ['this','is','a','sentence']
joinstr = '-'.join(sentence)
print(joinstr)
# result = ' '.join(str(i) for i in value)
print(result)

