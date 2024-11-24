# Case Study: Deck of Cards
from random import shuffle

# Card Class
# Attributes: 
# -- Suit (Spades, Hearts, Clubs, Diamonds)
# -- Ranks: (2 to 10 + Jack, Queen, King, Aces)
# Methods:
#  -- getters for suit and rank
#  -- make it printable
class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
    
    @property # read-only getter for suit
    def suit(self):
        return self._suit
    
    @property # read-only getter for rank
    def rank(self):
        return self._rank

    # printable
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card({self.suit}, {self.rank})"
# end of Class

# Deck class: 52 card objects.
# Implement a method in the Deck class to shuffle the cards randomly.
# Implement a method in the Deck class to deal a specified number of cards from the top of the deck.
class Deck:
    SUITS = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
    RANKS = [str(x) for x in range(2,11)] + ['Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self._deck = [Card(s, r) for s in self.SUITS for r in self.RANKS]
    
    @property # getter for deck
    def deck(self):
        return self._deck
    
    def shuffle(self):
        # non returning method
        shuffle(self.deck) # this is executing the random's shuffle function
    
    def deal(self, num):
        # let num represent the number of cards to be dealt
        if num > len(self.deck):
            raise ValueError(f"{num} is greater than the number of cards in the deck.")
        else:
            return [self.deck.pop() for _ in range(num)]


# Player class: with a hand attribute to hold a player's cards.
# Implement a method in the Player class to add a card to the player's hand.
# Implement a method in the Player class to display the cards in the player's hand.

class Player:
    def __init__(self):
        self._hand = [] # Empty list to be initialized
    
    @property # getter for hand
    def hand(self):
        return self._hand
    
    def add_cards(self, card_list):
        self._hand += card_list 
# end of Player

p1 = Player()
d1 = Deck()
d1.shuffle()

dealt_cards = d1.deal(5)
p1.add_cards(dealt_cards)

print(p1.hand)