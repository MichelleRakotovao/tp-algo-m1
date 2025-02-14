from board.BitBoard import BitBoard
from utils.Bits import Bits
bord1 = BitBoard()


bord1.place_piece(0,0)
bord1.place_piece(0,1)
bord1.place_piece(0,2)

bord1.place_piece(1,0)
bord1.place_piece(1,1)
bord1.place_piece(1,2)
bord1.print_board()

bord1.make_move(1,0,2,1)

bord1.print_board()
#openBoard = Bits.open_board(bord1)

#print(bord1.is_adjacent(0,0 , 0,1))

#bord1.get_successors(10 , bord1.myPieces , bord1.opponentPieces)

#print(bin(openBoard))





