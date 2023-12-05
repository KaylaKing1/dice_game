import random
import time
from dice_game import DiceGame
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()


def roll_dice():
    """Simulates the rolling of two dice."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def calculate_sum(die1, die2):
    """Calculates the sum of two dice."""
    return die1 + die2


def play_game():
    """Plays the dice game until a win or loss occurs."""
    wins = 0
    losses = 0

    while True:
        die1, die2 = roll_dice()
        total_sum = calculate_sum(die1, die2)

        print(f"You rolled: {die1} and {die2}")
        print(f"Sum of the dice: {total_sum}")

        if total_sum == 7 or total_sum == 11:
            print("Congratulations! You win!")
            wins += 1
            break
        elif total_sum == 3 or total_sum == 12:
            print("Sorry, you lose!")
            losses += 1
            break
        else:
            print("Rolling again in 2 seconds...\n")
            time.sleep(2)

    return wins, losses


if __name__ == "__main__":
    total_wins = 0
    total_losses = 0

    while True:
        wins, losses = play_game()
        total_wins += wins
        total_losses += losses

        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            break

    print(f"\nTotal Wins: {total_wins}")
    print(f"Total Losses: {total_losses}")
