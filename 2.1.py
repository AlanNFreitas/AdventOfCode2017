from adventutils import input_file
from adventutils import read_matrix

file = input_file()
matrix = read_matrix(file, convert=int)
s = sum([next(x // y for x in row for y in row if (x != y and x % y == 0))
             for row in matrix])
print(s)
