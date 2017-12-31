from adventutils import input_file
from adventutils import read_matrix

file = input_file()
matrix = read_matrix(file, convert=int)
s = sum([sum([-min(row), max(row)]) for row in matrix])
print(s)
