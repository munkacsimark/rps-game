import sys

RED = '\033[1;31m'
GREEN = '\033[0;32m'
BLUE = '\033[1;34m'
RESET = '\033[0;0m'
BOLD = '\033[;1m'

def printRed(str):
	sys.stdout.write(RED)
	print(str)
	sys.stdout.write(RESET)

def printGreen(str):
	sys.stdout.write(GREEN)
	print(str)
	sys.stdout.write(RESET)

def printBlue(str):
	sys.stdout.write(BLUE)
	print(str)
	sys.stdout.write(RESET)

def printBold(str):
	sys.stdout.write(BOLD)
	print(str)
	sys.stdout.write(RESET)