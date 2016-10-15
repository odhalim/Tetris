from Piece import  Piece
from Piece_S import Piece_S
from Piece_L import Piece_L
from Piece_O import Piece_O
from Piece_H import Piece_H
from Piece_I import Piece_I
from random  import randrange

class Rectangle():

    def __init__(self,width,height):
        self.width  = width
        self.height = height

    def rand(self,choix):
        if choix == 1:
            return Piece_L()
        elif choix == 2 :
            return Piece_S()
        elif choix == 3 :
            return Piece_H()
        elif choix == 4 :
            return Piece_O()
        elif choix == 5 :
            return Piece_I()

gameover = False
while gameover == False:
    rec  = Rectangle(20,29)
    aleatoire = randrange(1,5)
    print (aleatoire)
    block = rec.rand(aleatoire)
    """affichage"""
    
    gameover = True
    break





