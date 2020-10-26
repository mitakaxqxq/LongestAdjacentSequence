import sys

from create_matrix import get_coordinates, create_matrix
from solution import find_longest_adjacent_sequence

def main():
    for elem in sys.argv[1:]:
        elem = "tests/" + elem
        rows,cols = get_coordinates(elem)
        matrix = create_matrix(elem)
        print(find_longest_adjacent_sequence(rows, cols, matrix))

if __name__ == "__main__":
    main()