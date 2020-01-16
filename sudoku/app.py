from sudoku.modules.sudoku import Sudoku

def run():
    sudoku = Sudoku()
    sudoku.get_empty_board(9)
    sudoku.print_board((sudoku.get_solved_board(9)))