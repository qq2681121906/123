s_acc = "123456"
s_pwd = "abc"
acc = input("请输入账号")
pwd = input("请输入密码")
if s_acc == acc and s_pwd == pwd:
	print("登陆成功")
elif s_acc != acc and s_pwd == pwd:
	print("账号错误")
elif s_acc == acc and s_pwd != pwd:
	print("密码错误")

