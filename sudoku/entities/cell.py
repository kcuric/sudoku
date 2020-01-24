class Cell:

    def __init__(self,index: int, content: int):
        self.index = index
        self.content = content
        self.neighbors = []
        self.saturation_degree = 0
        self.degree = 0 # Number of neighbors

    def get_content(self) -> int:
        return self.content

    def set_content(self,content: int):
        self.content = content

    def set_neighbors(self, node):
        self.neighbors.append(node)
        self.degree += 1

    def possible_values(self,order: int) -> list:
        '''
        Returns the set of possible values 
        to enter.
        '''
        possible_numbers = list(range(1,order+1))
        possible_numbers_set = set(possible_numbers)
        alreadyExist = set()
        for neighbor in self.neighbors:
            if neighbor.get_content() == 0:
                continue
            alreadyExist.add(int(neighbor.get_content()))
        possible_numbers_set = possible_numbers_set - alreadyExist
        if (len(possible_numbers_set) == 0):
            return -1
        return list(possible_numbers_set)

    def calculate_saturation(self):
        for neighbor in self.neighbors:
            if neighbor.get_content() != 0:
                self.saturation_degree += 1

    def get_saturation(self):
        return self.saturation_degree

    def _increase_saturation(self):
        self.saturation_degree += 1

    def _decrease_saturation(self):
        self.saturation_degree -= 1

    def increase_saturation_neighbors(self):
        for neighbor in self.neighbors:
            neighbor._increase_saturation()

    def decrease_saturation_neighbors(self):
        for neighbor in self.neighbors:
            neighbor._decrease_saturation()