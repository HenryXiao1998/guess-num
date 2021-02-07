import random
r = random.randint(1, 100)

while True:
	num = input('请猜数字：')
	num = int(num)
	if num > r:
		print('输入的数字比答案大')
	elif num < r:
		print('输入的数字比答案小')
	elif num == r:
		print('你猜对了!')
		break
	