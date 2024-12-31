import numpy as np


np.zeros(10)

np.ones(10)

arr = np.zeros(10)
arr[0:] = 5

np.random.randint(10, 51)

np.random.randint(10, 51, 2)

matriz = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

np.eye(3)

np.random.rand()

np.random.randn(5, 5)

zero_um = np.linspace(0, 1, 24)
print(zero_um)

matrix = np.arange(1, 26).reshape(5, 5)
output = matrix[2:, 1:]
print(output)


matrix1 = np.arange(1, 26).reshape(5, 5)
output1 = matrix[3:, 1:]
print(output1)

output2 = matrix[4:, 1:]
print(output2)

total_sum = np.sum(matrix)
print(total_sum)

std_variation = np.std(matrix)
print(std_variation)

total_sum_column = np.sum(matrix, axis=0)
print(total_sum_column)
