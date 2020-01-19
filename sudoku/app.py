from sudoku.modules.sudoku import Sudoku

def run():
    sudoku = Sudoku()
    sudoku.print_board((sudoku.get_solved_board(9)))
