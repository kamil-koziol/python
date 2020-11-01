from typing import List

def get_neighbors(matrix, (x, y)):
    neighbors = []
    height = len(matrix)
    width = len(matrix[0])
    for i in range(-1,2):
        if y+i < 0 or y+i > height:
            continue
        for j in range(-1,2):
            if x+j < 0 or x+j > width:
                continue
            if i == 0 and j == 0:
                continue

            neighbors.append((matrix[y+i][x+j], x+j, y+i))

    return neighbors

def get_first_letters_coordinates(matrix, letter):
    coordinates = []
    for y, row in enumerate(matrix):
        for x, le in enumerate(row):
            if le == letter:
                coordinates.append((x, y))
    return coordinates

def wsearch(matrix, word):
    coordinates = get_first_letters_coordinates(matrix, word[0])
    for coordinate in coordinates:
        if word[1] in get_neighbors(coordinate):
            



matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']
]

print(get_first_letters_coordinates(matrix, 'O'))
# print wsearch(matrix, 'FOAM')
# True
