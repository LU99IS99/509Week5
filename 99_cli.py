def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def get_player_move(player, board):
    while True:
        try:
            row = int(input(f"{player}'s turn. Enter the row number (0-2): "))
            col = int(input(f"{player}'s turn. Enter the column number (0-2): "))
            if board[row][col] == " ":
                return row, col
            else:
                print("That spot is taken. Choose another.")
        except (IndexError, ValueError):
            print("Invalid input. Try again.")

def check_win(board):
    lines = [board[0], board[1], board[2],
             [board[0][0], board[1][0], board[2][0]],
             [board[0][1], board[1][1], board[2][1]],
             [board[0][2], board[1][2], board[2][2]],
             [board[0][0], board[1][1], board[2][2]],
             [board[2][0], board[1][1], board[0][2]]]
    for line in lines:
        if line[0] == line[1] == line[2] != " ":
            return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = create_board()
    current_player = "X"
    while True:
        print_board(board)
        row, col = get_player_move(current_player, board)
        board[row][col] = current_player
        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()

