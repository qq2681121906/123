def hero():
    yx = input("请输入英雄")
    a.append(yx)
a = []
while True:
    hero()
    if len(a) == 5:
        print(a)
        break
