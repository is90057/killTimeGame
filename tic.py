board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"

def print_board():
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))

def get_move():
    move = input("Player {}: Enter your move (1-9): ".format(player))
    while move not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(move) - 1] != " ":
        move = input("Invalid move. Player {}: Enter your move (1-9): ".format(player))
    return int(move) - 1

def make_move(move):
    global player
    board[move] = player
    print_board()
    if player == "X":
        player = "O"
    else:
        player = "X"

def check_winner():
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
        elif board[i*3] == board[i*3+1] == board[i*3+2] != " ":
            return board[i*3]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    elif board[2] == board[4] == board[6] != " ":
        return board[2]
    return None

def main():
    print_board()
    while not check_winner() and " " in board:
        move = get_move()
        make_move(move)
    winner = check_winner()
    if winner:
        print("Player {} wins!".format(winner))
    else:
        print("Tie game.")

if __name__ == "__main__":
    main()
