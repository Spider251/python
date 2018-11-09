import re

pattern = r'(ab)cd(?P<dogs>ef)'
regex = re.compile(pattern)

# 获取match对象
obj = regex.search('abcdefgh')

#obj属性变量
print(obj.pos)  # 目标字串的开始位置
print(obj.endpos)   # 目标字串的结束位置
print(obj.re)   # 正则表达式
print(obj.string)   # 目标字符串
print(obj.lastgroup)    # 最后一组的组名
print(obj.lastindex)    # 最后一组是几组
print("****************************")
print(obj.span())   #匹配内容的起止位置
print(obj.start())  #匹配内容的开始位置
print(obj.end())    #匹配内容的结束位置

print(obj.group())  #获取正则表达式匹配到的内容
print(obj.group('dogs')) #获取dogs子组匹配到的内容

print(obj.groupdict())  #捕获组字典
print(obj.groups()) #所有子组对应内容