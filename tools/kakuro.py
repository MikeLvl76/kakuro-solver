from copy import deepcopy
from random import randint

class Resolver:

    def __init__(self, next):
        self.size = 0
        self.grid = deepcopy(next)

    # read file and fills the grid with data
    def prepare(self):
        self.size = len(self.grid)
        self.fill_randomly()
        print(f"Base :\n{self}")

    def get_grid(self):
        return self.grid

    def get_size(self):
        return self.size

    # put a random value between 1 and 9 on all white cells
    def fill_randomly(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if len(self.grid[i][j]) == 1:
                    self.grid[i][j] = str(randint(1, 9))

    # change one random cell of the grid and return a new object with that grid
    def neighbor(self):
        array = deepcopy(self.grid)
        x = randint(1, len(array) - 1) 
        y = randint(1, len(array) - 1)
        rand = str(randint(1, 9))
        while len(array[x][y]) > 1: # searching for valid cell
            x = randint(1, len(array) - 1)
            y = randint(1, len(array) - 1)

        while array[x][y] == str(rand): # give a different value
            rand = randint(1, 9)
        array[x][y] = str(rand)

        return Resolver(array)

    # FITNESS 1 : count wrong row or col (uncomment it and comment the other to use)
    # def get_quality(self):
    #     quality = 0  
    #     for i in range(len(self.grid)):
    #         for j in range(len(self.grid[i])):
    #             if len(self.grid[i][j]) > 2: # indicator
    #                 indicator = self.grid[i][j]
    #                 splitted = indicator.split('/')
    #                 if splitted[0] != '0' and splitted[1] == '0': # down
    #                     s = 0
    #                     for a in range(i + 1, len(self.grid)):
    #                         if len(self.grid[a][j]) != 1:
    #                             break
    #                         s += int(self.grid[a][j]) # cells below 
    #                     if s != int(splitted[0]):
    #                         quality += 1

    #                 elif splitted[0] == '0' and splitted[1] != '0': # right
    #                     s = 0
    #                     for b in range(j + 1, len(self.grid)):
    #                         if len(self.grid[i][b]) != 1:
    #                             break
    #                         s += int(self.grid[i][b]) # cells at right
    #                     if s != int(splitted[1]):
    #                         quality += 1

    #                 elif splitted[0] != '0' and splitted[1] != '0': # down and right
    #                     s1, s2 = 0, 0
    #                     for x in range(i + 1, len(self.grid)):
    #                         if len(self.grid[x][j]) != 1:
    #                             break
    #                         s1 += int(self.grid[x][j])
    #                     for y in range(j + 1, len(self.grid)):
    #                         if len(self.grid[i][y]) != 1:
    #                             break
    #                         s2 += int(self.grid[i][y])
    #                     if s1 != int(splitted[0]):
    #                         quality += 1
    #                     if s2 != int(splitted[1]):
    #                         quality += 1
    #     return quality

    # FITNESS 2 : calculate the sum of absolute values of difference between the indicator's value and the sum obtained
    def get_quality(self):
        quality = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if len(self.grid[i][j]) > 2: # indicator
                    s, s1, s2 = 0, 0, 0
                    indicator = self.grid[i][j]
                    splitted = indicator.split('/')
                    if splitted[0] != '0' and splitted[1] == '0': # down
                        for a in range(i + 1, len(self.grid)):
                            if len(self.grid[a][j]) != 1:
                                break
                            s += int(self.grid[a][j]) # cells below 
                        quality += abs(int(splitted[0]) - s)

                    elif splitted[0] == '0' and splitted[1] != '0': # right
                        for b in range(j + 1, len(self.grid)):
                            if len(self.grid[i][b]) != 1:
                                break
                            s += int(self.grid[i][b]) # cells at right
                        quality += abs(int(splitted[1]) - s)

                    elif splitted[0] != '0' and splitted[1] != '0': # down and right

                        for x in range(i + 1, len(self.grid)):
                            if len(self.grid[x][j]) != 1:
                                break
                            s1 += int(self.grid[x][j])
                        for y in range(j + 1, len(self.grid)):
                            if len(self.grid[i][y]) != 1:
                                break
                            s2 += int(self.grid[i][y])

                        quality += abs(int(splitted[0]) - s1) + abs(int(splitted[1]) - s2)
        return quality

    def __str__(self):
        string = ""
        for row in self.grid:
            for elt in row:
                if len(elt) > 2:
                    if elt.split('/')[0] == '0' and elt.split('/')[1] != '0':
                        string += '/' + elt.split('/')[1] # right
                    elif elt.split('/')[0] != '0' and elt.split('/')[1] == '0':
                        string += elt.split('/')[0] + '/' # down
                    else:
                        string += elt
                else:
                    string += elt
                string += "\t"
            string += "\n"
        return string