import random
col_1 = int(input('col_1 = '))
col_2 = int(input('col_2 = '))

matrix_1=[[random.randint(1, 11) for j in range(col_2)] for i in range(col_1) ]
print('matrix 1: ')
for i in range(col_1):
    print(matrix_1[i])

matrix_2 = [ [ random.randint(1, 11) for j in range(col_2)] for i in range(col_1) ]
print('matrix 2: ')
for i in range(col_1):
    print(matrix_2[i])

result = [[matrix_1[i][j] + matrix_2[i][j]  for j in range
(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Сложение: ")
for r in result:
    print(r)