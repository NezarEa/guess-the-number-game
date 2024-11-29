import random

class Game:
    def __init__(self, min_number=1, max_number=100, max_attempts=10):
        self.min_number = min_number
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.secret_number = random.randint(self.min_number, self.max_number)
        self.attempts = 0

    def make_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            return "Correct!"

    def is_game_over(self):
        return self.attempts >= self.max_attempts or self.secret_number == self.attempts
