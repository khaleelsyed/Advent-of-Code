import numpy as np

with open('input.txt') as f:
	data = [int(i) for i in f.read().splitlines()]

windows = np.convolve(data, np.ones(3), 'valid')

increases = 0
prev = windows[0]

for current in windows[1:]:
	if current > prev:
		increases += 1
	prev = current

print(increases)
