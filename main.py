from game import Game
from player import Player
from utils import get_player_guess

def main():
    print("Welcome to 'Guess the Number'!")
    name = input("Please enter your name: ")
    player = Player(name)

    game = Game()
    print(f"Hello, {player.name}! Try to guess the number between {game.min_number} and {game.max_number}. You have {game.max_attempts} attempts.")

    while not game.is_game_over():
        guess = get_player_guess()
        result = game.make_guess(guess)
        print(result)

        if result == "Correct!":
            player.increment_score()
            print(f"Congratulations, {player.name}! You've guessed the number in {game.attempts} attempts.")
            print(f"Your score: {player.get_score()}")
            break

        if game.attempts >= game.max_attempts:
            print("Sorry, you've used all your attempts. Better luck next time!")
            print(f"The secret number was {game.secret_number}.")

if __name__ == "__main__":
    main()
