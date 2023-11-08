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
            secretNum = getSecretNum()
            print('I have thought up a Number.')
            print('You have {} guesses to get it.'.format(MAX_GUESSES))

           numGuesses = 1
           while numGuesses <= MAX_GUESSES:
               guess =''
               while len(guess) != NUM_DIGITS or guess.isdecimal():
                   print('Guess #{}: '.format(numGuesses))
                   guess = input('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

                if guess == secretNum:
                    break
                if numGuesses>MAX_GUESSES:
                    print('You ran out of guesses.')
                    print(f'The answer was {secretNum}.')

            print('Do you want to play again? (yes or no)')
            if not input('> ').lower().startswith('y'):
                break
        print('Thanks for playing!')

def getSecretNum():
    '''Returns a string made up of NUM_DIGITS unique random digits.'''
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


