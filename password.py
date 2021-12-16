password = "a123456"
time = 3
while time >= 0:
	pwd = input("请输入密码")
	if pwd == password:
		print("成功登入")
		break
	else:
		time = time - 1
		if time == 0:
			print("byebye")
			break
		print("你剩下",time,"次机会")
		




