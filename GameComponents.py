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

    def calculate_value(self, deck):

        ##TODO Fix issue when player is dealt 'A' 'A', this will return 'a' 'a', need to be 'A' 'a'

        score = 0

        def ace_check():
            for card in self.cards:
                if card == 'A':
                    return True

        def ace_replace():
            for card_pos in range(len(self.cards)):
                if self.cards[card_pos] == 'A':
                    self.cards[card_pos] = 'a'
                    break

        for card in self.cards:
            score += deck.card_value[card]
        if score < 21:
            return score

        if score == 21:
            return score

        if score > 21:
            if ace_check:
                ace_replace()
                self.calculate_value(deck)
            else:
                return 'bust'


    def add_card(self, deck):
        self.cards.append(deck.deal_and_remove_card())

    def hit(self, deck):
        self.add_card(deck)

    def double_down(self, deck):
        self.add_card(deck)

    ##TODO Add split eventually
    def split(self):
        pass

    def stand(self):
        pass


class Player():
    def __init__(self, deck):
        player_hands = []




class Dealer():
    def __init__(self, deck):
        pass