import sys, random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

def main():
    print('''BlackJack Rules:
    Try to get as close to 21 without going over.
    Kings, Queens and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')

    money = 5000

    while True: #Main loop


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
            return bet #Player entered a valid bet

def getDeck():
    deck =[]
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck



