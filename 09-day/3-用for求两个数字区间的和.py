while True:
	a = int(input("请输入第一个数字"))
	b = int(input("请输入第二个数字"))
	sum = 0
	if a < b:
		for i in range(a,b+1):
			print(i)
			sum = sum+i
		print(sum)
		break
	else:
		print("输入有误请从新输入")
