def print_game_status(game):
    print(f"Game Status: {game.rounds_played} rounds played")
    for player in game.players:
        print(f"{player.name}: {len(player.hand)} cards remaining")
