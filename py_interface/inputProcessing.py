import data_engine as de
import errorHandling as err
############ BASIC PROCESSING ##############
def process(command):
    command = command.strip().split()
    for i in range(len(command)):
        command[i] = command[i].strip().lower()
    return command
################# MATRIX ####################
def flatten(mat):
    return [elem for row in mat for elem in row]
def reshape(flat, n):
    return [flat[i*n:(i+1)*n] for i in range(n)]
def matmul(command):
    if (len(command) <2):
        raise err.InvalidInstructionTypeError("'matadd' cannot have less than 2 arguments")
    matrices = int(command[2])
    if matrices <2:
        raise err.LowMatrixCountError("Cannot have number of matrices to be less than 2")
    final =[]
    r = int(input("Enter rows or Columns of the square matrix: "))
    for i in range(matrices):
        temp = []
        print(f"Enter rows for matrix {i+1}:")
        for j in range(r):
            while True:
                try:
                    tempRow = list(map(int, input(f"Enter row {j+1}: ").strip().split()))
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
        if isinstance(final[0], list):
            final = flatten(final)
        if i!=0:
            final = de.matrixMultiply(final, flatten(temp), r)
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
    for row in matrix:
        for val in row:
            print(f"{val:.2f}", end=" ")
        print()
def reshape(flat, r, c):
    return [flat[i*c:(i+1)*c] for i in range(r)]
def matadd(command):
    if (len(command) <2):
        raise err.InvalidInstructionTypeError("'matadd' cannot have less than 2 arguments")
    matrices = int(command[2])
    if matrices <2:
        raise err.LowMatrixCountError("Cannot have number of matrices to be less than 2")
    final =[]
    r = int(input("Enter number of rows of the matrix: ")) 
    c = int(input("Enter number of columns of the matrix: "))
    for i in range(matrices):
        print(f"Enter rows for matrix {i+1}:")
        temp = []
        for j in range(r):
            while True:
                try:
                    tempRow = list(map(float, input(f"Enter row {j+1}: ").strip().split()))
                    break
                except:
                    print("Please enter valid input")
            if len(tempRow) != c:
                raise err.MatrixInputInconsistencyError(f"Column length is not {c}")
            tempRow = list(map(float, tempRow))
            if i!=0:
                temp.append(tempRow)
            else:
                final.append(tempRow)
        if isinstance(final[0], list):
            final = flatten(final)
        if i!=0:
            final = de.matrixAdd(final, flatten(temp), r, c)
    final = reshape(final, r, c)
    outputMatrix(command, final)

def matsub(command):
    if (len(command) <2):
        raise err.InvalidInstructionTypeError("'matadd' cannot have less than 2 arguments")
    matrices = int(command[2])
    if matrices <2:
        raise err.LowMatrixCountError("Cannot have number of matrices to be less than 2")
    final =[]
    r = int(input("Enter number of rows of the matrix: ")) 
    c = int(input("Enter number of columns of the matrix: "))
    for i in range(matrices):
        temp = []
        print(f"Enter rows for matrix {i+1}:")
        for j in range(r):
            while True:
                try:
                    tempRow = list(map(float, input(f"Enter row {j+1} ").strip().split()))
                    break
                except:
                    print("Please enter valid input")
            if len(tempRow) != c:
                raise err.MatrixInputInconsistencyError(f"Column length is not {c}")
            tempRow = list(map(float, tempRow))
            if i!=0:
                temp.append(tempRow)
            else:
                final.append(tempRow)
        if isinstance(final[0], list):
            final = flatten(final)
        if i!=0:
            final = de.matrixSubtract(final, flatten(temp), r, c)
    final = reshape(final, r, c)
    outputMatrix(command, final)

################# Standard Data ###################


def meanData(command):
    if len(command)== 1:
        raise err.InvalidInstructionTypeError("'mean' should have atleast another argument")
    data = command[1:]
    data = list(map(float, data)) 
    print(f"The mean of the data is: {de.mean(data)}")

def medianData(command):
    if len(command) == 1:
        raise err.InvalidInstructionTypeError("'median' should have atleast another argument")
    data = command[1:]
    data = list(map(float, data))
    print(f"The median of thee data is: {de.median(data)}")
def modeData(command):
    if len(command) == 1:
        raise err.InvalidInstructionTypeError("'mode' should have atleast another argument")
    data = command[1:]
    data = list(map(float, data))
    print(f"The mode of the data is: {de.mode(data)}")
def varData(command):
    if len(command) == 1:
        raise err.InvalidInstructionTypeError("'var' should have atleast another argument")
    data = command[1:]
    data = list(map(float, data))
    print(f"The var of the data is: {de.var(data)}")

def std_devData(command):
    if len(command) == 1:
        raise err.InvalidInstructionTypeError("'std_dev' should have atleast another argument")
    data = command[1:]
    data = list(map(float, data))
    print(f"The Standard Deviation of the data is: {de.std_dev(data)}")



################# IDENTIFICATION ##################

def identify(command):
    match command[0]:
        case "matmul": return matmul
        case "matadd": return matadd
        case "matsub": return matsub
        case "mean": return meanData
        case "median": return medianData
        case "mode": return modeData
        case "var": return varData
        case "std_dev": return std_devData
        case "load": return load
        case "exit": exit()

        

    

