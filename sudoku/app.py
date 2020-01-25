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

# Tkinter master elements.

root = tkinter.Tk()
root.wm_title("Sudoku (Generator/Solver/Grapher)")
tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent, style='My.TFrame')
tab2 = ttk.Frame(tab_parent, style='My.TFrame')
tab_parent.add(tab1, text="Matrix")
tab_parent.add(tab2, text="Graph")

# Tkinter style

s = ttk.Style()
s.configure('My.TFrame', background='white')

# Tkinter global variables

size = tkinter.IntVar()
size.set(9)
algorithm = tkinter.IntVar()
algorithm.set(1)

# Class instances for visual represenation
graph = Graph()
matrix = Matrix()

def run():
    
    bottom_menu = tkinter.Frame(root, height="200", width="200")

    layout = [
        tkinter.Label(bottom_menu, text="Solving algorithm: "),
        tkinter.OptionMenu(
            bottom_menu, 
            algorithm, 
            Algortihms.BACKTRACKING, 
            Algortihms.DSATUR, 
            command=on_change_algorithm
        ),
        tkinter.Label(
            bottom_menu, 
            text="Board size: "
        ),
        tkinter.Radiobutton(
            master=bottom_menu, 
            text="9x9", 
            variable=size, 
            value=9
        ),
        tkinter.Button(
            master=bottom_menu, 
            text="Generate a solved board", 
            command= on_generate_click
        ),
        tkinter.Button(
            master=bottom_menu, 
            text="Quit", 
            command=on_quit
        )
    ]

    tab_parent.pack(expand=1, fill='both')
    bottom_menu.pack(side=tkinter.BOTTOM)

    for element in layout:
        element.pack(side=tkinter.LEFT)

    tkinter.mainloop()

def on_change_algorithm(alg):
    '''
    Event handler that exists only because there is no elegant way
    to represent algorithm name with text inside the option menu
    and store it's int value to the corresponding variable.
    '''
    algorithm.set(alg.value)

def on_generate_click():
    '''
    Event handler with the purpose of generating the 
    new solved sudoku board and visualy representing it
    via the imported classes.
    '''

    # Reset
    for child in tab1.winfo_children():
        child.destroy()

    for child in tab2.winfo_children():
        child.destroy()

    # Generate new solved sudoku.
    board = Solver.get_solved_board(size.get(), algorithm.get())

    # Draw Matrix
    matrix.get_figure(tab1, board).pack(expand=True)

    # Draw Graph
    graph.create_graph(board)
    graph_fig = graph.get_figure()
    graph_canvas = FigureCanvasTkAgg(graph_fig, master=tab2) 
    graph_canvas.draw()
    graph_canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def on_quit():
    '''
    Event handler for successfully exiting the app.
    '''
    root.quit()     
    root.destroy()  
