import math

class Board:

    '''
    To be used in the future.
    '''

    def __init__(self, board: list):
        self.rows = board
        self.order = len(board)
        self.cluster_order = math.sqrt(self.order)
        self.cell_num = math.pow(self.order, 2)

    def get_rows(self):
        return self.rows

    def get_order(self):
        return self.order
    
    def get_cluster_order(self):
        return self.cluster_order

    def get_cell_num(self):
        return self.cell_num