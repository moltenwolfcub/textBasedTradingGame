import math
import random
import time

DEBUG_MODE = False

StartMinBalance = 5
StartMaxBalance = 50


#region utility methods
def wait(len: float) -> None:
	if not DEBUG_MODE:
		time.sleep(len)


def loadingAnimation(duration: float, prefix: str = "") -> None:
	if DEBUG_MODE:
		return

	speed: float=0.1
	iterations: int = math.ceil(duration/speed)

	total = 5
	width = 3

    #38 means change foreground color
    #2 means use rgb
    #the following 3 numbers are the rgb values
	colours = [
		"\033[38;2;255;0;0m", #red
    	"\033[38;2;0;255;0m", #green
    	"\033[38;2;0;128;255m", #blue
    	"\033[38;2;255;255;0m", #yellow
    	"\033[38;2;255;0;255m" #magenta
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

		full = prefix
		for c in chars:
			full += str(c)

		print(f"\r\033[K{full}", flush=True, end='')
		wait(speed)
	print(f"\r\033[K{reset}", end='')

def prettyPrint(text: str, speed: float = 0.06, enterOnEnd: bool = True) -> None:
	for c in text:
		print(c, end="", flush=True)
		wait(speed)
	if enterOnEnd:
		print("")

def prettyInput(text: str, speed: float = 0.06) -> str:
	prettyPrint(text, speed, False)
	return input("")
#endregion



def introMessage() -> None:
	prettyPrint("Welcome Trader!")
	name: str = prettyInput("What is your name? ") #TODO SANATISE INPUT AGHHGHAHGIAEH
	greeting = f"Hello {name},"
	speed = 0.75/len(greeting)
	prettyPrint(greeting, speed)
	prettyPrint("You will travel around and try and make as much profit as possible. ", 0.04, False)
	wait(0.25)
	prettyPrint("Good Luck!", 0.07)

def setupStats() -> None:
	prettyPrint("We are going to find out your starting stats.\nThis is up to fate so may the odds be ever in your favour")
	wait(0.4)

	prettyPrint("Firstly, ", enterOnEnd=False)
	prettyPrint("your starting balance...")
	loadingAnimation(3)
	startingBalance = random.randint(StartMinBalance, StartMaxBalance)
	prettyPrint(f"You are starting with £{startingBalance}")
	wait(0.4)

	prettyPrint("Next, ", enterOnEnd=False)
	prettyPrint("your goods...")
	wait(0.2)
	prettyPrint(f"You are starting with:")

	loadingAnimation(2, "\t")
	goldQuant = random.randint(3, 15)
	prettyPrint(f"\t- {goldQuant} Gold Pieces")

	loadingAnimation(2, "\t")
	silverQuant = random.randint(5, 23)
	prettyPrint(f"\t- {silverQuant} Silver Pieces")


def place() -> None:
	pass


def main() -> None:
	if not DEBUG_MODE:
		introMessage()
	wait(0.5)
	setupStats()
	


if __name__ == '__main__':
	main()
