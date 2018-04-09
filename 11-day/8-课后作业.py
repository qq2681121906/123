a = []
c = 0
p = []
while c < 3:
    x = {} 
    b = {}
    b["名字"] = input("请输入名字:")
    if b in p:
        print("姓名重复请从新输入")
        continue
    p.append(b)
    x["年龄"] = int(input("请输入年龄:"))
    x["性别"] = input("请输入性别:")
    x["QQ"] = input("请输入QQ:")
    x["体重"] = int(input("请输入体重:"))
    x.update(b)
    a.append(x)
    c+=1
for i in a:
    print("*"*50)
    for j,v in i.items():
        print("%s:%s"%(j,v))
    print("*"*50)
z = 0
for i in a:
    z+=i["年龄"]
print("平均年龄为%0.2f"%(z/len(a)))
