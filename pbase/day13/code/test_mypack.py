# test_mypack.py

import mypack.menu #导入mtpack包内的menu模块

mypack.menu.show_menu()  #调用包内模块的show_menu函数


#导入mypack里的games文件夹内的contra.py
import mypack.games.contra

mypack.games.contra.play()
mypack.games.contra.game_over()

# #导入mypack里的games文件夹内的supermario.py
# import mypack.games.supermario
# mypack.games.supermario.play()

# #导入mypack里的games文件夹内的tanks.py
# import mypack.games.tanks#mypack下的games子包被导入
# mypack.games.tanks.play()