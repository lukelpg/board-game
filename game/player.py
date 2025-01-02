class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw()
        if card:
            self.hand.append(card)
        return card

    def play_card(self):
        return self.hand.pop() if self.hand else None

    def __repr__(self):
        return f"Player({self.name}, Hand: {len(self.hand)} cards)"
