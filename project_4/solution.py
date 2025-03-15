game_board = [[1,2,3], [4,5,6], [7,8,9]]
game_on = True

def print_gameboard():
    for row in game_board:
        print(row)

def check_winner(board, mark):
    for row in board:
        if all([cell == mark for cell, mark in zip(row, [mark]*3)]):
            return True
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

current_player = "X"
turns = 0

while True:
    print("\nCurrent Game Board:")
    print("\n".join([str(row) for row in game_board]))
    guess = int(input(f"Player {1 if gameon else 2}, choose your spot: "))

    valid_move = False
    for row in game_board:
        if guess in row:
            row[row.index(guess)] = "X" if gameon else "O"
            valid_move = True
            break

    if not valid_move:
        print("Invalid spot. Try again.")
        continue

    # Check for a win
    if check_winner(game_board, "X" if gameon else "O"):
        print(f"Player {1 if gameon else 2} wins!")
        print_gameboard()
        break

    gameon = not gameon
