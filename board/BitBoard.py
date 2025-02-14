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

    def place_piece(self, row, col, is_my_piece=True):
        print(self.pieces_placed)
        if(self.pieces_placed>5):
            print("deplace les pieces en utilisant make_move()")
            return
        bit = Bits.at(row, col)
        if (self.myPieces | self.opponentPieces) & bit:
            raise ValueError("Case déjà occupée")

        if (self.myPieces & Bits.My_tourn) :
            self.myPieces |= bit
        else:
            self.opponentPieces |= bit

        self.pieces_placed += 1
        self.print_board()
        self.check_victory()
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
        if not Bits.is_adjacent(start_row, start_col, end_row, end_col):
            raise ValueError("Le mouvement n'est pas adjacent ou valide selon la règle")


        # Déplacer la pièce
        if self.myPieces & start_bit:
            self.myPieces &= ~start_bit
            self.myPieces |= end_bit
        elif self.opponentPieces & start_bit:
            self.opponentPieces &= ~start_bit
            self.opponentPieces |= end_bit

        # Changement de joueur
        self.print_board()
        self.check_victory()
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
        if(Bits.isCheck(self.opponentPieces)):
            print("player 1 win")
            self.reset5()
            return "oppenBorder wine "
        if(Bits.isCheck(self.myPieces)):
            print("oplayer 2 win")
            self.reset5()
            return "myPieces wine "
    
    def reset (self):
        self.myPieces = 0
        self.opponentPieces = 0
    
    def get_all_possible_moves():
        Bits.open_board(self) & 