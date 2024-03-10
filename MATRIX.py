import numpy as np

# TAKING THE INPUT FOR BOTH MATRIX, IN ROWS AND COLUMNS.
m1_r = int(input("Enter the number of rows for both matrices: "))
m1_c = int(input("Enter the number of columns for both matrices: "))
a = 0
b = 0
total_ele = m1_r + m1_c
matrix_1 = []
matrix_2 = []

# Input for matrix 1
for i in range(1, m1_r + 1):
    list_row_1 = []
    matrix_1.append(list_row_1)
    for j in range(1, m1_c + 1):
        ele = int(input(f"Enter the {j} element of row {i} in matrix 1: "))
        list_row_1.append(ele)

# Input for matrix 2
for i in range(1, m1_r + 1):
    list_row_2 = []
    matrix_2.append(list_row_2)
    for j in range(1, m1_c + 1):
        ele = int(input(f"Enter the {j} element of row {i} in matrix 2: "))
        list_row_2.append(ele)

# print("MATRIX_1: ")
# for i in matrix_1:
#     print(i)
# print()
# print("MATRIX_2: ")
# for i in matrix_2:
#     print(i)
# print()
print("MATRIX 1:",np.array(matrix_1),"\n") #using 'NumPy' package
print("MATRIX 2:",np.array(matrix_2),"\n")


while True:
    oper = input("Enter the operation (ADD = '+', SUB = '-', MUL = '*', DIV = '/'): ")
    if oper not in ['+', '-', '*', '/']:
        print("Enter the right operational sign!")
    else:
        break

final_matrix = []

# Perform the operation on each element of the matrices
for i in range(m1_r):
    final_list = []
    final_matrix.append(final_list)
    for j in range(m1_c):
        if oper == "+":
            total = matrix_1[i][j] + matrix_2[i][j]
        elif oper == "-":
            total = matrix_1[i][j] - matrix_2[i][j]
        elif oper == "*":
            if m1_c != m1_r:
                print("Matrix multiplication is not possible. "
                      "Number of columns in Matrix 1 must be equal to the number of rows in Matrix 2.")
                exit()

            total = 0
            for k in range(m1_c):
                total += matrix_1[i][k] * matrix_2[k][j]
        elif oper == "/":
            total = matrix_1[i][j] / matrix_2[i][j]
        final_list.append(total)

print("\nFINAL_MATRIX: ")
for i in final_matrix:
    print(i)
print(f" It is in the order: {m1_r}X{m1_c}")
