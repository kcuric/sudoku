def get_empty_board(size: int) -> list:
    '''
    Generates an empty sudoku board.
    '''
    board = list()
    for _ in range(size):
        board.append([0 for x in range(size)])
    return board

def run():
    print(get_empty_board(9))
