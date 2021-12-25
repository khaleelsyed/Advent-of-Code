with open('input.txt') as f:
	data = [tuple((instruction.split(' ')[0], int(instruction.split(' ')[1]))) for instruction in f.read().splitlines()]


def main_loop():
	horizontal_pos = 0
	depth = 0  # Down is +ve, Up is -ve
	
	for instruction in data:
		direction = instruction[0]
		scalar = instruction[1]
		
		if direction == 'forward':
			horizontal_pos += scalar
		elif direction == 'down':
			depth += scalar
		elif direction == 'up':
			depth -= scalar
	
	return horizontal_pos, depth


if __name__ == '__main__':
	x, y = main_loop()
	
	print(x * y)
