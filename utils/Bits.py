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
