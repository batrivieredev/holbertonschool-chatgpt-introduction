#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.safe_cells = width * height - mines  # Total number of non-mine cells

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # If the cell is a mine, the player loses
        if (y * self.width + x) in self.mines:
            return False

        # If the cell is already revealed, return
        if self.revealed[y][x]:
            return True

        # Reveal the current cell
        self.revealed[y][x] = True
        self.safe_cells -= 1

        # If no adjacent mines, reveal neighboring cells
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)

        return True

    def play(self):
        while True:
            self.print_board()

            # Check if the player has revealed all safe cells
            if self.safe_cells == 0:
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break

            # Get input from the player
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Invalid coordinates. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter valid integers.")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break


if __name__ == "__main__":
    game = Minesweeper(width=10, height=10, mines=10)  # You can adjust width, height, and mines here
    game.play()

