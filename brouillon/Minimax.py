from utils import Utils
import time

class Minimax:
    def __init__(self):
        self.utils = Utils()
    def minimax(self, deep, maximiser):
        if self.utils.isCheck():
            return 1 if maximiser else -1
        
        if deep == 0 or self.utils.get_successor() == []:
            return 0
        
        if maximiser:
            max_eval = -float('inf')
            for successeur in self.utils.get_successor():
                eval = successeur.minimax(deep -1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for successeur in self.utils.get_successor():
                eval = successeur.minimax(deep -1, True)
                min_eval = min(min_eval, eval)
            return min_eval
        

        
start = time.time()
print("Temps d'execution time: ", time.time() - start)
        