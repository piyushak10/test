import time
from random import *
print ('So... you like yourself a little bit of chance, eh?')
time.sleep(1)
print ('Well, you\'ve come to the right place!')
print ('Welcome to Piyush\'s Casino!')
time.sleep(1)
print (' ')
print ('===============Rules====================================================================================================')
print ('You start off with 100 coins and you can bid coins every round')
print ('If you win, you get the amount of your bid, but be careful, because if you lose, you lose your money!')
print ('You win if the two dice roll at least a eight when summed')
print ('At anytime, press Ctrl + C to quit')
print ('========================================================================================================================')
x = 0
pie = True
bal = 100
while (pie == True):
	while (x == 0):
		print ('Your balance is: ' + str(bal))
		if (int(bal) == 0):
			print ('Oops! Looks like you have no money left! Game over!')
			quit()
		time.sleep(2)
		input('Hit enter to continue')
		time.sleep(1)
		bid = input('Enter the number of coins you wish to bid: ')
		if (int(bid) < 1):
			print ('Please enter a valid number to bid!')
			break
		elif (int(bid) > bal):
			print ('You don\t have enough money to bid that much!')
			break
		else:
			print ('You will bid ' + str(bid) + ' coins')
		input('Click enter to continue')
		dice1 = randint(1, 6)
		dice2 = randint(1, 6)
		time.sleep(0.5)
		print ('Rolling...')
		time.sleep(1)
		print ('Dice 1: ' + str(dice1))
		print ('Dice 2: ' + str(dice2))
		
		if (dice1 + dice2 >= 8):
			print ('You won!')
			bal = bal + int(bid)
		else:
			print ('You lost...')
			bal = bal - int(bid)