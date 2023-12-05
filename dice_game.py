import tkinter as tk
import random
import time


class DiceGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Dice Game")

        self.wins = 0
        self.losses = 0

        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack(pady=10)

        self.button_roll = tk.Button(master, text="Roll Dice", command=self.play_game)
        self.button_roll.pack(pady=10)

        self.button_exit = tk.Button(master, text="Exit", command=self.exit_game)
        self.button_exit.pack(pady=10)

    def roll_dice(self):
        """Simulates the rolling of two dice."""
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1, die2

    def draw_dice(self, die_value, x, y):
        """Draws a representation of a die face on the canvas."""
        self.canvas.create_rectangle(x, y, x + 40, y + 40, fill="white", outline="black")
        if die_value % 2 == 1:  # Draw center dot for odd values
            self.canvas.create_oval(x + 18, y + 18, x + 22, y + 22, fill="black")

        if die_value > 1:  # Draw top-left and bottom-right dots for values greater than 1
            self.canvas.create_oval(x + 8, y + 8, x + 12, y + 12, fill="black")
            self.canvas.create_oval(x + 28, y + 28, x + 32, y + 32, fill="black")

        if die_value > 3:  # Draw top-right and bottom-left dots for values greater than 3
            self.canvas.create_oval(x + 28, y + 8, x + 32, y + 12, fill="black")
            self.canvas.create_oval(x + 8, y + 28, x + 12, y + 32, fill="black")

        if die_value == 6:  # Draw middle-left and middle-right dots for value 6
            self.canvas.create_oval(x + 8, y + 18, x + 12, y + 22, fill="black")
            self.canvas.create_oval(x + 28, y + 18, x + 32, y + 22, fill="black")

    def show_dice(self, die1, die2):
        """Shows the dice faces on the canvas."""
        frames = 10  # Number of frames for the rolling effect

        for _ in range(frames):
            self.master.update()
            time.sleep(0.1)

            self.canvas.delete("all")  # Clear previous drawings
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            self.draw_dice(roll1, 20, 20)
            self.draw_dice(roll2, 70, 20)

        # Show the final result
        self.canvas.delete("all")  # Clear previous drawings
        self.draw_dice(die1, 20, 20)
        self.draw_dice(die2, 70, 20)

    def calculate_sum(self, die1, die2):
        """Calculates the sum of two dice."""
        return die1 + die2

    def play_game(self):
        """Plays the dice game until a win or loss occurs."""
        while True:
            die1, die2 = self.roll_dice()
            total_sum = self.calculate_sum(die1, die2)

            self.show_dice(die1, die2)

            result_text = f"Sum of the dice: {total_sum}\n"

            if total_sum == 7 or total_sum == 11:
                self.wins += 1
                result_text += "You Win!"
                self.canvas.create_text(100, 160, text=result_text, font=("Arial", 12), anchor="center")
                self.master.update()
                time.sleep(1)
                break
            elif total_sum == 2 or total_sum == 3 or total_sum == 12:
                result_text += "Sorry, you lose!"
                self.losses += 1
                self.canvas.create_text(100, 160, text=result_text, font=("Arial", 12), anchor="center")
                self.master.update()
                time.sleep(1)
                break

            # Update the result text
            self.canvas.create_text(100, 160, text=result_text, font=("Arial", 12), anchor="center")
            self.master.update()
            time.sleep(1)  # Optional delay between rolls

    def exit_game(self):
        """Exits the game and displays the total wins and losses."""
        self.master.destroy()
        self.display_stats()

    def display_stats(self):
        """Displays the total wins and losses."""
        stats_text = f"Total Wins: {self.wins}\nTotal Losses: {self.losses}"
        stats_window = tk.Tk()
        stats_window.title("Game Statistics")
        label_stats = tk.Label(stats_window, text=stats_text)
        label_stats.pack(pady=10)
        stats_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()
