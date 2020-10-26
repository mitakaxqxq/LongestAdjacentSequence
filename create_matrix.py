def get_coordinates(filename):
    try:
        file = open(filename, 'r')
    except Exception:
        print("There was a problem opening the file "+filename)
        return
    dimensions = file.readline()
    rows,cols = map(int, dimensions.split(' '))
    file.close()
    return rows,cols

def create_matrix(filename):
    try:
        file = open(filename, 'r')
    except Exception:
        print("There was a problem opening the file "+filename)
        return
    rows,cols = get_coordinates(filename)
    my_matrix = [[' ' for x in range(cols)] for y in range(rows)]
    file.readline()
    for i in range(rows):
        characters = file.readline()
        new_row = list((characters.rstrip()).split(' '))
        my_matrix[i] = new_row
    file.close()
    return my_matrix