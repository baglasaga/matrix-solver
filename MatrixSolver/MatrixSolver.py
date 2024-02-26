import numpy as np


# builds matrix to solve based on user input and returns it 
def buildMatrix():
    print("Input number of rows of matrix, then number of columns.");
    numRows = int(input("Number of rows?"));
    numCols = int(input("Number of columns?"));
    matrix = np.empty;
    for r in range(numRows):
        rows = np.empty;
        for c in range(numCols):
            element = int(input());
            # add element to col
        # add col to row
    # figure out how to add to a numpy matrix 
    return;

# code from here made with reference to https://www.geeksforgeeks.org/converting-matrix-into-row-echelon-form-in-python/ 

# uses Gaussian elimination method to row reduce entire matrix
def rowReduce(matrix):
    # matrix = matrix.astype(np.float64); TODO: work in progress work for fractions
    currentRow = 0;
    try:
        numCols = matrix.shape[1];
    except:
        numCols = 0; # for a n x 1 matrix
    for col in range(numCols): # loops through columns
        nonzero = nonZeroRow(matrix, currentRow, col);
        if nonzero != None:
            swapRows(matrix, currentRow, nonzero);
            setPivotToOne(matrix, currentRow, col);
            eliminateAboveBelow(matrix, currentRow, col);
            currentRow += 1;
    return matrix;

# PARAMS: matrix: array representing matrix to be solved
#         pivot: integer representing row number of current pivot row 
#         col: integer representing current column being reduced
# EFFECTS: returns the row number of first non-zero row below the current pivot row
def nonZeroRow(matrix, pivot, col):
    numRows = matrix.shape[0];
    for row in range(pivot, numRows):
        if matrix[row, col] != 0:
            return row;
    return None; # there are only zero rows 

# swaps rows at row numbers row1 and row2 in matrix
def swapRows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]];

# PARAMS: matrix: array representing matrix to be solved
#         pivot: integer representing row number of current pivot row 
#         col: integer representing current column being reduced
# MODIFIES: matrix
# EFFECTS: divides every element in pivot row by the value of the element at matrix[row, pivot] 
#          in order to set that element to 1
def setPivotToOne(matrix, pivot, col):
    matrix[pivot] //= matrix[pivot, col];

# PARAMS: matrix: array representing matrix to be solved
#         pivot: integer representing row number of current pivot row 
#         col: integer representing current column being reduced
# MODIFIES: matrix
# EFFECTS: sets all elements below matrix[pivot, col] to 0
def eliminateAboveBelow(matrix, pivot, col):
    numRows = matrix.shape[0];
    for row in range(0, numRows): 
        if row != pivot:
            factor = matrix[row, col];
            matrix[row] -= factor * matrix[pivot];



# prints out entire given matrix to console
def printMatrix(matrix):
    for row in matrix:
        print(*row);

