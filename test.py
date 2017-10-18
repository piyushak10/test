q = input('Type in a math problem: ')
data = q.split()
x = 0
y = 0
while (y == 0):

	if ('+' in data):
		ans = float(data[x]) + float(data[x+2])
		print (ans)
		data.remove(data[x+2])
		data.remove(data[x+1])
		data.remove(data[x])
		x = x + 2
	elif ('-' in data):
		ans = float(data[x]) + float(data[x+2])
		print (ans)
		x = x + 2
	elif ('*' in data):
		ans = float(data[x]) + float(data[x+2])
		print (ans)
		x = x + 2
	else:
		print ('Failed')
		y = 1