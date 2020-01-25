import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib
import math

class Graph:
    
    def __init__(self):
        matplotlib.use('agg')
        self.board = nx.Graph()
        self.labels = dict()
        self.display_labels = dict()

    def create_graph(self, board: list):
        self._add_nodes(board)
        self._add_edges(board)
        self._add_cluster_edges(board)

    def _add_nodes(self, board: list):
        '''
        Adds the nodes to the board.

        Parameters:
        board (list): board.
        '''
        label = 0
        for row in range(len(board)):
            for col in range(len(board)):
                label += 1
                self.labels[(col, row)] = label
                self.display_labels[label] = board[row][col]
                self.board.add_node(label)
    
    def _add_edges(self, board: list):
        '''
        Adds the "main" edges to the board.

        Parameters:
        board (list): board.
        '''
        label = 0
        for row in range(len(board)):
            for col in range(len(board)):
                try:
                    self.board.add_edge(self.labels[row, col],
                        self.labels[row, col - 1])
                except (IndexError, KeyError):
                    #TODO: Exception handling.
                    pass
                try:
                    self.board.add_edge(self.labels[row, col],
                        self.labels[row + 1, col])
                except (IndexError, KeyError):
                    #TODO: Exception handling.
                    pass
                try:
                    self.board.add_edge(self.labels[row, col],
                        self.labels[row, col + 1])
                except (IndexError, KeyError):
                    #TODO: Exception handling.
                    pass
                try:
                    self.board.add_edge(self.labels[row, col],
                        self.labels[row - 1, col])
                except (IndexError, KeyError):
                    #TODO: Exception handling.
                    pass
    
    def _add_cluster_edges(self, board: list):
        '''
        Adds the edges between "clusters" to the board.

        Parameters:
        board (list): board.
        '''
        order = len(board)
        cluster_order = int(math.sqrt(order))
        
        # Find cluster beginnings
        cluster_beginnings = []
        for i in range(0, order, cluster_order):
            for j in range(0, order, cluster_order):
                cluster_beginnings.append((i, j))
        
        # Iterate through cluster and add edges.
        for cluster in cluster_beginnings:
            current_cluster = []
            for row in range(cluster[0], cluster[0] + cluster_order):
                for col in range(cluster[1], cluster[1] + cluster_order):
                    current_cluster.append((row, col))

            for node in current_cluster:
                for _ in current_cluster:
                    self.board.add_edge(
                        self.labels[node],
                        self.labels[_]
                    )

    def show_graph(self):
        '''
        Shows the graph.

        Parameters:
        board (list): board.
        '''
        plt.clf()
        pos = dict((v,k) for k,v in self.labels.items())
        nx.draw_networkx(
            self.board,
            pos=pos,
            with_labels=True, 
            node_size=800,
            labels=self.display_labels
        )
        plt.axis('off')
        plt.show()

    def get_figure(self) -> object:
        '''
        Returns a visual representation of the sudoku
        board in the form of a somewhat simplyfied graph.

        Parameters:
        master (int): Tkinter master element.
        board (list): Sudoku board in form of a 2D list.

        Returns:
        object: Matplotlib polot containing the visual representation
                of a sudoku board in form of a graph.
        '''
        plt.clf()
        pos = dict((v,k) for k,v in self.labels.items())
        plt.gca().invert_yaxis()
        nx.draw_networkx(
            self.board,
            pos=pos,
            with_labels=True, 
            node_size=800,
            labels=self.display_labels,
        )
        plt.axis('off')
        return plt.gcf()
