import sys
import re

# port = sys.argv[1]
# f = open('/home/tarena/AID1808/RE/day02/1.txt')
# d = f.read()

# pettern = port+r'.*'

# regex = re.search(pettern,d,flags=re.S).group()
# print(regex)


def get_address(port):
    f = open('/home/tarena/AID1808/RE/day02/1.txt')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        #已经读取到文件结尾
        if not data:
            return 'Not found the port'
        #匹配出首个单词
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
        if port == PORT:
            # pattern = r'address is (\w{4}\.\w{4}\.\w{4})'
            pattern = r'address is ((\d{1,3}\.){3}\d{1,3}/\d+|Unknow)'
            address = re.search(pattern,data).group(1)
            return address
        

if __name__ == '__main__':
    port = sys.argv[1]
    print(get_address(port))
