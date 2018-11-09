#处理僵尸进程的示例

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
    pid,status = os.wait()
    print("Child pid:",pid)
    # 退出状态 os._exit(n)   status = n*256
    print("Child status:",os.WEXITSTATUS(status))
    print("Patent process......")
    while True:
        pass