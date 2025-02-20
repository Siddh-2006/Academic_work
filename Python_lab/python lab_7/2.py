import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.total_rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def find_winner(self, user_choice):
        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            self.user_wins += 1
            return "User wins"
        else:
            self.computer_wins += 1
            return "Computer wins"

    def play_round(self, user_choice):
        self.current_round += 1
        result = self.find_winner(user_choice)
        print(f"Round {self.current_round}: {result}")

    def check_game_winner(self):
        if self.current_round >= self.total_rounds:
            if self.user_wins > self.computer_wins:
                return "User is the overall winner!"
            elif self.user_wins < self.computer_wins:
                return "Computer is the overall winner!"
            else:
                return "The game is a tie!"
        else:
            return "The game is still ongoing."

# Example usage:
game = Rock_paper_scissors(rounds=3)

game.play_round('rock')
game.play_round('paper')
game.play_round('scissors')

print(game.check_game_winner())
