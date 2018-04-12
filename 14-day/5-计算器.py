#定义函数
def jisuanqi(x,y,fuhao):
    if fuhao == "+":
        z = x+y
        print("和是%.02f"%z)
    elif fuhao == "-":
        z = x-y
        print("差是%.02f"%z)
    elif fuhao == "*":
        z = x*y
        print("积是%.02f"%z)
    elif fuhao == "/":
        z = x/y
        if y != 0:
            print("商是%.02f"%z)
        else:
            print("输入错误")
x = float(input("请输入一个数字"))
y = float(input("请输入一个数字"))
z = input("请输入+-*/")
jisuanqi(x,y,z)            

