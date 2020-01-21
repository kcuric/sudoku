from sudoku.modules.sudoku import Sudoku
from sudoku.modules.graph import Graph
from sudoku.modules.matrix import Matrix

import tkinter
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

root = tkinter.Tk()
root.wm_title("Sudoku (Generator/Solver/Grapher)")
sudoku = Sudoku()
graph = Graph()
matrix = Matrix()

size = tkinter.IntVar()
algorithm = tkinter.StringVar(root)
algorithm.set("Backtracking")

s = ttk.Style()
s.configure('My.TFrame', background='white')

tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent, style='My.TFrame')
tab2 = ttk.Frame(tab_parent, style='My.TFrame')
tab_parent.add(tab1, text="Matrix")
tab_parent.add(tab2, text="Graph")

def run():
    global root
    
    frame = tkinter.Frame(root, height="200", width="200")

    layout = [
        tkinter.OptionMenu(frame, algorithm, "Backtracking", "DSatur"),
        tkinter.Radiobutton(master=frame, text="9x9", variable=size, value=9),
        tkinter.Button(master=frame, text="Generate", command= _generate),
        tkinter.Button(master=frame, text="Quit", command=_quit)
    ]

    tab_parent.pack(expand=1, fill='both')
    frame.pack(side=tkinter.BOTTOM)

    for element in layout:
        element.pack(side=tkinter.LEFT)

    tkinter.mainloop()

def _generate():
    global size

    # Reset
    for child in tab2.winfo_children():
        child.destroy()

    # Generate new solved sudoku.
    board = sudoku.get_solved_board(size.get())

    # Draw Matrix
    matrix.get_figure(tab1, board).pack(expand=True)

    # Draw Graph
    graph.create_graph(board)
    graph_fig = graph.get_figure()
    graph_canvas = FigureCanvasTkAgg(graph_fig, master=tab2) 
    graph_canvas.draw()
    graph_canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def _quit():
    global root
    root.quit()     
    root.destroy()  
