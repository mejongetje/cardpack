class Card:

    """
    Card Class - creates a card instance with a specified suit and rank. 
    The suit and rank are matched with the list provided in the class to get the 
    cards name.

    Card instances can be compared with eachother, through the __lt__ method.
    The __eq__ method is not used, to avoid conflicts with hashing, which is 
    used in the CustomizeDeck class. Equalitity can be tested with card.rank
    or card.value.
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = None
        self.trump = False
        card_suit = list('hsdc')
        card_rank = list('A23456789TJQK')
        self.name = f'{card_rank[self.rank-1]}{card_suit[self.suit]}'


    def __repr__(self):
        return self.name


    def __iter__(self):
        return self


    def __lt__(self, other):
        if self.trump and other.trump:
            if self.value:
                return self.value < other.value
            else:
                return self.rank < other.rank
        elif self.trump and other.trump == False:
            return self.rank < 0
        elif other.trump and self.trump == False:
            return self.rank < 100
        elif self.value:
            return self.value < other.value
        else:
            return self.rank < other.rank


    def __add__(self, other):
        if isinstance(other, Card):
            if self.value:
                return self.value + other.value
            else:
                return self.rank + other.rank

