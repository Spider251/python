# caocao.py
jl = {'曹操','刘备','孙权'}
jsy = {'曹操','孙权','张飞','关羽'}
a = jl & jsy
b = jl - jsy
c = jsy - jl
d = '张飞' in jl
f = jl ^ jsy
g = (jsy - jl) | (jl - jsy) | (jl & jsy)
print(a,b,c,d,f,g)