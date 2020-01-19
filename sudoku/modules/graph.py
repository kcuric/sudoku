import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    
    def __init__(self):
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
                self.labels[(row, col)] = label
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
                    pass
                try:
                    self.board.add_edge(self.labels[row, col],
                        self.labels[row + 1, col])
                except (IndexError, KeyError):
                    pass
                try:
                    self.board.add_edge(self.labels[row, col],
                        self.labels[row, col + 1])
                except (IndexError, KeyError):
                    pass
                try:
                    self.board.add_edge(self.labels[row, col],
                        self.labels[row - 1, col])
                except (IndexError, KeyError):
                    pass
    
    def _add_cluster_edges(self, board: list):
        '''
        Adds the edges between "clusters" to the board.

        Parameters:
        board (list): board.
        '''
        size = len(board)
        divider = 2 if size % 2 == 0 else 3
        num_sectors = int(size / divider)
        
        # Find cluster beginnings
        cluster_beginnings = []
        for i in range(0, size, divider):
            for j in range(0, size, divider):
                cluster_beginnings.append((i, j))
        
        # Iterate through cluster and add edges.
        for cluster in cluster_beginnings:
            current_cluster = []
            for row in range(cluster[0], cluster[0] + divider):
                for col in range(cluster[1], cluster[1] + divider):
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