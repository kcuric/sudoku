from sudoku.modules.sudoku import Sudoku

def run():
    sudoku = Sudoku()
    print(sudoku.get_empty_board(9))
