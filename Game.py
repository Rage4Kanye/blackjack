import Deck
import GameComponents

class Game:
    def __init__(self):
        self.game_deck = Deck.Deck(6)
        self.player = GameComponents.Player(self.game_deck)
        self.dealer = GameComponents.Dealer(self.game_deck)
    
