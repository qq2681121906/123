md = ["美队","钢铁侠","雷神","浩克","黑寡妇","鹰眼","幻视"]
for i in md:
    print("邀请%s来吃饭"%i)
print("共邀请了%d位嘉宾来赴宴"%len(md))
print("%s去约会不能来"%md[4])
md[4] = "洛基"
for i in md:
    print("邀请%s来吃饭"%i)
print("共邀请了%d为嘉宾来赴宴"%len(md))
print("我找到一个更大的桌子,能再来3个人")
md.insert(0,"星爵")
md.insert(4,"蜘蛛侠")
md.append("格鲁特")
for i in md:
    print("邀请%s来吃饭"%i)
print("共邀请了%d位嘉宾来赴宴"%len(md))
print("餐桌没送来,只能邀请两个")
for i in range(len(md)):
    if len(md) == 2:
        break
    print("%s,餐桌没来,不能邀请你们了"%md[0:1])
    md.pop(0)
for i in md:
    print("%s,请按时来吃饭"%i)
print("共邀请了%d位嘉宾来赴宴"%len(md))
del md[0:2]
print(md)
print("共邀请了%d为嘉宾来赴宴"%len(md))
