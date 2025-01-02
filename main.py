import tkinter as tk
from tkinter import messagebox
from game.game import Game

class CardGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Petty Theft")
        
        self.game = None
        self.current_player_index = 0

        # Set up canvas for displaying the game
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="green")
        self.canvas.pack()

        # Status label to show whose turn it is
        self.status_label = tk.Label(self.root, text="Welcome to the Card Game!", font=("Arial", 16))
        self.status_label.pack()

        # Button to start the game
        self.play_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.play_button.pack()

        self.selected_card = None  # To keep track of the selected card

    def start_game(self):
        """ Start the game with 3 players and shuffle the deck. """
        # self.display_card()
        player_names = ["Alice", "Bob", "Charlie"]
        self.game = Game(player_names)
        self.game.start_game()
        
        self.play_button.config(state=tk.DISABLED)  # Disable the Start Game button
        self.update_game_display()  # Update display to show player's cards

    def update_game_display(self):
        """ Updates the game display on the canvas """
        self.canvas.delete("all")  # Clear the canvas

        if self.game:
            current_player = self.game.players[self.current_player_index]
            self.status_label.config(text=f"{current_player.name}'s Turn")

            # Display cards in hand for the current player
            x_offset = 50
            for i, card in enumerate(current_player.hand):
                self.display_card(card, x_offset, 500, i)

            # Display played card (if any)
            if current_player.hand:
                self.display_played_card(current_player.hand[0], 350, 100)

    def display_card(self, card, x, y, index):
        """ Display a card in the player's hand and set up click interaction """
        try:
            image_path = f"./game/images/{card.rank}_of_{card.suit}.png"
            image = tk.PhotoImage(file=image_path)
            card_id = self.canvas.create_image(x, y, image=image)
            self.canvas.image = image  # Keep a reference to avoid garbage collection
            self.canvas.tag_bind(card_id, "<Button-1>", lambda event, card=card: self.play_card(card))
            self.canvas.tag_bind(card_id, "<Enter>", lambda event, card=card: self.on_card_hover(event, card, True))
            self.canvas.tag_bind(card_id, "<Leave>", lambda event, card=card: self.on_card_hover(event, card, False))
        except Exception as e:
            print(f"Error loading card image: {e}")
            self.canvas.create_text(x, y, text=str(card), font=("Arial", 12))

    def display_played_card(self, card, x, y):
        """ Display the card played at the center of the screen """
        try:
            image_path = f"images/cards/{card.rank}_of_{card.suit}.png"
            image = tk.PhotoImage(file=image_path)
            self.canvas.create_image(x, y, image=image)
        except Exception as e:
            print(f"Error loading played card image: {e}")
            self.canvas.create_text(x, y, text=str(card), font=("Arial", 12))

    def play_card(self, card):
        """ Play a card when clicked and move to the next turn """
        current_player = self.game.players[self.current_player_index]
        
        if card in current_player.hand:
            # Remove card from player's hand and update display
            current_player.hand.remove(card)
            self.game.play_round()  # Update the game after playing a card

            # Check if the game has ended (if rounds are over)
            if self.game.rounds_played >= self.game.max_rounds:
                self.end_game()
            else:
                self.update_game_display()  # Update display for next turn
        else:
            print("Invalid card selection!")

    def on_card_hover(self, event, card, hover):
        """ Handle card hover to change appearance """
        if hover:
            print(f"Hovering over card: {card}")
        else:
            print(f"Left hover over card: {card}")

    def next_turn(self):
        """ Go to the next player's turn and update the display """
        self.current_player_index = (self.current_player_index + 1) % len(self.game.players)
        if self.game.rounds_played < self.game.max_rounds:
            self.update_game_display()
        else:
            self.end_game()

    def end_game(self):
        """ End the game and display winner """
        messagebox.showinfo("Game Over", "The game is over!")
        self.root.quit()

# Main application setup
if __name__ == "__main__":
    root = tk.Tk()
    app = CardGameApp(root)
    root.mainloop()
