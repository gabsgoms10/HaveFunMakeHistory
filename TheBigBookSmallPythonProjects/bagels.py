# Escreva o seu código aqui :-)
import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When i say:  That means:
 Pico        One digit is correct but in wrong position.
 Fermi       One digit is correct and in the right position.
 Bagels      No digit is correct.

 For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.'''.format(NUM_DIGITS))
        while True:
            secretnum = getSecretNum()
            print('I have thought up a Number.')
            print('You have {} guesses to get it.'.format(MAX_GUESSES))

           numGuesses = 1
           while numGuesses <= MAX_GUESSES:
               guess =''
               while len(guess) != NUM_DIGITS or guess.isdecimal():
                   print('Guess #{}: '.format(numGuesses))
                   guess = input('> ')

