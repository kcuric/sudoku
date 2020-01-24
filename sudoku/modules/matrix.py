import tkinter
from tkinter import ttk

class Matrix:

    def get_figure(self, master: object, board: list) -> object:
        '''
        Returns a visual representation of the sudoku
        board in the form of a matrix.

        Parameters:
        master (int): Tkinter master element.
        board (list): Sudoku board in form of a 2D list.

        Returns:
        object: Tkinter Frame containing the visual representation
                of a sudoku board in form of a matrix.
        '''
        matrix_frame = ttk.Frame(master=master)
        for i, row in enumerate(board): #Rows
            for j, element in enumerate(row): #Columns
                b = tkinter.Label(
                    matrix_frame, 
                    text=element,
                    borderwidth=1, 
                    relief=tkinter.SOLID, 
                    height=3, 
                    width=5, 
                    fg="black", 
                    bg="white"
                )
                b.grid(row=i, column=j)
        return matrix_frame
        