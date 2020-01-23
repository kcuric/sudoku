import tkinter
from tkinter import ttk

class Matrix:

    def get_figure(self, master, board: list):
        size = len(board)
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
        