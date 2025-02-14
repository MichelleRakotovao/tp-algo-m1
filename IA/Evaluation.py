from utils.Bits import Bits
class Evaluation:


    
    @staticmethod
    def evaluate(board):
        score = 0

        # 1. Compter les pièces
        my_count = bin(board.myPieces & Bits.on_border).count('1')
        opponent_count = bin(board.opponentPieces & Bits.on_border).count('1')
        score += (my_count - opponent_count) * 10

        # 2. Contrôle du centre (1,1)
        center_bit = Bits.at(1, 1)
        if board.myPieces & center_bit:
            score += 5
        if board.opponentPieces & center_bit:
            score -= 5

        # 3. Vérifier alignements gagnants
        if Bits.isCheck(board.myPieces):
            score += 100
        if Bits.isCheck(board.opponentPieces):
            score -= 100

        return score

    @staticmethod
    def is_terminal(board):
        # Vérifier si un joueur a gagné
        if Bits.isCheck(board.myPieces) or Bits.isCheck(board.opponentPieces):
            return True
        # Vérifier si toutes les cases sont occupées
        full = (board.myPieces | board.opponentPieces) & Bits.on_border
        if full == Bits.on_border:
            return True
        return False

    @staticmethod
    def winner(board):
        if Bits.isCheck(board.myPieces):
            return "Mon joueur"
        elif Bits.isCheck(board.opponentPieces):
            return "Adversaire"
        return None
