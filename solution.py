import sys

def is_valid_coordinate(x, y, rows, cols):
    if x >= 0 and y >= 0 and x < rows and y < cols:
        return True
    else:
        return False

def get_possible_neighbours(x, y, rows, cols):
    neighbours = []
    if is_valid_coordinate(x - 1, y, rows, cols):
        neighbours.append((x - 1, y))
    if is_valid_coordinate(x, y - 1, rows, cols):
        neighbours.append((x, y - 1))
    if is_valid_coordinate(x + 1, y, rows, cols):
        neighbours.append((x + 1, y))
    if is_valid_coordinate(x, y + 1, rows, cols):
        neighbours.append((x, y + 1))
    return neighbours

def bfs(row, col, matrix, elem, visited):
    count = 0
    queue = []
    queue.append((row, col))
    while queue:
        current_elem = queue.pop(0)
        x, y = current_elem[0], current_elem[1]
        neighbours = get_possible_neighbours(x, y, len(matrix), len(matrix[0]))
        if matrix[x][y] == elem and visited[x][y] == False:
            visited[x][y] = True
            count += 1
            for element in neighbours:
                queue.append(element)
    return count


def find_longest_adjacent_sequence(rows, cols, matrix):
    visited = [[False for y in range(cols)] for x in range(rows)]
    longest_adjacent_sequence = 0
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == False:
                result = bfs(i, j, matrix, matrix[i][j], visited)
                if result > longest_adjacent_sequence:
                    longest_adjacent_sequence = result
    return longest_adjacent_sequence