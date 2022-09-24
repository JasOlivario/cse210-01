"Author: Joshue Sam Olivario"
"Game: Tic-Tac-Toe"

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_draw(board)):
        print_board(board)
        player_input(player, board)
        player = next_player(player)
    print_board(board)
    winner = winning_player(board, player)
    if has_winner(board):
        print (f"Congratulations! {winner} won!")
    elif is_draw(board):
        print ("Draw, Thanks for playing!")

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def print_board(board):
    print ()
    print (f"{board[0]}|{board[1]}|{board[2]}")
    print ("-+-+-")
    print (f"{board[3]}|{board[4]}|{board[5]}")
    print ("-+-+-")
    print (f"{board[6]}|{board[7]}|{board[8]}")
    print ()

def is_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[6] == board[4] == board[2])

def winning_player(board, player):
    if has_winner(board):
        if player == "o":
            return "x"
        elif player == "x":
            return "o"

def next_player(turn):
    if turn == "" or turn == "o":
        return "x"
    elif turn == "x":
        return "o"

def player_input(player, board):
    square = int(input(f"{player}'s turn. Choose from 1-9: "))
    board[square - 1] = player

if __name__ == "__main__":
    main()
