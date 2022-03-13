# Matthew Ortega
from termcolor import colored
import random 
'''
Directions:
---------------
Guess a country within 5 attempts, it will start to print out the words that the country starts with depending on the amount of attempts

'''
Wordlibrary = open("Countries.txt")
Wordlibrary = Wordlibrary.readlines()
Loop = False

def WordLoop():
	Word = Wordlibrary[random.randint(1, 197)]
	Guesses = 1
	Response = "Yes"
	while(Guesses < 7):		
		WordGuess = str(input(colored("\nGuess the Country: ", 'blue')))
		if (WordGuess.upper() + "\n" == Word.upper()):
			print(colored("Correct", 'green'))
			print("The country was in fact: " + Word)
			break
		elif(Guesses == 6 or Guesses > len(Word) - 1):
			print("The country was: " + Word)
			Reply = str(input(colored("\nDo you want to play again? ", 'blue')))
			if(Reply.upper() == Response.upper()):
				WordLoop()
			else:
				print(colored("\nGame Over", 'red'))
				break
			
		elif(WordGuess != Word):
			print("\nIncorrect\n")
			print("The Country starts with the letter: " + Word[0 : Guesses])
		Guesses +=1
WordLoop()
