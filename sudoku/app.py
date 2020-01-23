from sudoku.modules.solver import Solver
from sudoku.algorithms.algorithms import Algortihms
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
graph = Graph()
matrix = Matrix()

size = tkinter.IntVar()
algorithm = tkinter.IntVar(root)
algorithm.set(Algortihms.BACKTRACKING)

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
        tkinter.Label(frame, text="Solving algorithm: "),
        tkinter.OptionMenu(frame, algorithm, "Backtracking", "DSatur"),
        tkinter.Label(frame, text=" | "),
        tkinter.Label(frame, text="Board size: "),
        tkinter.Radiobutton(master=frame, text="9x9", variable=size, value=9),
        tkinter.Label(frame, text=" | "),
        tkinter.Button(master=frame, text="Generate a solved board", command= _generate),
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
    for child in tab1.winfo_children():
        child.destroy()

    for child in tab2.winfo_children():
        child.destroy()

    # Generate new solved sudoku.
    board = Solver.get_solved_board(9, Algortihms.BACKTRACKING)

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
