def xitong():
    padu = 0
    zid = {}
    xh = input("请输入学号")
    for i in lie:
        if xh == i["学号"]:
            padu = 1
            break
    if padu == 1:
        print("学号重复")
    else:
        name = input("请输入姓名")
        shu = float(input("请输入数学成绩:"))
        yu = float(input("请输入语文成绩:"))
        ying = float(input("请输入英语成绩:"))
        zid["学号"] = xh
        zid["姓名"] = name
        zid["数学成绩"] = shu
        zid["语文成绩"] = yu
        zid["英语成绩"] = ying
        lie.append(zid)
def cha():
    panduan = 0
    padu = input("请输入学号:")
    for i in lie:
        if padu == i["学号"]
            panduan = 1
            for j,v in i.items():
                print("%s:%s"%(j,v))
    if panduan == 0:
        print("查无此人")
def xiu():
    padu = 0
    xuehao = input("请输入学号:")
    for i in lie:
        if xuehao == i["学号"]:
            padu = 1
            xm = input("请输入修改项1(学号),2(姓名)3,(成绩)")
            if xm == "1":
                while True:
                    pd = 0
