country = input ('哪國人呢??')
age = input ('年齡呢??')

age = int (age)

if country == '台灣' :
	if age >= 18:
		print ('可以開車')
	else :
		print('不可以開車')
else :
	print ('不是台灣')