import queue

board = [[" " for _ in range(3)] for _ in range(3)]
player = ["x","o"]

def Display(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

Display(board)
tag = int(input(print("choose 0 for x and 1 for o : ")))
row = int(input(print("Enter row : ")))
col = int(input(print("\nEnter col : ")))

while(True):
	if row > 2 or row < 0 or col > 2 or col < 0:
		print("invalud input")
		continue
	if not board[row][col] == " ":
		board[row][col] = player[tag]
		break
	else:
		print("invalid input")
		continue


IsWin(tag,board):
	for i in range(3):
		if board[i][0] == player[tag] and board[i][0] == board[i][1] == board[i][2]:
			print(f"player {tag} wins")
		if board[0][i] == player[tag] and board[0][i] == board[1][i] == board[2][i]:
			print(f"player {tag} wins")
	if board[0][0] == board[1][1] == board[2][2] :
		print(f"player {tag} wins")
	if board[0][2] == board[1][1] == board[2][0] :
		print(f"player {tag} wins")

isdraw(board)