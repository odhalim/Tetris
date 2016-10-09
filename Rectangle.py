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
            return Piece_L([[1,2],[2,2],[3,2],[3,1]])
        elif choix == 2 :
            return Piece_S([[1,2],[2,2],[2,1],[3,1]])
        elif choix == 3 :
            return Piece_H([[1,1],[2,1],[3,1],[3,2]])
        elif choix == 4 :
            return Piece_O([[1,1],[1,2],[2,1],[2,2]])
        elif choix == 5 :
            return Piece_I([[1,2],[2,2],[3,2],[4,2]])

gameover = False
while gameover == False:
    rec  = Rectangle(20,29)
    aleatoire = randrange(1,5)
    print (aleatoire)
    block = rec.rand(aleatoire)
    """affichage"""
    
    gameover = True
    break





