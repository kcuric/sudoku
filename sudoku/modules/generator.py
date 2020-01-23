import random

class Generator:        

    @staticmethod
    def get_unsolved_board(size: int) -> list:
        '''
        Generates an empty board and then it
        populates the "diagonal" of the board with random
        numbers. Definition of the "diagonal" can be found
        in the README file as well as the explanation for
        this.

        Parameters:
        size (int): Size of the Sudoku board (size x size).

        Returns:
        list: Semi populated Sudoku board as a 2D list.
        '''
        board = list()
        for _ in range(size):
            board.append([0 for x in range(size)])
        
        divider = 2 if size % 2 == 0 else 3
        num_sectors = int(size / divider)
        possible_numbers_count = num_sectors * num_sectors
        for cluster in range(divider):
            possible_numbers = list([x for x in range(1, possible_numbers_count + 1)])
            possible_numbers = random.sample(possible_numbers, possible_numbers_count)
            for i in range(num_sectors):
                for j in range(num_sectors):
                    if possible_numbers:
                        board[i + num_sectors * cluster][j + num_sectors * cluster] = possible_numbers.pop()
                        
        return board

