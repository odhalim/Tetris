from abc import ABCMeta,abstractmethod

class Piece(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self,s):
        self.shape = s
        pass

    @abstractmethod
    def move_left(self):
        return

    @abstractmethod
    def move_right(self):
        return

    @abstractmethod
    def move_conter_clockwise(self):
        return

    @abstractmethod
    def move_clockwise(self):
        return