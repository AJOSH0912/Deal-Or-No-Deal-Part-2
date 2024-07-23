import random
import pygame

class Briefcase:
    def __init__(self, number, value):
        self.number = number
        self.value = value
        self.is_open = False

class Game:
    def __init__(self, num_players=1, num_briefcases=26, game_mode="classic", difficulty="medium"):
        self.num_players = num_players
        self.num_briefcases = num_briefcases
        self.game_mode = game_mode
        self.difficulty = difficulty
        self.briefcases = [Briefcase(i+1, value) for i, value in enumerate(self.generate_briefcase_values())]
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.current_player = 0
        self.open_briefcases = []
        self.banker_personality = random.choice(["aggressive", "cautious", "friendly"])
