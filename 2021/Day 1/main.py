with open('input.txt') as f:
	data = [int(i) for i in f.read().splitlines()]
	
increases = 0
prev = data[0]
for current in data[1:]:
	if current > prev:
		increases += 1
	prev = current

print(increases)
