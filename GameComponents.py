import Deck
import random

class Hand:
    def __init__(self, deck, card1 = 0, card2 = 0):
        self.cards = []
        self.value = 0
        if card1 != 0 and card2 != 0:
            self.cards.append(card1)
            self.cards.append(card2)

        elif card1 != 0:
            self.cards.append(card1)

        elif card2 != 0:
            self.cards.append(card2)

        else:
            self.cards.append(deck.deal_and_remove_card())
            self.cards.append(deck.deal_and_remove_card())

    def calculate_value(self):
        pass


    def draw_card(self):
        pass

    def hit(self):
        pass

    def double_down(self):
        pass

    def stand(self):
        pass


class Player():
    def __init__(self, deck):
        pass


class Dealer():
    def __init__(self, deck):
        pass