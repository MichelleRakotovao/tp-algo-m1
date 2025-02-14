from board.BitBoard import BitBoard
from IA.IA_module import AiModule
from utils.utils import manual_input


player = int(input("player1 ou player2 [1 ou 2] :"))
current_player = "AI"
if(player==2):
    bord1 = BitBoard(False)
else:
    bord1 = BitBoard()

ai = AiModule(max_depth=3)
manual_input(bord1,ai)

