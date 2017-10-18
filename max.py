import time
x = 1 - 1
while (x == 0):
	list = input('Enter two values: ')
	list.split()
	if (len(list) < 2):
		print ('Please enter 2 values!')
	else:
		x = 1
	max = int(max(list))
	print ('Max Value: ' + str(max))
	while (x == 1):

		while (len(list) >= 2):
			newval = input ('Enter another value: ')
			time.sleep(1)
			list.append(newval)
			if (newval > max):
				print ('New max value found: ' + newval)
			else:
				print ('No new max value found...')
