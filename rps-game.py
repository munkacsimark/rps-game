#!/usr/bin/env python

import os
import random

from i18n import i18n
from colors import *

def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

def printLine():
	print ('--------------')

def getLang(langInput):
	if langInput == '0' or langInput == 'en':
		return 'en'
	elif langInput == '1' or langInput == 'hu':
		return 'hu'
	else:
		return None

def getUserDecision(userDecisionInput):
	if userDecisionInput == '0' or userDecisionInput == 'exit':
		return 'exit'
	if userDecisionInput == '1' or userDecisionInput == i18n[lang]['ROCK']:
		return 1
	elif userDecisionInput == '2' or userDecisionInput == i18n[lang]['PAPER']:
		return 2
	elif userDecisionInput == '3' or userDecisionInput == i18n[lang]['SCISSORS']:
		return 3
	else:
		return 'invalid'

def getDecisionName(decisionNum):
	if decisionNum == 1:
		return i18n[lang]['ROCK']
	elif decisionNum == 2:
		return i18n[lang]['PAPER']
	else:
		return i18n[lang]['SCISSORS']

def getWinner(computerDecision, userDecision):
	if computerDecision == userDecision:
		return 'DRAW'
	elif computerDecision == 1:
		if userDecision == 2:
			return 'USER'
		else:
			return 'COMPUTER'
	elif computerDecision == 2:
		if userDecision == 1:
			return 'COMPUTER'
		else:
			return 'USER'
	else:
		if userDecision == 1:
			return 'USER'
		else:
			return 'COMPUTER'

def printResults(computerDecision, userDecision):
	printBold(i18n[lang]['COMPUTER'] + ': ' + getDecisionName(computerDecision))
	printBold(userName + ': ' + getDecisionName(userDecision))
	printLine()

def printWinner(winner):
	if winner == 'DRAW':
		printBlue(i18n[lang]['DRAW'] + '!')
	else:
		print(i18n[lang]['WINNER'] + ': ')
		if winner == 'USER':
			printGreen(userName)
		else:
			printRed(i18n[lang][winner])
	printLine()

def incrementWins(winner):
	if winner == 'COMPUTER':
		global computerWinNum
		computerWinNum += 1
	elif winner == 'USER':
		global userWinNum
		userWinNum += 1

def printStatistics():
	print(i18n[lang]['COMPUTER'] + ': ' + str(computerWinNum))
	print(userName + ': ' + str(userWinNum) + '\n')

# start of everything
computerWinNum = 0
userWinNum = 0

# get language
lang = None
while lang == None:
	clearScreen()
	lang = getLang(raw_input('Language\n[0] en\n[1] hu\n> ').strip())

clearScreen()

# getting user name
userName = raw_input(i18n[lang]['GIVE_NAME'] + ': ').strip()
clearScreen()

while True:

	# getting computer decision
	computerDecision = random.randint(1, 3)

	# getting user decision
	printBold(i18n[lang]['MAKE_DECISION'] + ': \n')
	userDecision = getUserDecision(raw_input(
		'[0] ' + i18n[lang]['EXIT'] +
		'\n[1] ' + i18n[lang]['ROCK'] +
		'\n[2] ' + i18n[lang]['PAPER'] +
		'\n[3] ' + i18n[lang]['SCISSORS'] +
		'\n> ').strip())

	clearScreen()
	# exit
	if userDecision == 'exit':
		printStatistics()
		printBold(i18n[lang]['BYE'] + ' ' + userName + '!\n')
		break

	# invalid decision
	elif userDecision == 'invalid':
		clearScreen()
		printRed(i18n[lang]['INVALID'] + '!')
		continue

	# print results then winner
	winner = getWinner(computerDecision, userDecision)
	printResults(computerDecision, userDecision)
	printWinner(winner)
	incrementWins(winner)
	