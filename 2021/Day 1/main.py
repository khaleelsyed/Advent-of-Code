

with open('input.txt') as f:
	data = f.readlines()
	
counter = 0
prev = None
for current in data:
	current = int(current)
	try:
		if current > prev:
			counter += 1
	
	except TypeError as e:
		if str(e) != "'>' not supported between instances of 'int' and 'NoneType'":
			raise e
	
	finally:
		prev = current

print(counter)
