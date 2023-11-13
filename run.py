def create_board(size):
    return [["O" for _ in range(size)] for _ in range(size)]
    board_size = 10 
    game_board = create_board(board_size)

def print_board(board):
 
 
        
   for row in board:
        print(" ".join(row))
        print_board(game_board)
import random

def place_ships(board, num_ships):
    for _ in range(num_ships):
        x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        board[x][y] = "S"  # "S" denotes a ship
        place_ships(game_board, 5)
def get_user_guess():
    while True:
        try:
            x, y = map(int, input("Enter your guess (row column): ").split())
            return x, y
        except ValueError:
            print("Invalid input. Please enter numbers.")
            user_guess = get_user_guess(
 def check_guess(board, guess):
    x, y = guess
    if x < 0 or y < 0 or x >= len(board) or y >= len(board):
        return "Off-grid!"
    if board[x][y] == "S":
        board[x][y] = "H"  # "H" for hit
        return "Hit!"
    else:
        board[x][y] = "M"  # "M" for miss
        return "Miss!"           
        result = check_guess(game_board, user_guess)
print(result)

def main():
    board_size = int(input("Enter board size: "))
    num_ships = int(input("Enter number of ships: "))

    game_board = create_board(board_size)
    place_ships(game_board, num_ships)

    while True:
        print_board(game_board)
        guess = get_user_guess()
        result = check_guess(game_board, guess)
        print(result)
        if result == "Hit!":
            num_ships -= 1
            if num_ships == 0:
                print("All ships have been destroyed! You win!")
                break

if __name__ == "__main__":
    main()
    