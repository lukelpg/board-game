from .deck import Deck
from .player import Player

class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.deck = Deck()
        self.deck.shuffle()
        self.current_player_index = 0
        self.max_rounds = 10
        self.rounds_played = 0

    def start_game(self):
        print(f"Starting the game with {len(self.players)} players.")
        self.deal_cards()
        while self.rounds_played < self.max_rounds:
            self.play_round()
            self.rounds_played += 1
        print("Game Over")

    def deal_cards(self):
        print("Dealing cards to players...")
        for player in self.players:
            for _ in range(5):  # Deal 5 cards to each player
                player.draw_card(self.deck)

    # In game.py - update the play_round method to call next_turn appropriately
    def play_round(self):
        print(f"\nRound {self.rounds_played + 1}:")
        current_player = self.players[self.current_player_index]
        print(f"{current_player.name}'s turn with hand: {current_player.hand}")

        card_played = current_player.play_card()
        print(f"{current_player.name} plays {card_played}")

        # Move to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)


    def __repr__(self):
        return f"Game({len(self.players)} players, {len(self.deck.cards)} cards left)"
