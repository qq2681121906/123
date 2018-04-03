a = 123456
b = 123456
i = 1
while True:
	c = int(input("请输入账号"))
	d = int(input("请输入密码"))
	if c == a and d == b:
		print("登录成功")
		e = input("请选择英雄0代表ADC,1代表肉,3代表法师")
		if e == "0":
			print("鲁班大师")
		elif e == "1":
			print("程咬金")
		elif e == "2":
			print("王昭君")
		break
	else:
		print("错误%d次"%i)
	i+=1
	if i == 4:
		print("账号被封")
		break
