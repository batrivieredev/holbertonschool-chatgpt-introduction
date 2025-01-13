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
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.safe_cells = width * height - mines  # Nombre total de cases sûres

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
        # Si la cellule est une mine
        if (y * self.width + x) in self.mines:
            return False  # Défaite

        # Si la cellule est déjà révélée
        if self.revealed[y][x]:
            return True

        # Révéler la cellule actuelle
        self.revealed[y][x] = True
        self.safe_cells -= 1

        # Si la cellule n'a pas de mines autour, révéler les voisins
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

            # Vérifier si le joueur a gagné
            if self.safe_cells == 0:
                self.print_board(reveal=True)
                print("Félicitations ! Vous avez gagné.")
                break

            # Lecture des coordonnées de l'utilisateur
            try:
                x = int(input("Entrez la coordonnée x : "))
                y = int(input("Entrez la coordonnée y : "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordonnées hors limites. Réessayez.")
                    continue

                # Révéler la cellule et vérifier si c'est une mine
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over ! Vous avez touché une mine.")
                    break
            except ValueError:
                print("Entrée invalide. Veuillez entrer des nombres uniquement.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
