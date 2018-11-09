import re 
f = open('/home/tarena/AID1808/RE/day01/price.py')
data = f.read()
# pattern = r'\b[A-Z]\S*'
pattern = r'-?\d+\.?/?\d*%?'

l = re.findall(pattern,data)
print(l)