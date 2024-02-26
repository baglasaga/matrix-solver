import numpy as np
import MatrixSolver as ms

def main():
    # testRowReductions(empty_matrix, empty_matrix, "empty matrix");
    testRowReductions(matrix_allZeroes, matrix_allZeroes, "zero matrix");
    testRowReductions(matrix_alreadySolved, matrix_alreadySolved, "already solved matrix");
    testRowReductions(matrix_1x1, matrix_1x1Solved, "1x1 matrix");
    testRowReductions(matrix_2x2, matrix_2x2Solved, "2x2 matrix");
    testRowReductions(matrix_1x3, matrix_1x3Solved, "1x3 matrix");
    testRowReductions(matrix_3x1, matrix_3x1Solved, "3x1 matrix");
    testRowReductions(matrix_3x4, matrix_3x4Solved, "3x4 matrix");
    testRowReductions(matrix_4x3, matrix_4x3Solved, "4x3 matrix");
    testRowReductions(matrix_almostSolved, matrix_almostSolvedSolved, "almost solved matrix");
    testRowReductions(matrix_zeroInMiddle, matrix_zeroInMiddleSolved, "matrix with a 0 row in the middle");
    testRowReductions(matrix_multipleZeroesInMiddle, matrix_multipleZeroesInMiddleSolved, "matrix with multiple 0 rows in the middle");

def testRowReductions(toTest, soln, name):
    print("Testing " + name + "...");

    success = np.array_equal(ms.rowReduce(toTest), soln);
    if not success:
        print("Test using " + name + " failed.");
        print("Expected output:");
        ms.printMatrix(soln);
        print("Actual output:");
        ms.printMatrix(toTest);
        return;
    
    print("Test " + name + " passed!");

###### definitions here
# empty_matrix = np.empty
# empty_matrix = np.array();

matrix_allZeroes = np.array([[0, 0, 0],
                             [0, 0, 0]
                             [0, 0, 0]]);

matrix_1x1 = np.array([[1, 2]]);
matrix_1x1Solved = np.array([[1, 0]]);

matrix_2x2 = np.array([[1, 2], 
                      [1, 3]]);
matrix_2x2Solved = np.array([[1, 0],
                            [0, 1]])

matrix_1x3 = np.array([[1],
                      [5],
                      [3]]);
matrix_1x3Solved = np.array([[1],
                            [0],
                            [0]])

matrix_3x1 = np.array([1, 1, 1]);
matrix_3x1Solved = np.array([1, 1, 1]);

matrix_almostSolved = np.array([[1, 0, 0],
                               [0, 1, 1],
                               [0, 0, 1]]);
matrix_almostSolvedSolved = np.array([[1, 0, 0],
                                     [0, 1, 0],
                                     [0, 0, 1]]);

matrix_alreadySolved = np.array([[1, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]]);

matrix_3x4 = np.array([[4, 1, 2, 0], 
                       [3, 1, 5, 0], 
                       [17, 2, 1, 2]]);
matrix_3x4Solved = np.array([[1, 0, 0, 1/4], 
                            [0, 1, 0, -7/6], 
                            [0, 0, 1, 1/12]]);

matrix_4x3 = np.array([[3, 1, 3],
                      [2, 2, 2],
                      [1, 1, 3],
                      [10, 15, 20]]);
matrix_4x3Solved = np.array([[1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 1],
                            [0, 0, 0]]);

# next two tests specifically tests if zero rows get pushed to the bottom 
matrix_zeroInMiddle = np.array([[1, 2, 3],
                               [2, 4, 6],
                               [3, 2, 1]]);
matrix_zeroInMiddleSolved = np.array([[1, 0, -1],
                                     [0, 1, 2],
                                     [0, 0, 0]]);

matrix_multipleZeroesInMiddle = np.array([[1, 2, 3],
                                         [2, 4, 6],
                                         [3, 6, 9],
                                         [3, 2, 1]]);
matrix_multipleZeroesInMiddleSolved = np.array([[1, 0, -1],
                                               [0, 1, 2],
                                               [0, 0, 0],
                                               [0, 0, 0]]);

main();