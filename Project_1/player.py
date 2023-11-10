import math
import random


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        valid_square = False
        move = None
        while not valid_square:
            square = input(f"{self.symbol}'s turn. Input move (0-9): ")
            try:
                move = int(square)
                if move not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return move


class RandomComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        move = random.choice(game.available_moves())
        return move


class SmartComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            move = random.choice(game.available_moves())
        else:
            move = self.minimax(game, self.symbol)['position']
        return move

    def minimax(self, state, current_player):
        max_player = self.symbol
        other_player = 'O' if current_player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        best = {'position': None, 'score': -math.inf} if current_player == max_player else {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, current_player)
            sim_score = self.minimax(state, other_player)

            state.undo_move(possible_move)

            sim_score['position'] = possible_move

            if (current_player == max_player and sim_score['score'] > best['score']) or (current_player != max_player and sim_score['score'] < best['score']):
                best = sim_score

        return best
