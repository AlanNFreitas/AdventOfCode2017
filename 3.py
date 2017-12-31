import numpy as np
from adventutils import matrix_center, manhattan

PUZZLE_INPUT = 312051

def spiral_matrix(n, sum_neighbors = False, puzzle_input = None):    
    directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    left_turn = {'N': 'W', 'S': 'E', 'E': 'N', 'W': 'S'}
    matrix = np.zeros((n,n))
    center = n // 2
    i = center
    j = center    
    matrix[i][j] = 1
    visited = {(i, j)}
    orientation = 'E'
    count = 1
    while count <= n ** 2:
        if (directions[left_turn[orientation]][0] + i,
                    directions[left_turn[orientation]][1] + j) in visited:
            i = i + directions[orientation][0]
            j = j + directions[orientation][1]         
        else:
            i = i + directions[left_turn[orientation]][0]
            j = j + directions[left_turn[orientation]][1]
            orientation = left_turn[orientation]
            
        count +=1

        if sum_neighbors == False:
            matrix[i][j] = count
        else:
            matrix[i][j] = sum_neighbors((i, j), matrix)
            if matrix[i][j] > puzzle_input:
                return matrix[i][j]
            
        visited.add((i,j))
                
    return matrix

mat = spiral_matrix(int(np.ceil(np.sqrt(PUZZLE_INPUT))))
coordinates = np.argwhere(mat == PUZZLE_INPUT)
y, x = coordinates[0]
c = matrix_center(mat)
dist = manhattan(x, y, c, c)
print(dist)
