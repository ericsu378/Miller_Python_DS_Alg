__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 1.17 Programming Exercises

# 14. Design a class to represent a playing card. Now design a class to represent a deck of
# cards. Using these two classes, implement a favorite card game.

# Game: War

import random
# A playing card needs 3 attributes, rank, suit, and blackjack value
# Suit power is Diamonds > Hearts > Spades > Clubs
# Card values range from 2 to Ace
class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.card_name = None
        self.card_value = None
        self.suit_name = None
        self.suit_value = suit

        # Define Suits
        if suit == 1: self.suit_name = 'Clubs'
        if suit == 2: self.suit_name = 'Spades'
        if suit == 3: self.suit_name = 'Hearts'
        if suit == 4: self.suit_name = 'Diamonds'

        # Define names for values
        if self.rank == 2: self.card_name = 'Two'
        if self.rank == 3: self.card_name = 'Three'
        if self.rank == 4: self.card_name = 'Four'
        if self.rank == 5: self.card_name = 'Five'
        if self.rank == 6: self.card_name = 'Six'
        if self.rank == 7: self.card_name = 'Seven'
        if self.rank == 8: self.card_name = 'Eight'
        if self.rank == 9: self.card_name = 'Nine'
        if self.rank == 10: self.card_name = 'Ten'
        if self.rank == 11: self.card_name = 'Jack'
        if self.rank == 12: self.card_name = 'Queen'
        if self.rank == 13: self.card_name = 'King'
        if self.rank == 14: self.card_name = 'Ace'

        # Card Values for War
        self.card_value = self.rank

        # # **Note** For other cards games
        # # For Jack, Queen, and King, mark card with value 10
        # # For Ace, mark card with value 11
        # if self.rank > 10:
        #     self.card_value = 10
        # elif self.rank == 14:
        #     self.card_value = 11
        # else:
        #     self.card_value = self.rank

    # We want the print function to print the name and suit of card
    def __str__(self):
        return self.card_name + " of " + self.suit_name

    # Overriding operators due to non-canonical comparisons
    def __lt__(self, other):
        if self.getCardValue() == other.getCardValue():
            return self.getSuitValue() < other.getSuitValue()
        else:
            return self.getCardValue() < other.getCardValue()

    def __gt__(self, other):
        if self.getCardValue() == other.getCardValue():
            return self.getSuitValue() > other.getSuitValue()
        else:
            return self.getCardValue() > other.getCardValue()

    def getRank(self):
        return self.rank

    def getCardName(self):
        return self.card_name

    def getCardValue(self):
        return self.card_value

    def getSuitName(self):
        return self.suit_name

    def getSuitValue(self):
        return self.suit_value


# Helper Functions
# Generate a random card value
def generateCard():
    rank = random.randrange(2,15) # return randomly selected element from range(start, stop, step)
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
        card = random.choice(self.deck) # returns a random element from a non-empty sequence
        self.deck.remove(card)
        return card

    def getDeckName(self):
        return self.name

    def getDeckSize(self):
        return len(self.deck)

def cardGameWar():
    print("Card Game: War")
    deck = Deck('deck1')
    player1 = str(input("Please enter player 1's name --> "))
    player2 = str(input("Please enter player 2's name --> "))

    while int(input("Please enter '1' to play, '0' to quit --> ")) == 1:
        if deck.getDeckSize() < 2:
            print("Out of cards!!!")
            break
        else:
            card1 = deck.drawCard()
            card2 = deck.drawCard()
            print("%s's card: %s \n%s's card: %s" % (player1, card1, player2, card2))
            if card1 > card2:
                print("%s Wins!" % (player1))
            else:
                print("%s Wins!" % (player2))


def main():
    cardGameWar()

if __name__ == '__main__': main()