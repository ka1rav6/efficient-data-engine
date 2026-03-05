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
def matadd(command):
    pass  
def matsub(command):
    pass  

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

        

    

