# nonlocal.py

#此示例示意nonlocal的用法
var = 100
def f1():   
    var = 200
    print('f1.var=',var)  #200
    def f2():
        var = 300
        nonlocal var
        print('f1.var=',var)  #300
    f2()
    print('f1.var=',var)  #300
f1()
print('全局的var=',var)  #100 

