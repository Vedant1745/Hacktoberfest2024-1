class ConnectTheDots:
    def __init__(self, size=5):
        self.size = size
        self.horizontal = [[' ' for _ in range(size - 1)] for _ in range(size)]
        self.vertical = [[' ' for _ in range(size)] for _ in range(size - 1)]
        self.boxes = [[' ' for _ in range(size - 1)] for _ in range(size - 1)]
        self.current_player = 1

    def print_board(self):
        for i in range(self.size):
            # Print horizontal connections
            for j in range(self.size):
                if j == 0:
                    print(" ", end="")
                else:
                    print("|", end="")
                print(" " + self.horizontal[i][j] + " ", end="")
            print()

            # Print vertical connections for boxes
            if i < self.size - 1:
                for j in range(self.size):
                    print(" " + self.vertical[i][j] + " ", end="")
                print()

        print()

    def make_move(self, x, y, orientation):
        if orientation == 'H' and y < self.size - 1 and self.horizontal[x][y] == ' ':
            self.horizontal[x][y] = '-' if self.current_player == 1 else '='
            return True
        elif orientation == 'V' and x < self.size - 1 and self.vertical[x][y] == ' ':
            self.vertical[x][y] = '|' if self.current_player == 1 else '/'
            return True
        return False

    def check_boxes(self):
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if (self.horizontal[i][j] != ' ' and self.horizontal[i + 1][j] != ' ' and
                        self.vertical[i][j] != ' ' and self.vertical[i][j + 1] != ' '):
                    self.boxes[i][j] = 'X' if self.current_player == 1 else 'O'

    def is_game_over(self):
        return all(cell != ' ' for row in self.boxes for cell in row)

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def play(self):
        while True:
            self.print_board()
            print(f"Player {self.current_player}, enter your move (row, column, orientation [H/V]): ")
            try:
                x, y, orientation = input().split()
                x, y = int(x), int(y)

                if self.make_move(x, y, orientation):
                    self.check_boxes()
                    if self.is_game_over():
                        self.print_board()
                        print(f"Game over! Player {self.current_player} wins!")
                        break
                    self.switch_player()
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates and orientation.")

if __name__ == "__main__":
    game = ConnectTheDots()
    game.play()
