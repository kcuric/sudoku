from sudoku.modules.sudoku import Sudoku
from sudoku.modules.graph import Graph

def run():
    sudoku = Sudoku()
    board = sudoku.get_solved_board(9)

    sudoku.print_board(board)

    graph = Graph()
    graph.create_graph(board)
    graph.show_graph()
    
