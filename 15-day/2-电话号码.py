def check_phone(phone):
    if phone.startswith("1") and len(phone) == 11:
        return True
    else:
        return False
#第一个功能
phone = input("请输入手机号")
result = check_phone(phone)
if result == False:
    print("手机号错误")
#另一个功能
phone2 = input("请输入手机号")
result = check_phone(phone2)
if result == False:
    print("手机号错误")
