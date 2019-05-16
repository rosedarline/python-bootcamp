import unittest
from deck_of_cards import Card, Deck

class CardTest(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """Cards should a suit, and a value"""
        self.assertEqual(self.card.suit, "Heart")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), "A of heart")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attribut, which is a list with 52 elements."""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string of form, 'Deck of COUNT cards.'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards.")

    def test_count(self):
        """count should return a count of the number of cards in the deck."""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

        
