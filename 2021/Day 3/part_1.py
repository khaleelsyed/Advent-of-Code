with open('input.txt') as f:
	data = f.read().splitlines()

# Bits per Line
bpl = len(data[0])

output = [0 for i in range(bpl)]

for line in data:
	for i in range(bpl):
		if line[i] == '1':
			output[i] += 1
		elif line[i] == '0':
			output[i] -= 1

gamma = int(''.join(['1' if i > 0 else '0' for i in output]), 2)
epsilon = int(''.join(['0' if i > 0 else '1' for i in output]), 2)

print(gamma * epsilon)
