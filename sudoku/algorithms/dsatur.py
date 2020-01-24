from sudoku.entities.cell import Cell
import math

class DSatur:

    '''
    Class implementing the DSatur algorithm for solving
    the Sudoku board.
    '''
        
    @classmethod
    def solve(cls, board: list) -> list:

        cells = list()
        for row in board:
            for el in row:
                cells.append(el)

        cls.size = len(cells)
        cls.order = int(math.sqrt(cls.size))
        cls.cluster_order = int(math.sqrt(cls.order))

        cls.cells = cls._create_cells(cells,cls.size)
        cls.clusters = cls._define_clusters(cls.size,cls.cluster_order,cls.order)
        cls._find_neighbors(cls.order)

        if cls.dSatur():
            board = list()
            row = list()
            for cells in cls.cells:                
                if(cells % cls.order == 0 and cells != 0):
                    board.append(row)
                    row = list()
                row.append(cls.cells[cells].get_content())
            board.append(row)
            return board
        else:
            #TODO: Exception handling.
            pass
    
    @classmethod
    def dSatur(cls) -> bool:
        '''
        Implementation of the DSatur algorithm.
        '''
        if cls._is_solved():
            return True
        biggest_saturation_index = cls._find_biggest_saturation()
        possible_values = cls.cells[biggest_saturation_index].possible_values(cls.order)
        if possible_values == -1:
            # Case if there are no possible values to enter to the cell.
            return False
        if not possible_values:
            # If the possible_colors list is empty.
            return False
        for value in possible_values:
            cls.cells[biggest_saturation_index].set_content(value)
            cls.cells[biggest_saturation_index].increase_saturation_neighbors()
            if cls.dSatur():
                return True
            else:
                cls.cells[biggest_saturation_index].decrease_saturation_neighbors()
                cls.cells[biggest_saturation_index].set_content(0)
        return False

    @classmethod
    def _create_cells(cls, cells: list, size: int) -> dict:
        '''
        Returns a dictionary whose keys are integers [0, size - 1] 
        and values are instances of a Node class containing the value.
        '''
        cells_dict = dict()
        for i in range(size):
            cells_dict[i] = Cell(i,cells[i])
        return cells_dict
    
    @classmethod
    def _define_clusters(cls,size: int, cluster_order: int ,order: int) -> list:
        '''
        Group the node indexes that belong in the same cluster.
        '''
        clusters_list = list()
        for first_node_vertical in range (0,size,cluster_order*order):
            for first_node_horizontal in range(first_node_vertical, first_node_vertical+order, cluster_order):
                node = set()
                for vertical in range(first_node_horizontal,first_node_horizontal + order*cluster_order-1,order):
                    for horizontal in range(vertical,vertical+cluster_order):
                        node.add(horizontal)
                clusters_list.append(node)
        return clusters_list

    @classmethod
    def _find_neighbors(cls, order: int):
        '''
        Using the bitwise "OR (|)" this method joins
        all the neighbor sets into one set that then
        represents all the neighbors of the node. 
        The method assigns the neighbors (merged set)
        to each the node (value) of the Sudoku board.
        '''
        
        for node in cls.cells:
            mod = node % order
            dif = order - mod
            lim = node + dif

            row_neighbors = set()
            for i in range(node-mod,lim):
                row_neighbors.add(i)

            column_neighbors = set()
            for going_up in range(node,0,-order):
                column_neighbors.add(going_up)
            for goind_down in range(node,cls.size,order):
                column_neighbors.add(goind_down)

            for cells in cls.clusters:
                if node in cells:
                    cluster_neighbors = cells

            neighbors = row_neighbors | column_neighbors | cluster_neighbors
            cls._assign_neighbors(node,neighbors)

    @classmethod
    def _assign_neighbors(cls,node,neighbors):
        '''
        Assigns the neighbor cells to the desired 
        node.
        '''
        for neighbor in neighbors:
            if (node != neighbor):
                cls.cells[node].set_neighbors(cls.cells[neighbor])
        cls.cells[node].calculate_saturation()

    @classmethod
    def _find_biggest_saturation(cls) -> int:
        '''
        Returns the index of the node with the
        biggest saturation.
        '''
        bigger_saturation = 0
        bigger_index = 0
        for node in cls.cells:
            if cls.cells[node].get_saturation() > bigger_saturation and cls.cells[node].get_content() == 0:
                bigger_saturation = cls.cells[node].get_saturation()
                bigger_index = node
        return bigger_index  

    @classmethod
    def _is_solved(cls) -> bool:
        '''
        Checks if all cells have been filled.
        '''
        for node in cls.cells:
            if cls.cells[node].get_content() == 0:
                return False
        return True
