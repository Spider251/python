#处理僵尸进程的示例(无BUG)

import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    sleep(3)
    print("Child %d process exit"%os.getpid())
    os._exit(3)
else:
    #非阻塞等待
    while True:
        p,status = os.waitpid(-1,os.WNOHANG)
        print("Child pid:",p)
        # 退出状态 os._exit(n)   status = n*256
        print("Child status:",os.WEXITSTATUS(status))
        if p != 0:
            break
        sleep(1)
    while True:
        print("Patent process......")
        sleep(2)
        