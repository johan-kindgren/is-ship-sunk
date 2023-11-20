import random

class BattleshipGame:
    def __init__(self, size, num_ships):
        self.board_size = size
        self.num_ships = num_ships
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.place_ships(self.player_board)
        self.place_ships(self.computer_board)

    def create_board(self):
        # Creates a game board as a list of lists filled with 'O'
        return [["O" for _ in range(self.board_size)] for _ in range(self.board_size)]

    def place_ships(self, board):
        # Randomly places ships (marked as 'S') on the board
        for _ in range(self.num_ships):
            ship_placed = False
            while not ship_placed:
                row, col = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
                if board[row][col] == "O":
                    board[row][col] = "S"
                    ship_placed = True

    def print_board(self, board, reveal=False):
        # Displays the game board to the player
        for row in board:
            display_row = []
            for cell in row:
                if cell == "O":
                    display_row.append('.')
                elif cell == "S":
                    display_row.append('S' if reveal else '.')
                elif cell == "H":
                    display_row.append('V')  # 'V' for hit
                elif cell == "M":
                    display_row.append('X')  # 'X' for miss
            print(" ".join(display_row))

    def get_shot(self):
        # Gets player's shot location with input validation
        while True:
            try:
                row = int(input("Enter row to hit (0-{}): ".format(self.board_size - 1)))
                col = int(input("Enter column to hit (0-{}): ".format(self.board_size - 1)))
                if 0 <= row < self.board_size and 0 <= col < self.board_size:
                    return row, col
                else:
                    print("Input out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    def make_move(self, board, row, col):
        # Processes a move and updates the board
        if board[row][col] == "S":
            board[row][col] = "H"  # Hit
            print("Hit!")
            return True
        elif board[row][col] == "O":
            board[row][col] = "M"  # Miss
            print("Miss.")
        else:
            print("Already hit this spot.")
        return False

    def is_game_over(self, board):
        # Checks if the game is over (no ships left)
        return not any("S" in row for row in board)

    def play(self):
        # Main game loop
        player_name = input("Enter your name: ")
        while True:
            print(f"\n{player_name}'s turn:")
            self.print_board(self.player_board, reveal=True)
            row, col = self.get_shot()
            self.make_move(self.computer_board, row, col)

            if self.is_game_over(self.computer_board):
                print(f"Congratulations, {player_name}! You have won the game!")
                break

            print("\nComputer's turn:")
            row, col = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            self.make_move(self.player_board, row, col)

            if self.is_game_over(self.player_board):
                print("Sorry, the computer has won the game.")
                break

            print("\nCurrent Board:")
            self.print_board(self.player_board, reveal=True)

# Game setup
game = BattleshipGame(5, 3)
game.play()
