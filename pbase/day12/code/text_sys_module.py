# text_sys_module.py

import sys
print('hello')
print('Current Version is:',sys.version_info[:3])

sys.exit()#最强boos，终止所有后面的程序

#sys.argv 能够得到命令行参数
print('sys.argv=',sys.argv)