class Utils:
    def __init__(self, border_size):
        self.border_size = border_size  # Taille du plateau, 3x3 pour Fanorona Telo
    
    def isCheck(self, board):
        # Vérification d'alignement horizontal, vertical et croisé sur le BitBoard
        # alignement horizontal
        for i in range(self.border_size - 2):
            if board & (board >> (i + 1)) & (board >> (i + 2)):
                return True

        # alignement vertical
        for i in range(self.border_size - 2):
            if board & (board >> (i + self.border_size)) & (board >> (i + 2 * self.border_size)):
                return True

        # alignement croisé
        if board & (board >> (self.border_size + 1)) & (board >> (2 * self.border_size + 2)):
            return True
        
        if board & (board >> (self.border_size - 1)) & (board >> (2 * self.border_size - 2)):
            return True

        return False

    def is_terminal(self, board):
        # Vérifie si un joueur a gagné ou si le jeu est terminé
        return self.isCheck(board)
    
    def get_successor(self, board, player):
        successors = []
        for move in self.move_possible(board, player):
            new_board = self.make_move(board, player, move)
            successors.append(new_board)
        return successors

    def move_possible(self, board, player):
        possibles_moves = []
        for i in range(self.border_size * self.border_size):
            # Vérifie si la case i est libre pour un mouvement du joueur
            if not (board & (1 << i)):  # Si la case i est libre
                possibles_moves.append(i)
        return possibles_moves

    def make_move(self, board, player, move):
        # Applique le mouvement 
        new_board = board
        new_board |= (1 << move)  
        return new_board
    
    def isCheck(self, board):
        # Vérification d'alignement horizontal, vertical et croisé sur le BitBoard
        # alignement horizontal
        for i in range(self.border_size - 2):
            if board & (board >> (i + 1)) & (board >> (i + 2)):
                return True

        # alignement vertical
        for i in range(self.border_size - 2):
            if board & (board >> (i + self.border_size)) & (board >> (i + 2 * self.border_size)):
                return True

        # alignement croisé
        if board & (board >> (self.border_size + 1)) & (board >> (2 * self.border_size + 2)):
            return True
        
        if board & (board >> (self.border_size - 1)) & (board >> (2 * self.border_size - 2)):
            return True

        return False
