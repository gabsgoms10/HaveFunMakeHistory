import sys
import random

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

    while True:  # Main loop
        if money < 1:  # Making sure the player has money to bet
            print('''You're broke
            Good thing you weren't playing with real money
            Thanks for playing''')
            sys.exit()

        print(f"Money: {money}"

        bet = getBet(money)
        #Give two cards of the deck to each player
        Hands = getHand()
        dealerHand, playerHand = Hands[0], Hands[1]

        #Handle Player Actions
        print('Bet: ' bet)
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
        if getHandValue(playerHand)>21:
            break

        move = getMove(playerHand, money - bet)

        if move =='D':
            additionalBet = getBet(min(bet, (money-bet)))
            bet +=additionalBet
            print(f'Bet increased to {bet}')
            print('Bet: ', bet)

        if move in ('H', 'D'):
            newCard = deck.pop()
            rank, suit = newCard
            print('You drew a {} of {}.'.format(rank, suit))
            playerHand.append(newCard)

            if getHandValue(playerHand)>21:
                continue

        if move in('S', 'D'):
            break

    if getHandValue(playerHand) <=21:
        while getHandValue(dealerHand) <17:
            print('Dealer hits...')
            dealerHand.append(deck.pop())
            displayHands(playerHand, dealerHand, False)

            if getHandValue(dealerHand) >21:
                break
                input("Press enter to continue")
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getDealerValue(dealerHand)

        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            money +=bet
        elif (playerValue>21) or (playerValue<dealerValue):
            print("You lost")
            money -=bet
        elif playervalue > dealerValue:
            print(f"You won ${bet}")
            money +=bet
        elif playervalue==dealerValue:
            print("It's a tie, the bet returned to you")

        input("Press Enter to continue...")
        print('\n\n')



def getBet(maxBet):
 """Ask the player how much they want to bet for this round."""
    while True: # Keep asking until they enter a valid amount.
        print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
        continue # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet #  Player entered a valid bet.

def getDeck():
    deck =[]
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def getHand():
    deck = getDeck()
    dealerHand =[]
    playerHand=[]
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]
    return [dealerHand, playerHand]

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('Dealer:', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ????')
        #Hide dealer first card
        displayCards([BACKSIDE] dealerHand[1:])

    #show players cards
    print('PLAYER:', getHandValue(playerHand))
    displayCards(playerHand)

def getHandValue(cards):
    """Return the value of the cards. Face cards are worth 10, aces are worth 1 or 11
    (this function gets the most suitable value)."""
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank =="A":
            numberOfAces +=1
        elif rank in ('K','Q','J'):
            value +=10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <=21:
            value +=10

    return value

def displayCards(cards):
    rows = ['','','','']

    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        if card == BACKSIDE:
            #print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += f'|{rank.ljust(2)} | '
            rows[2] += f'| {suit} | '
            rows[3] += f'|_{rank.rjust(2, '_')}| '

    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']

        if len(playerHand)==2 and money >0:
            moves.append('(D)ouble down')

        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()
