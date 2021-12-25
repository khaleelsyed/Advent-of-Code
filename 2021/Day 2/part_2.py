with open('input.txt') as f:
	data = [tuple((instruction.split(' ')[0], int(instruction.split(' ')[1]))) for instruction in f.read().splitlines()]


def main_loop():
	horizontal_pos = 0
	
	# NOTE: Down is +ve, Up is -ve
	depth = 0
	aim = 0
	
	for instruction in data:
		direction = instruction[0]
		scalar = instruction[1]
		
		
		if direction == 'down':
			aim += scalar
		elif direction == 'up':
			aim -= scalar
		elif direction == 'forward':
			horizontal_pos += scalar
			depth += scalar * aim
	
	return horizontal_pos, depth


if __name__ == '__main__':
	x, y = main_loop()
	
	print(x * y)
