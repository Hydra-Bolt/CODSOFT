import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

# Constants
PLAYER_X = 'X'
PLAYER_O = 'O'

class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
        self.last_move = None  # Added to keep track of the last move

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def make_move(self, square, symbol):
        if self.board[square] == ' ':
            self.board[square] = symbol
            self.last_move = square  # Update the last move
            if self.is_winner(square, symbol):
                self.current_winner = symbol
            return True
        return False

    def undo_move(self, square):
        self.board[square] = ' '
        self.current_winner = None

    def is_winner(self, square, symbol):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == symbol for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == symbol for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == symbol for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == symbol for s in diagonal2]):
                return True

        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


def play_game(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    current_player = PLAYER_X
    while game.empty_squares():
        if current_player == PLAYER_O:
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, current_player):
            if print_game:
                print(current_player + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(current_player + ' wins!')
                return current_player

            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = SmartComputerPlayer(PLAYER_X)
    o_player = HumanPlayer(PLAYER_O)
    tic_tac_toe_game = TicTacToe()
    play_game(tic_tac_toe_game, x_player, o_player, print_game=True)
