# test.py

class Process(object):
    def start(self):
        #假设对run已经进行了很复杂的调用
        self.run()
    def run(self):
        #"不知道要做什么,需要用户自己决定"
        pass

class myClass(Process):
    def run(self):
        print("根据自己的功能编写")

obj = myClass()
obj.start()