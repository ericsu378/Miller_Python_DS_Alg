__author__ = 'ESU_2'

# Problem Solving with Algorithms and Data Structures Release 3.0
# Brad Miller, David Ranum
# September 22, 2013

# 1.7 Programming Exercises

# 10. Design a class to represent a playing card. Now design a class to represent a deck of
# cards. Using these two classes, implement a favorite card game.

import random
# A playing card needs 3 attributes, rank, suit, and blackjack value
# Suit power is Diamonds > Hearts > Spades > Clubs
# Card Value is from 2 to Ace
class Card:

    def __init__(self, rank, suit):

        self.rank = rank

        # For Jack, Queen, and King, mark card with value 10
        if self.rank > 10:
            self.value = 10
        else:
            self.value = self.rank

        # Define Suits
        if suit == 1: self.suit = 'Clubs'
        if suit == 2: self.suit = 'Spades'
        if suit == 3: self.suit = 'Hearts'
        if suit == 4: self.suit = 'Diamonds'

        # Define names for values
        if self.rank == 2: self.name = 'Two'
        if self.rank == 3: self.name = 'Three'
        if self.rank == 4: self.name = 'Four'
        if self.rank == 5: self.name = 'Five'
        if self.rank == 6: self.name = 'Six'
        if self.rank == 7: self.name = 'Seven'
        if self.rank == 8: self.name = 'Eight'
        if self.rank == 9: self.name = 'Nine'
        if self.rank == 10: self.name = 'Ten'
        if self.rank == 11: self.name = 'Jack'
        if self.rank == 12: self.name = 'Queen'
        if self.rank == 13: self.name = 'King'
        if self.rank == 14: self.name = 'Ace'

    # We want the print function to print the name and suit of card
    def __str__(self):
        return self.name + " of " + self.suit

    def __lt__(self, other):
        if self.getRank() == other.getRank():
            return self.getSuit() < other.getSuit()
        else:
            return self.getRank() < other.getRank()

    def __gt__(self, other):
        if self.getRank() == other.getRank():
            return self.getSuit() > other.getSuit()
        else:
            return self.getRank() > other.getRank()

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

# Helper Functions
# Generate a random card value
def generateCard():
    rank = random.randrange(2,15)
    suit = random.randrange(1,4)
    return rank, suit

# Draw a random card
def drawRandomCard():
    rank, suit = generateCard()
    card = Card(rank, suit)
    return card

# Generate a Deck of cards
def generateDeck():
    deck = []
    rankList = [(x+2) for x in range(13)]
    suitList = [(x+1) for x in range(4)]
    for rank in rankList:
        for suit in suitList:
            deck.append(Card(rank, suit))
    return deck

class Deck:
    def __init__(self, name):
        self.deck = generateDeck()
        self.name = name

    def drawCard(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def getDeckName(self):
        return self.name

def cardGameWar():
    print "War"
    deck = Deck('deck1')
    player1 = str(raw_input("Please enter player 1's name --> "))
    player2 = str(raw_input("Please enter player 2's name --> "))

    while int(raw_input("Please enter '1' to play, '0' to quit --> ")) == 1:
        if len(deck) < 3:
            print "Out of card!!!"
            break
        else:
            card1 = deck.drawCard()
            card2 = deck.drawCard()
            print "%s's card: %s \n%s's card: %s" % (player1, card1, player2, card2)
            if card1 > card2:
                print "%s Wins!" % (player1)
            else:
                print "%s Wins!" % (player2)


def main():
    cardGameWar()

if __name__ == '__main__': main()