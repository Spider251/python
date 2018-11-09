import re


s = '''hello world
hello kitty
你好 北京!
'''
pattern = r'''hello#匹配hello
\s+#匹配空格
world#匹配world
'''
regex = re.compile(pattern,re.X)

try:
    s = regex.search(s).group()
except Exception:
    print('没有匹配到内容')
else:
    print(s)