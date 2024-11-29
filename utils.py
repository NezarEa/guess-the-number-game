def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")
