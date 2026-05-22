import queue
import random

def PrintBoard(board):

    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_valid_move(board, row, col):

    return 0 <= row < 3 and \
           0 <= col < 3 and \
           board[row][col] == " "

def is_winner(board, player):

    # Rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_draw(board):

    for row in board:
        if " " in row:
            return False

    return True

def BfsMove(board, player):

    q = queue.Queue()

    q.put(board)

    while not q.empty():

        current_board = q.get()

        # Try winning move
        for row in range(3):
            for col in range(3):

                if current_board[row][col] == " ":

                    new_board = [r[:] for r in current_board]

                    new_board[row][col] = player

                    if is_winner(new_board, player):
                        return row, col

                    q.put(new_board)

    # Fallback move
    empty = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " " ]

    return random.choice(empty)

def Game():

    board = [[" " for _ in range(3)] for _ in range(3)]

    players = ["X", "O"]

    current_player = players[0]

    while True:

        PrintBoard(board)

        if current_player == "X":

            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))

        else:

            print("AI Move")

            row, col = BfsMove(board, current_player)

        if is_valid_move(board, row, col):

            board[row][col] = current_player

            if is_winner(board, current_player):

                PrintBoard(board)

                print(f"Player {current_player} wins!")

                break

            # Draw check
            if is_draw(board):

                PrintBoard(board)

                print("Draw!")

                break

            current_player = players[1] if current_player == players[0]  else players[0]

        else:

            print("Invalid move")

Game()