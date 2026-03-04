import data_engine as de
import errorHandling as err
def process(command):
    command = command.strip().split()
    for i in range(len(command)):
        command[i] = command[i].strip().lower()
    return command

def flatten(mat):
    return [elem for row in mat for elem in row]
def reshape(flat, r):
    return [flat[i*r:(i+1)*r] for i in range(r)]
def matmul(command):
    matrices = int(command[2])
    if matrices <2:
        raise err.LowMatrixCountError("Cannot have number of matrices to be less than 2")
    final =[]
    r = int(input("Enter rows or Columns of the square matrix: "))
    for i in range(matrices):
        temp = []
        for j in range(r):
            while True:
                try:
                    tempRow = list(map(int, input(f"Enter row {i} ").strip().split()))
                    break
                except:
                    print("Please enter valid input")
            if len(tempRow) != r:
                raise err.MatrixInputInconsistencyError("Cannot Have different column lengths")
            tempRow = list(map(float, tempRow))
            if i!=0:
                temp.append(tempRow)
            else:
                final.append(tempRow)
        if i!=0:
            final = de.matrixMultiply(flatten(final), flatten(temp), r)
            final = reshape(final, r)
    outputMatrix(command, final)

def outputMatrix(command, final):
    if command[1] == "int":
        for i in range(len(final)):
            final[i] = list(map(int, final[i]))
        printMatrix(final)
    else: #as only int or double allowed
        printMatrix(final)

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(" ".join(map(str, matrix[i])))
    

def isLoad(command):
    return command == "load"

def identify(command):
    if (command[0]== 'matmul'):
        return matmul

