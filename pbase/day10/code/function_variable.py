# function_variable.py

#此示例示意函数名绑定函数,函数名是变量
def fn():
    print("hello world")
    
f1 = fn
print(f1)
fn()
f1()
f2 = fn()
print()