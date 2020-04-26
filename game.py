def main():
    play_game = True
    while play_game:
        board = create_board()
        show_board(board)
        player = "X"
        while game_is_not_finished(board):
            player = make_move(player, board)
            show_board(board)
        if tie(board):
            print('Tie!')
        else:
            winner = changePlayer(player)
            print('Congratulations, {}! You are won the game!'.format(winner))
        play_game = ask_contineuse()


def ask_contineuse():
    print('Play again? Type y to play again')
    answer = input()
    if answer=='y':
        print('New game started')
        return True
    else:
        print('Bye!')
        return False


def create_board():
    board = {}
    for p in range(1,10):
        p = str(p)
        board[p] = p
    return board


def show_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[str(1 + i * 3)], "|", board[str(2 + i * 3)], "|", board[str(3 + i * 3)], "|")
        print("-------------")


def make_move(player, board):
    print("Where to put {}?".format(player))
    position = input()
    if position_is_valid(position, board):
        updateBoard(board, position, player)
        nextplayer = changePlayer(player)
    else:
        print('Choose number from 1 to 9')
        nextplayer = player
    return nextplayer


def game_is_not_finished(board):
    win_coord = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))
    for each in win_coord:
        if board[str(each[0])] == board[str(each[1])] == board[str(each[2])]:
            print('3 in line!')
            return False
    if tie(board):
        return False
    return True


def tie(board):
    n_empty_spots = 0
    for p in range(1, 10):
        if position_is_int(board[str(p)]):
            n_empty_spots += 1
    if n_empty_spots == 0:
        return True
    return False


def changePlayer(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


def position_is_valid(position: str, board: dict) -> bool:
    if position_is_int(position):
        if 1 <= int(position) <= 9:
            if position_is_int(board[position]):
                return True
            else:
                print('The position is occupied! Choose another position.')
                return False
        return False
    else:
        return False


def position_is_int(position):
    try:
        int(position)
        return True
    except ValueError:
        return False


def updateBoard(board, position, player):
    board[position] = player


if __name__ == '__main__':
    main()
