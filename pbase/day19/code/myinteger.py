# myinteger.py

class myinteger:
    def __init__(self, value):
        self.data = int(value)
    def __int__(self):
        '''此方1法必须返回整数'''
        return  self.data
    def __float__(self):
        return float(self.data)
    
a1 = myinteger("100")
i = int(a1)  #将myinteger转为整数
print(i)

f = float(a1)   #a1.__float__()
print(f)

c = complex(a1)  # a1.__complex__()
print(c)

d = bool(a1)    # a1.__bool__()
print(d)