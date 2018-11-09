# price.py

# 练习:
#   1.输入一个圆的半径,打印出这个圆的面积
#   2.输入一个圆的面积,打印出这个圆的半径
# 
from math import pi, sqrt
R = float(input("请输入圆的半径:"))
print('圆的面积=',pi*(R**2))
M = float(input("请输入圆的面积:"))
print('圆的半径=',sqrt(M/pi))     


