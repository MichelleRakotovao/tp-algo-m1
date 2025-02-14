import math
from utils.Bits import Bits

class AiModule:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth

    def evaluate(self, board, is_maximizing_player):
        # Évaluation basée sur le nombre de pièces et alignements
        player_pieces = Bits.count(board.myPieces)
        opponent_pieces = Bits.count(board.opponentPieces)

        score = player_pieces - opponent_pieces

        if Bits.isCheck(board.myPieces):
            score += 100
        if Bits.isCheck(board.opponentPieces):
            score -= 100

        return score if is_maximizing_player else -score

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or Bits.isCheck(board.myPieces) or Bits.isCheck(board.opponentPieces):
            return self.evaluate(board, maximizing_player)

        if maximizing_player:
            max_eval = -math.inf
            for move in board.get_all_possible_moves(True):
                new_board = board.simulate_move(move)
                eval = self.minimax(new_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in board.get_all_possible_moves(False):
                new_board = board.simulate_move(move)
                eval = self.minimax(new_board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self, board):
        best_move = None
        best_value = -math.inf
        for move in board.get_all_possible_moves(True):
            new_board = board.simulate_move(move)
            move_value = self.minimax(new_board, self.max_depth - 1, -math.inf, math.inf, False)
            if move_value > best_value:
                best_value = move_value
                best_move = move
        return best_move
