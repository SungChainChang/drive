country = input('輸入國籍: ')
age = input('輸入年齡: ')
age = float(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country == '美國':
	if age >=16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('你只能輸入台灣/美國')
	