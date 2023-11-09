import sys, random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def getBet(maxBet):
    # We'll ask the player how much money the bet will be
    while True: # Don't stop asking until a valid bet is inputed
        print(f"How much do you bet? (1-{maxBet} or QUIT")
        bet = input("> ").uppet().strip()
        if bet =="QUIT":
            print("Thanks for playing")
            sys.exit()
        if not bet.isdecimal():
            continue #For when the input is not decimal but is not "QUIT"
        bet = int(bet)
        if 1<=bet <=maxBet:
            return bet



