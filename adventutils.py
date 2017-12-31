import os
import __main__ as main

def input_file():
    return open('input_files/{}.txt'.format(
            os.path.basename(main.__file__).split('.')[0]))

def input_string():
    return input_file().read().rstrip('\n')

def read_matrix(file, convert=str):    
    return (list(map(convert,line.strip().split('\t'))) for line in file)

def read_phrases(file):
    return [line.strip().split(' ') for line in file]

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print('{}\t'.format(element), end='')
        print('')

def manhattan(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def matrix_center(matrix):
    c = len(matrix) // 2
    return c

    


