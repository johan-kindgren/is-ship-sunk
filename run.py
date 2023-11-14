import random

def create_board(size):
    return [["O" for _ in range(size)] for _ in range(size)]

def place_ships(board, num_ships):
    size = len(board)
    for _ in range(num_ships):
        ship_placed = False
        while not ship_placed:
            row, col = random.randint(0, size - 1), random.randint(0, size - 1)
            if board[row][col] == "O":
                board[row][col] = "S"
                ship_placed = True

def print_board(board, reveal=False):
    display_board = []
    for row in board:
        display_row = []
        for cell in row:
            if cell == "O":
                display_row.append('.')
            elif cell == "S":
                display_row.append('S' if reveal else '.')
            elif cell == "H":
                display_row.append('V')
            elif cell == "M":
                display_row.append('X')
        display_board.append(display_row)
    for row in display_board:
        print(" ".join(row))

def get_shot():
    while True:
        try:
            row = int(input("Enter row to hit: "))
            col = int(input("Enter column to hit: "))
            return row, col
        except ValueError:
            print("Please enter valid row and column numbers.")

def make_move(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board):
        if board[row][col] == "S":
            board[row][col] = "H"  # H for hit (will display as V)
            print("Hit!")
            return True
        elif board[row][col] == "O":
            board[row][col] = "M"  # M for miss (will display as X)
            print("Miss.")
    else:
        print("Out of bounds.")
    return False

def is_game_over(board):
    return not any("S" in row for row in board)

# Game setup
board_size = 5
num_ships = 3

player_board = create_board(board_size)
computer_board = create_board(board_size)

place_ships(player_board, num_ships)
place_ships(computer_board, num_ships)

player_name = input("Enter your name: ")

# Game loop
game_over = False
while not game_over:
    print(f"\n{player_name}'s turn:")
    print_board(player_board, reveal=True)
    row, col = get_shot()
    make_move(computer_board, row, col)

    if is_game_over(computer_board):
        print(f"Congratulations, {player_name}! You have won the game!")
        break

    print("\nComputer's turn:")
    row, col = random.randint(0, board_size - 1), random.randint(0, board_size - 1)
    make_move(player_board, row, col)

    if is_game_over(player_board):
        print("Sorry, the computer has won the game.")
        break

    print("\nCurrent Board:")
    print_board(player_board, reveal=True)
