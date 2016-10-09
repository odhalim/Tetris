from Piece import Piece

class Piece_O(Piece):

    def __init__(self,s):
        super(Piece_O, self).__init__(s)

    def move_left(self):
        print "move left"
        i = 0
        for elm in list:
            list[i][1] += 1
            i = i + 1

    def move_right(self):
        print "move right"
        i = 0
        for elm in list:
            list[i][1] -= 1
            i = i + 1

    def move_clockwise(self):
        pass

    def move_conter_clockwise(self):
        pass



