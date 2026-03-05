import data_engine as de # type: ignore   ## to ignore the warning error 
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
        case "quicksort": return quickSort
        case "bubblesort": return bubbleSort
        case "insertionsort": return insertionSort
        case "exit": exit()
        case _: raise err.InvalidInstructionTypeError(f"{command[0]} is not a valid command")
def invalid(command):
    print("Please Enter a vaild command")
###################### SORTING ##############
def quickSort(command):
    if len(command) <3:
        raise err.InvalidInstructionTypeError("'quickSort' should have atleast another argument")
    data = command[2:]
    try:
        if command[1]=="int":
            data = list(map(int, data))
        else:
            data = list(map(float, data))
    except:
        raise TypeError("Only int and float allowed")
    data = de.quickSort(data)
    print("The sorted array is:\n", *data)
def bubbleSort(command):
    if len(command) == 1:
        raise err.InvalidInstructionTypeError("'quickSort' should have atleast another argument")
    data = command[2:]
    try:
        if command[1]=="int":
            data = list(map(int, data))
        else:
            data = list(map(float, data))
    except:
        raise TypeError("Only int and float allowed")
    data = de.bubbleSort(data)
    print("The sorted array is:\n", *data)
def insertionSort(command):
    if len(command) == 1:
        raise err.InvalidInstructionTypeError("'quickSort' should have atleast another argument")
    data = command[2:]
    try:
        if command[1]=="int":
            data = list(map(int, data))
        else:
            data = list(map(float, data))
    except:
        raise TypeError("Only int and float allowed")
    data = de.quickSort(data)
    print("The sorted array is:\n", *data)

########### FILE HANDLING #####################
import sys
def identifyFileCommand(command):
    if len(command)==1:
        match command[0]:
            case "file.close": sys.exit(0)
            case "mean": return wholeMean
            case "median": return wholeMedian
            case "mode": return wholeMode
            case "var": return wholeVar
            case "std_dev": return wholeStd_dev
            case "exit": sys.exit(0)
            case "_": raise err.InvalidInstructionTypeError(f"{command[0]} is not a valid command")
    else:
        match command[0]:
            case "mean": return labelMean
            case "median": return labelMedian
            case "mode": return labelMode
            case "var": return labelVar
            case "std_dev": return labelStd_dev
            case "_": raise err.InvalidInstructionTypeError(f"{command[0]} is not a valid command")
def labelMean(file, command):
    meanList = de.meanWhole(file)
    labelList = de.getLabels(file)
    
    label = "".join(command[1:])
    label = label.capitalize()
    print(labelList)
    if label in labelList:
        idx = labelList.index(label)
        print(f"Mean: {meanList[idx]:.2f}")
def labelMedian(file, command):
    medianList = de.medianWhole(file)
    labelList = de.getLabels(file)
    
    label = "".join(command[1:])
    label = label.capitalize()
    print(labelList)
    if label in labelList:
        idx = labelList.index(label)
        print(f"Median: {medianList[idx]:.2f}")
def labelMode(file, command):
    modeList = de.modeWhole(file)
    labelList = de.getLabels(file)
    
    label = "".join(command[1:])
    label = label.capitalize()
    print(labelList)
    if label in labelList:
        idx = labelList.index(label)
        print(f"Mode: {modeList[idx]:.2f}")
def labelVar(file, command):
    varList = de.varWhole(file)
    labelList = de.getLabels(file)
    
    label = "".join(command[1:])
    label = label.capitalize()
    print(labelList)
    if label in labelList:
        idx = labelList.index(label)
        print(f"Var: {varList[idx]:.2f}")
def labelStd_dev(file, command):
    std_devList = de.std_devWhole(file)
    labelList = de.getLabels(file)
    
    label = "".join(command[1:])
    label = label.capitalize()
    print(labelList)
    if label in labelList:
        idx = labelList.index(label)
        print(f"Standard Deviation: {std_devList[idx]:.2f}")
        
def load(command):
    fileName = input("Enter the file path: ")
    print("Enter commands:")
    while True:
        command1 = input("\t>>>>  ")
        command1 = process(command1)
        func = identifyFileCommand(command1)
        func(fileName, command1)
def wholeMean(file, command):
    meanList = de.meanWhole(file)
    labelList = de.getLabels(file)
    for i in range(len(labelList)):
        print(f"Label: {labelList[i]}, mean: {meanList[i]:.2f}")
def wholeMedian(file, command):
    medianList = de.medianWhole(file)
    labelList = de.getLabels(file)
    for i in range(len(labelList)):
        print(f"Label: {labelList[i]}, median: {medianList[i]:.2f}")
def wholeMode(file, command):
    modeList = de.modeWhole(file)
    labelList = de.getLabels(file)
    for i in range(len(labelList)):
        print(f"Label: {labelList[i]}, mode: {modeList[i]:.2f}")
def wholeVar(file, command):
    varList = de.varWhole(file)
    labelList = de.getLabels(file)
    for i in range(len(labelList)):
        print(f"Label: {labelList[i]}, variance: {varList[i]:.2f}")
def wholeStd_dev(file, command):
    stdList = de.std_devWhole(file)
    labelList = de.getLabels(file)
    for i in range(len(labelList)):
        print(f"Label: {labelList[i]}, Standard Deviation: {stdList[i]:.2f}")
