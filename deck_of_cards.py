from random import shuffle

class Card:
   
    def __init__(self, suit,value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.suit} of {self.value}"

c = Card("A", "Hearts")
c2 = Card("10", "Diamonds")
c3 = Card("K", "Spades")
print(c, c2, c3)
class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4","5", "6", "7", "8", "9", "10", "J","Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values ]
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def deal_cards(self):
        return self._deal(1) [0]
    
    def deal_hands(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
    
d = Deck()
d.shuffle()
card = d.deal_cards()
print(card)
hand = d.deal_hands(50)
card2 = d.deal_cards()
print(card2)
print(d.cards)
card2 = d.deal_cards()
