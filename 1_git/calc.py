import sys


while(True):
	print("1 : Add two numbers")
	print("2 : Add subtract numbers")
	print("3 : To exit")
	print("Enter your choice")
	choice = raw_input()
	if choice == '1':
		a = float(raw_input())
		b = float(raw_input())
		print("result = " +  str(a + b))
	elif choice == '1':
		a = float(raw_input())
		b = float(raw_input())
		print("result = " +  str(a - b))
	elif choice == '3':
		sys.exit()
	else:
		print('invalid choice')
	
