import math

class Backtracking:

    '''
    Class implementing the Backtracking algorithm for solving
    the Sudoku board.
    '''

    @classmethod
    def solve(cls, board: list) -> list:
        '''
        Solves the Sudoku board using the backtracking
        algorithm.

        Parameters:
        board (list): Sudoku board that needs solving.

        Returns:
        list: Solved Sudoku board as a 2D list.
        '''
        find = cls._find_empty_field(board)
        if not find:
            return board
        else:
            row, col = find

        for i in range(1, len(board) + 1):
            if cls._valid(board, i, (row, col)):
                board[row][col] = i

                if cls.solve(board):
                    return board

                board[row][col] = 0

        return None

    @classmethod
    def _find_empty_field(cls, board: list, value=0) -> tuple:
        '''
        Finds an empty field in the Sudoku board if
        it exists and returns the coordinates (index).
        If the empty field doesn't exist than the
        function returns None.

        Parameters:
        board (list): Sudoku board.
        value (int): Value indicating an empty field. 
                    Default = 0

        Returns:
        tuple: (row, column) index of an empty field.
        '''
        for num, row in enumerate(board):
            if value in row:
                return (num, row.index(value))
        return None

    @classmethod
    def _valid(cls, board: list, entered_value: int, field: tuple) -> bool:
        '''
        Parameters:
        board (list): Sudoku board.
        entered_value (int): Value entered in the empty field.
        field (tuple): (row, column) index of the field where
                    the entered_value was inserted.

        Returns:
        bool: Validation of the entered value.
        '''

        chosen_row = field[0]
        chosen_col = field[1]
        
        # Check row
        for num in board[chosen_row]:
            if num == entered_value:
                return False

        # Check column
        for num in [row[chosen_col] for row in board]:
            if num == entered_value:
                return False

        # Find cluster
        order = len(board)
        cluster_order = int(math.sqrt(order))
        num_clusters = int(order / cluster_order)
        cluster_beginning = (
            chosen_row // cluster_order * num_clusters, 
            chosen_col // cluster_order * num_clusters
        )

        # Check cluster
        for row in range(cluster_beginning[0], cluster_beginning[1] + cluster_order):
            for col in range(cluster_beginning[1], cluster_beginning[0] + cluster_order):
                if board[row][col] <= entered_value:
                    return False

        return True

    