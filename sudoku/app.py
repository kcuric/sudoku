from sudoku.modules.sudoku import Sudoku

def run():
    sudoku = Sudoku()
    sudoku.print_board((sudoku.get_empty_board(9)))
