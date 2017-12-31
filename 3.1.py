import numpy as np

PUZZLE_INPUT = 312051

def spiral_matrix(n, neighbors = False, puzzle_input = None):    
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

        if neighbors == False:
            matrix[i][j] = count
        else:
            matrix[i][j] = sum_neighbors((i, j), matrix)
            if matrix[i][j] > puzzle_input:
                return matrix[i][j]
            
        visited.add((i,j))
                
    return matrix

def sum_neighbors(coordinates, matrix):
    result = 0
    i = coordinates[0]
    j = coordinates[1]
    for delta_i in [-1, 0, 1]:
        if delta_i == 0:
            delta_j_list = [-1, 1]
        else:
            delta_j_list = [-1,0,1]
            
        for delta_j in delta_j_list:
            if  (0 <= i + delta_i < len(matrix)
                 and 0 <= j + delta_j < len(matrix)):
                result += matrix[i + delta_i][j + delta_j]
    return result

print(int(spiral_matrix(50, True, PUZZLE_INPUT)))

