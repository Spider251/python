'''
实现猎人的功能
需要传入的参数:1.所有人员的字典
'''

# person 所有角色共有的属性
# survival 所有人员存活情况{1:0,2:1...} 键1代表角色号码,值0为死亡,1为存活
class hunter:
    def __init__(self,survival):
        self.survival = survival
    def fun(self):
        for i in self.survival:
            if i == 2:
                if self.survival[i] == 1:
                    pass
                elif self.survival[i] == 0:
                    print("猎人已经死亡")
                    self.say()
    def say(self):
        while True:
            a = input("杀人Y/放弃N:")
            if a == 'N':
                print("结束")
            elif a == 'Y':
                print("请选择要带走的角色:",end="")
                for i in self.survival:
                    if i != 2:
                        print(i,end=" ")
                print()
                a = input("杀死:")
                print(a,"已死")
                break

if __name__ == '__main__':
    a = {1:0,2:0,3:1}
    hunter = hunter(a)
    hunter.fun()