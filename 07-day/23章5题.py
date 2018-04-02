stature = float(input("请输入身高"))
money = float(input("请输入身价"))
nice = float(input("请输入颜值分"))
if stature > 180 and money > 1000 and nice > 99:
	print("高富帅")
elif money > 1000 and nice > 99:
	print("富帅")
elif nice > 99:
	print("帅")
elif stature < 160 and money < 100 and nice < 60:  
	print("矮穷矬")

