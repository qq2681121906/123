s_acc = "2681121906"
s_pwd = "123456"
s_bal = 10000
acc = input("请输入账号")
pwd = input("请输入密码")
if acc == s_acc and pwd == s_pwd:
	print("登陆成功")
	money = float(input("请输入取款金额:"))
	if money <= s_bal:
		print("已取金额:%.02f,剩余金额:%.02f"%(money,s_bal-money))
	elif money > s_bal:
		print("没钱取毛线")
else:
	print("非法账户")

