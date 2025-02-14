from utils.Bits import Bits
class BitBoard :
    cols = 3
    rows = 3

    def __init__(self , goes_first = True):
        self.evaluation = 0
        self.initial_position(goes_first)
        self.pieces_placed = 0
        self.oppenBorder = 0

    def initial_position(self , goes_first=True):
        self.myPieces = 0 
        self.opponentPieces = 0

        if goes_first:
         self.myPieces |= Bits.My_tourn
        else:
            self.opponentPieces |= Bits.My_tourn

    def print_board(self):
        Bits.affichage_fanorona3(self.myPieces,self.opponentPieces)

    #def make_move(self , row , col ):
    #    if not self.is_valid_move(col):
    #       raise ValueError("Mouvement invalide")
        

    def place_piece(self, row, col, is_my_piece=True):
        bit = Bits.at(row, col)
        if (self.myPieces | self.opponentPieces) & bit:
            raise ValueError("Case déjà occupée")

        if (self.myPieces & Bits.My_tourn) :
            self.myPieces |= bit
        else:
            self.opponentPieces |= bit

        self.pieces_placed += 1
        self.change_player()

    def can_move_pieces(self):
        return self.pieces_placed >= 6
    
    def make_move(self, start_row, start_col, end_row, end_col):
        if not self.can_move_pieces():
            raise ValueError("Toutes les pièces doivent être placées avant de pouvoir bouger")

 
    
        start_bit = Bits.at(start_row, start_col)
        end_bit = Bits.at(end_row, end_col)
        
        # Vérification de la validité du mouvement
        if not self.is_valid_move(start_bit, end_bit):
            raise ValueError("Mouvement invalide")

                # Vérification des mouvements adjacents ou dans une direction spécifique (diagonale, etc.)
        if not self.is_adjacent(start_row, start_col, end_row, end_col):
            raise ValueError("Le mouvement n'est pas adjacent ou valide selon la règle")


        # Déplacer la pièce
        if self.myPieces & start_bit:
            self.myPieces &= ~start_bit
            self.myPieces |= end_bit
        elif self.opponentPieces & start_bit:
            self.opponentPieces &= ~start_bit
            self.opponentPieces |= end_bit

        # Capture de l'adversaire si possible
        #if self.opponentPieces & end_bit:
        #    self.opponentPieces &= ~end_bit

        # Changement de joueur
        self.change_player()

    def is_valid_move(self, start_bit, end_bit):
        if not (self.myPieces & start_bit) and not (self.opponentPieces & start_bit):
            return False

        if (self.myPieces | self.opponentPieces) & end_bit:
            return False

        return True

    def change_player(self):
        self.myPieces ^= Bits.My_tourn
        self.opponentPieces ^= Bits.My_tourn

    def check_victory(self):
        if Bits.count(self.opponentPieces) == 0:
            return "Joueur 1 gagne!"
        elif Bits.count(self.myPieces) == 0:
            return "Joueur 2 gagne!"
        return "Partie en cours"
    

    #def get_successors(self , position_i , position_J):
        

    def is_adjacent(self , i1, j1, i2, j2):
        di = i2 - i1
        dj = j2 - j1

        # Vérification des déplacements adjacents horizontaux et verticaux
        if (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            return True
        
        # Vérification des déplacements diagonaux
        if (di, dj) in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
            if (i1 == j1) or (i1 == -j1):
                if (i1 == j1 and i2 == j2) or (i1 == -j1 and i2 == -j2):
                    return True

        return False

    def get_successors(self, i, j):
        successors = []
        
        # Les déplacements possibles (horizontaux, verticaux et diagonaux)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            # Vérifier que la nouvelle position est valide (dans les limites du plateau)
            if 0 <= ni < self.rows and 0 <= nj < self.cols:
                bit = Bits.at(ni, nj)
                
                # Vérification que la case cible est libre
                if not (self.myPieces & bit or self.opponentPieces & bit):
                    successors.append((ni, nj))  # Ajouter la case comme successeur

        return successors


            

        



    #def reset_game(self):
    #    self.initial_position(True)
    #    self.pieces_placed = 0

    #def change_Player(self):

    #def check_victory(self, pieces):

    #def reset_game(self):