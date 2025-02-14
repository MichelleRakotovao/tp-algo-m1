from board.BitBoard import BitBoard
from utils.Bits import Bits

bord1 = BitBoard()


bord1.place_piece(2,0)
bord1.place_piece(1,1)
bord1.place_piece(1,0)
bord1.place_piece(0,2)
bord1.place_piece(0,0)

#bord1.print_board()

#print(Bits.isCheck(bord1.myPieces))

succ = Bits.get_successors(2,2)

Bits.affichage_fanorona3(succ,0)

#print(Bits.is_adjacent(0, 2, 1, 1))

#bord1.print_board()
#openBoard = Bits.open_board(bord1)

#print(bord1.is_adjacent(0,0 , 0,1))

#bord1.get_successors(10 , bord1.myPieces , bord1.opponentPieces)

#print(bin(openBoard))





