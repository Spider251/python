#经过优化后，2个1000可能会合并成为1个1000,两个地址相同，ｐｙｔｈｏｎ优化！！
a = 1000
b = 1000
print(id(a))
print(id(b))
print(a is b)   #True
