tell.py


f = open("data.txt")
f.read(3)
print("当前读写位置是:",f.tell())

f.close()