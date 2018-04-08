import random
import time
list=["薛栋炎","李双双","刘瑞涛","娄雪嫚","张轩轩","郑成峰","郝竟良","张晨波","王晓俊","刘明松","崔利艳","尹天","张圆","那思源","韩月瑞","王保轩","贾纪闯","翟宏乐","崔健","杨振亚","闫子雄","梁文琦","李冰","陈怡杰","韩迪","周肸","张世豪","李明瑞","王琳","于奇林","吴金航","王含青","王润泽"]
print("班级总人数:%d人"%len(list))
print("正在合理计算中\n")
time.sleep(3)
i = random.randint(0,len(list)-1)
print("呦,你被上帝看中了:------ %s"%list[i])
list.pop(i)
j = random.randint(0,len(list)-1)
print("呦,你看着也很不错呀:------%s\n"%list[j])

k = int(input("如果想查看奖励请继续:\n1继续 0退出\n"))
if k == 1:
	count = random.randint(5,30)
	print("上帝奖励了你们组%d个俯卧撑"%count)
else:
	print("欢迎下次使用")
