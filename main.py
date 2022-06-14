from os import getcwd, sep
from time import time
from tools.kakuro import Resolver
from tools.simulated_annealing import Solution

VERY_EASY = getcwd() + sep + 'data' + sep + 'very_easy.txt'
EASY = getcwd() + sep + 'data' + sep + 'easy.txt'
MEDIUM = getcwd() + sep + 'data' + sep + 'medium.txt'

class Main:

    def __init__(self, file) -> None:
        self.file = file
        self.grid = []

    # creates 2D array from txt file
    def __open_file(self):
        with open(self.file, 'r') as reader:
            return [line.replace('\n', '').split() for line in reader.readlines()] # removing \n from the line and split by whitespace character in many items in one array


    def resolve_kakuro(self):
        array = self.__open_file()
        t1 = time()
        resolver = Resolver(array)
        solution = Solution(cooling_factor=0.9, iterations=5000, temperature=1.0, Nt=100)
        solved = solution.resolve(resolver)
        t2 = time()
        print(f"Resolved :\n{solved}")
        print(f"Time : {round(t2 - t1, 3)}s")
        self.grid = solved.get_grid()

def main():
    main = Main(EASY)
    main.resolve_kakuro()

if __name__ == "__main__":
    main()