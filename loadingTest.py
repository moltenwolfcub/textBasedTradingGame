import math, time, random


def loadingAnimation(duration: float):
	# if DEBUG_MODE:
	# 	return

	speed: float=0.1
	iterations: int = math.ceil(duration/speed)

	total = 25
	width = 10

    #38 means change foreground color
    #2 means use rgb
    #the following 3 numbers are the rgb values
	colours = [
		"\033[38;2;255;0;0m", #red
    	"\033[38;2;0;255;0m", #green
    	"\033[38;2;0;128;255m", #blue
    	"\033[38;2;255;255;0m" #yellow
	]
	reset = '\033[0m'

	direction = 1
	index = -width
	currentColour = random.choice(colours)
	colCopy = colours.copy()
	colCopy.remove(currentColour)

	for _ in range(iterations):
		index += direction
		if index == total+width:
			direction = -1
			currentColour = random.choice(colCopy)
			colCopy = colours.copy()
			colCopy.remove(currentColour)
		elif index == 0:
			direction = 1
			currentColour = random.choice(colCopy)
			colCopy = colours.copy()
			colCopy.remove(currentColour)

		chars = []
		for _ in range(total):
			chars.append(f"{reset}□")

		for j in range(width):
			location = j+index-width
			if location < 0 or location >= total:
				continue

			chars[location] = f"{currentColour}■"

		full = ""
		for c in chars:
			full += str(c)

		print(f"\r\033[K{full}", flush=True, end='')
		time.sleep(speed)
	print("\r\033[K", end='')

loadingAnimation(10000)
