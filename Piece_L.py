from Piece import Piece

class Piece_L(Piece):

    def __init__(self,s):
        super(Piece_L, self).__init__(s)

    def move_left(self,list):
        print "move left"
        i = 0
        for elm in list:
            list[i][1] +=1
            i = i + 1


    def move_right(self,list):
        print "move right"
        i = 0
        for elm in list:
            list[i][1] -=1
            i = i + 1

    def move_clockwise(self):
        print "move clockwise"

        i = 0
        while i < len(object):
            R = [[0, 1], [-1, 0]]
            print(object[i])
            v = object[i]
            p = object[1]
            vr = [(v[0] - p[0]), (v[1] - p[1])]
            vt = []
            vt.append((R[0][0] * vr[0]) + (R[0][1] * vr[1]))
            vt.append((R[1][0] * vr[0]) + (R[1][1] * vr[1]))
            v_final = []
            v_final.append(p[0] + vt[0])
            v_final.append(p[1] + vt[1])

            object[i] = v_final
            i += 1

    def move_conter_clockwise(self,list):
        print "move conter clokwise"
        i=0
        while i < len(list):
            R = [[0, -1], [1, 0]]
            print(list[i])
            v = list[i]
            p = list[1]
            vr = [(v[0] - p[0]), (v[1] - p[1])]
            vt = []
            vt.append((R[0][0] * vr[0]) + (R[0][1] * vr[1]))
            vt.append((R[1][0] * vr[0]) + (R[1][1] * vr[1]))
            v_final = []
            v_final.append(p[0] + vt[0])
            v_final.append(p[1] + vt[1])

            list[i] = v_final
            i += 1

