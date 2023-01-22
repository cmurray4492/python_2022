"""Deck from Fluent Python"""
import collections
from random import choice
from colorama import Fore, init

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """Basic card deck for class demo"""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


init()

print(f"{Fore.LIGHTCYAN_EX}Here are my deck results!")

beer_card = Card("7", "diamonds")
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0])

my_card = choice(deck)
print(f"{Fore.LIGHTCYAN_EX}My Card is {my_card}.")
print(my_card)

print("")
print("______________________")
print("")

for card in reversed(deck):
    print(card)
