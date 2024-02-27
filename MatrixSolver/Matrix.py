import MatrixSolver as ms

def main():
    matrix = ms.buildMatrix();
    reduced = ms.rowReduce(matrix);
    print("Row reduced matrix:");
    ms.printMatrix(reduced);

main();