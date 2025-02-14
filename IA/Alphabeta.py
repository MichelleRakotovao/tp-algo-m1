from utils import Utils
import time

class Alphabeta:
    def __init__(self, border_size):
        self.utils = Utils(border_size)  # Initialiser Utils avec la taille du plateau
    
    def alphabeta(self, board, deep, maximiser, alpha, beta, player):
        # Vérifier si une condition de fin de jeu est atteinte
        if self.utils.isCheck(board):
            return 1 if maximiser else -1
        
        if deep == 0 or not self.utils.get_successor(board, player):
            return 0  # Retour de l'évaluation (match nul ou état terminal)

        if maximiser:
            max_eval = -float('inf')
            for successeur in self.utils.get_successor(board, player):
                eval = self.alphabeta(successeur, deep - 1, False, alpha, beta, player)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Coup de prunage
            return max_eval
        else:
            min_eval = float('inf')
            for successeur in self.utils.get_successor(board, player):
                eval = self.alphabeta(successeur, deep - 1, True, alpha, beta, player)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  
            return min_eval
        
start = time.time()
print("Temps d'execution: ", time.time() - start)