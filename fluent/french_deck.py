"""French Deck example form Fluent Python - doesn't work directly from the book"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """French Deck example form Fluent Python"""
    ranks = [str(n) for n in range(2, 15)]  # + list['JQKA']
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


my_deck = FrenchDeck()

print(my_deck)
