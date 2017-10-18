#!/usr/bin/env python
from random import randint
score = 0
wrongAns = 'WRONG! YOU FAILED!!'
print ('Are you ready to take the Math quiz?')

answer = input('Yes, No: ')

if (answer == 'Yes'):
	print ('Great, lets get started!')
elif (answer == 'No'):
	print ("Well thats too bad, cuz you're starting anyways!")
elif (answer == 'yes'):
	print ('Alright, lets begin!')
elif (answer == 'no'):
	print ('Sucks to be you, dude, we\'re starting loser!')
else:
	print ('Answer Yes or No... ending program')
	quit()



#Math quiz starts here.

numA = randint(5,10)

ans1 = input('Problem 1: What is ' + str(numA) + '^2? ')

if (ans1 == str(numA**2)):
	score = score + 1
	print ('Correct! Onwards!')
else:
	print (wrongAns + ' The correct answer was ' + str(numA**2))
	
numB = randint(10, 20)
numC = numB**2
ans2 = input('Problem 2: What is the square root of ' + str(numC) + '? ')
import math
if (ans2 == str(numB)):
	print ('Correct! Onwards!')
	score = score + 1
else:
	print (wrongAns + ' The correct answer was ' + str(numB))
	

num0 = randint(1,15)
num01 = randint(1,15)
ans3 = input('Problem 3: What is ' + str(num0) + ' x ' + str(num01) + '? ')
if (ans3 == str(num0*num01)):
	score = score + 1
	print ('Great Job!')
else:
	print (wrongAns + ' The correct answer was ' + str(num0*num1))

num1 = randint(1500, 4900)
num2 = randint(1, 1499)
ans4 = input('Problem 4: What is ' + str(num1) + ' - ' + str(num2) + '? ')

if (ans4 == str(num1-num2)):
	score = score + 1
	print('Amazing Work!')
else:
	print (wrongAns + ' The correct answer was ' + str(num1-num2))
	

num3 = randint(5, 25)
num4 = randint(2, 4)
ans5 = input('Problem 5: What is ' + str(num3) + '^' + str(num4) + '? ')

if (ans5 == str(num3**num4)):
	score = score + 1
	print ('Awesome Job!')
else:
	print (wrongAns + ' The correct answer was ' + str(num3**num4))
Grade = (score/5)*100

print ('You finished the quiz! Your score was: ' + str(Grade) + '%')

if (Grade == 100):
	print ('Perfect score! Amazing!')
elif (Grade >= 90):
	print ('You did good!')
elif (Grade >= 80):
	print ('You could have done better')
elif (Grade >= 70):
	print ('You need practice...')
elif (Grade >= 60):
	print ('Ok you failed')
else:
	print ('D:<')