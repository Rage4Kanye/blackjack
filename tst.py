import random

class Deck:
    """
    Suits
    Cards
    Deck
    Card_values
    """
    def __init__(self, number_of_decks):
        self.value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.suits = ['H', 'D', 'S', 'C']
        self.cards = [x + y for x in self.suits for y in self.value]
        self.deck = self.cards * number_of_decks

        self.card_value = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
            'A': 11
        }

    def deal_and_remove_card(self):
        """
        Return a card, then remove it from the deck.
        :return: A card
        """
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card
