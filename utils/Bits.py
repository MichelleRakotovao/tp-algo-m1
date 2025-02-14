class Bits:
    My_tourn = 1 << 10  # 44e bit pour indiquer à qui le tour
    shift_verticale = 3
    shift_horizontale = 1
    shift_sland = 4
    shift_backslant = -4
    on_border = (1 << 9) - 1
    cols = 3
    rows = 3

    @staticmethod
    def at(row, col):
        return 1 << (col + (Bits.rows - 1 - row) * Bits.cols) #affichage inversé
        #return 1 << (col + row * Bits.rows)

    @staticmethod
    def count(pieces):
        return bin(pieces & Bits.on_border).count('1')

    @staticmethod
    def last_bit(bitboard):
        return bitboard & -bitboard

    def affichage_fanorona3(board1: int, board2: int, rows=3, cols=3):
        print(bin(board1) + "\n")
        print(bin(board2)+ "\n")
        print("\n╔" + "═" * ((2 * cols) + 1) + "╗")
        for row in reversed(range(rows)):
            print("║ ", end="")
            for col in range(cols):
                bit_position = col + (rows - 1 - row) * cols
                bit1 = (board1 >> bit_position) & 1
                bit2 = (board2 >> bit_position) & 1

                if bit1 and bit2:
                    cell = "E"
                elif bit1:
                    cell = "X"
                elif bit2:
                    cell = "O"
                else:
                    cell = " "

                print(cell, end=" ")
            print("║")
        print("╚" + "═" * ((2 * cols) + 1) + "╝\n")

    def myturn(MyPiece):
        return MyPiece & Bits.My_tourn

    def open_board(board):
        occupied = board.myPieces | board.opponentPieces
        open_position = Bits.on_border & ~occupied
        return open_position
    
    def isCheck(board):
    # Vérification des lignes horizontales
        for row in range(3):
            line = (board >> (row * 3)) & 0b111
            if line == 0b111:
                return True

        # Vérification des colonnes verticales
        for col in range(3):
            column = ((board >> col) & 1) & ((board >> (col + 3)) & 1) & ((board >> (col + 6)) & 1)
            if column == 1:
                return True

        # Vérification de la diagonale principale (haut gauche -> bas droite)
        if (board & 0b100000001) == 0b100000001 and (board & 0b001001000) == 0b001001000:
            return True

        # Vérification de la diagonale secondaire (haut droite -> bas gauche)
        if (board & 0b001000100) == 0b001000100 and (board & 0b100000010) == 0b100000010:
            return True

        return False

