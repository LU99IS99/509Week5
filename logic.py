from typing import List


def make_empty_board() -> List[List[str]]:
    """Creates a new empty 3x3 Tic-Tac-Toe board."""
    return [[' ' for _ in range(3)] for _ in range(3)]


def show_board(input_board: List[List[str]]):
    """Prints the Tic-Tac-Toe board."""
    for row in input_board:
        print(" | ".join(row))
        print("-" * 9)


def input_move(input_board: List[List[str]]):
    """Prompts the user for a move and validates the input."""
    while True:  # Keep asking for input until a valid move is made
        try:
            row = int(input("Input row index (0, 1, 2): "))
            column = int(input("Input column index (0, 1, 2): "))
            if row < 0 or row > 2 or column < 0 or column > 2:
                print('Input invalid, should be >= 0 and <= 2')
            elif input_board[row][column] != ' ':
                print('Input invalid, position already taken')
            else:
                return row, column  # Valid move
        except ValueError:
            print('Input invalid, not an integer')


def next_player(old: str):
    """Switches the player turn."""
    return 'O' if old == 'X' else 'X'


def judge_winner(input_board: List[List[str]]) -> str:
    """Determines if there is a winner or a draw."""
    for i in range(3):
        if input_board[i][0] == input_board[i][1] == input_board[i][2] != ' ':
            return input_board[i][0]
    for i in range(3):
        if input_board[0][i] == input_board[1][i] == input_board[2][i] != ' ':
            return input_board[0][i]
    if (input_board[0][0] == input_board[1][1] == input_board[2][2] != ' ' or
            input_board[2][0] == input_board[1][1] == input_board[0][2] != ' '):
        return input_board[1][1]
    if all(cell != ' ' for row in input_board for cell in row):
        return 'Draw'
    return ''


def play_game():
    """Starts and manages the Tic-Tac-Toe game."""
    board = make_empty_board()
    winner = ''
    current_player = 'X'
    show_board(board)
    while winner == '':
        print('Next turn for:', current_player)
        row, column = input_move(board)
        board[row][column] = current_player
        show_board(board)
        winner = judge_winner(board)
        if winner:
            break  # Exit the loop if we have a winner or a draw
        current_player = next_player(current_player)

    # Announce the result
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"Player {winner} wins!")


if __name__ == '__main__':
    play_game()
