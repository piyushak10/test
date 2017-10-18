import math
print ('Welcome to the calculator!')
print ("Type in your problem using this format for every operation:")

print ('  * is multiply')
print ('  / is divide')
print ('  + is add')
print ('  - is subtract')
print ('  ** is exponent')
print ('  for square root use: sqrt')
print ('  sin, cos, & tan for trignometry')
print ('  Ex: 5*8')

poo = 0
pie = False
poop = ['sqrt', 'sin', 'cos', 'tan', 'cot']

while (poo == 0):

	while (pie == False):
	
		num1 = input('  Type in your number 1: ')
	
		oper = input('  Type in your operation: ')
		if (not (oper in poop)):
			num2 = input('  Type in your number 2: ')
	
	
		if (oper == '+'):
			print ('  The answer is: ', float(num1)+float(num2))
			pie = True
			quit()
		elif (oper == '-'):
			print ('  The answer is: ', float(num1)-float(num2))
			pie = True
			quit()
		elif (oper == '*'):
			print ('  The answer is: ', float(num1)*float(num2))
			pie = True
			quit()
		elif (oper == '/'):
			print ('  The answer is: ', float(num1)/float(num2))
			pie = True
			quit()
		elif (oper == '**'):
			print ('  The answer is: ', float(num1)**float(num2))
			pie = True
			quit()
		elif (oper == 'sqrt'):
			print ('  The answer is: ', math.sqrt(float(num1)))
			pie = True
			quit()
		elif (oper == 'sin'):
			print ('  The answer is: ', math.sin(float(num1)))
			pie = True
			quit()
		elif (oper == 'cos'):
			print ('  The answer is: ', math.cos(float(num1)))
			pie = True
			quit()
		elif (oper == 'tan'):
			print ('  The answer is: ', math.tan(float(num1)))
			pie = True
			quit()
		elif (oper == 'cot'):
			print ('  The answer is: ', math.cot(float(num1)))
			pie = True
			quit()
		else:
			print ('Type in a valid operation!')
			pie = False



