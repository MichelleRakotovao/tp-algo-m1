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
    
    def isCheck(board: int) -> bool:
        lignes = [0b111, 0b111000, 0b111000000]
        colonnes = [0b1001001, 0b010010010, 0b001001001]
        diagonales = [0b100010001, 0b001010100]

        for ligne in lignes:
            if board & ligne == ligne:
                return True

        for colonne in colonnes:
            if board & colonne == colonne:
                return True

        for diag in diagonales:
            if board & diag == diag:
                return True

        return False
    
    
    def is_adjacent(i1, j1, i2, j2):
        di = i2 - i1
        dj = j2 - j1

        # Vérification des déplacements adjacents horizontaux et verticaux
        if (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            return True
        
        # Vérification des déplacements diagonaux
        if (di, dj) in [(-1, -1), (1, 1), (-1, 1), (1, -1)] and (i1+j1)%2 == 0 :
            return True

        return False
    
    def is_adjacent2(i1, j1, i2, j2):
        di = i2 - i1
        dj = j2 - j1

        # Vérification des déplacements adjacents horizontaux et verticaux
        if (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            return True
        
        # Vérification des déplacements diagonaux
        if (di, dj) in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
            print(di , dj )
            if (i1 == j1) or (i1 == -j1):
                print(di , dj )
                if (i1 == j1 and i2 == j2) or (i1 == -j1 and i2 == -j2):
                    return True

        return False



    def get_successors(i, j):
        successors = 0
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (1, 1), (-1, 1), (1, -1)
        ]

        for di, dj in directions:
            ni, nj = i + di, j + dj
            #print(ni , nj)
            #print("     ****   ")
            if 0 <= ni < 3 and 0 <= nj < 3 and Bits.is_adjacent(i, j, ni, nj):
                #print(ni , nj)
                position = ni * 3 + nj
                successors |= (1 << position)

        return successors



