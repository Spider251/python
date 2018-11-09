# price03.py


s = {'唐僧', '悟空', '八戒', '沙僧'}
for i in s:
    print(i)
else:
    print("遍历结束")

print("====================")
s = {'唐僧', '悟空', '八戒', '沙僧'}
i = iter(s) # 获取迭代器
while True:
    try:
        x = next(i) 
        print(x)
    except:
        print("迭代结束")
        break
