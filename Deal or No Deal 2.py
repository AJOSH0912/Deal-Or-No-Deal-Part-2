import random

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

    def generate_briefcase_values(self):
        values = [1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        random.shuffle(values)
        return values[:self.num_briefcases]

    def calculate_banker_offer(self):
        # Placeholder for more complex banker offer calculation
        remaining_values = [b.value for b in self.briefcases if not b.is_open]
        average_value = sum(remaining_values) / len(remaining_values)
        offer = average_value * 0.8  # Adjust multiplier based on banker personality
        return offer

    def play(self):
        # Assign briefcases to players
        for i, player in enumerate(self.players):
            player.briefcase = self.briefcases[i]

        game_over = False
        while not game_over:
            current_player = self.players[self.current_player]
            print(f"It's {current_player.name}'s turn.")

            # Player chooses a briefcase to open
            while True:
                try:
                    choice = int(input("Choose a briefcase to open: "))
                    if choice in self.open_briefcases or choice > self.num_briefcases or choice < 1:
                        print("Invalid choice. Try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            chosen_briefcase = self.briefcases[choice - 1]
            chosen_briefcase.is_open = True
            self.open_briefcases.append(choice)
            print(f"Briefcase {choice} contains: ${chosen_briefcase.value}")

            # Banker offer after every 5 opened briefcases
            if len(self.open_briefcases) % 5 == 0:
                offer = self.calculate_banker_offer()
                print(f"Banker's offer: ${offer}")
                deal = input("Deal or No Deal (d/n)? ")
                if deal.lower() == "d":
                    print(f"{current_player.name} accepted the offer and won ${offer}")
                    return

            # Check for game over (only one briefcase left)
            if len(self.briefcases) - len(self.open_briefcases) == 1:
                print(f"{current_player.name} wins: ${current_player.briefcase.value}")
                game_over = True

            self.current_player = (self.current_player + 1) % self.num_players

class Player:
    def __init__(self, name):
        self.name = name
        self.briefcase = None

# Game setup and initialization
num_players = int(input("Enter number of players: "))
game = Game(num_players)
game.play()