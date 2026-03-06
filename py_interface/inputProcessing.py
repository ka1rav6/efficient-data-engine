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
        print(*(f"{v:.2f}" for v in row))
def reshape(flat, r, c):
    return [flat[i*c:(i+1)*c] for i in range(r)]
def matrixOperation(command, operation):
    matrices = int(command[2])
    r = int(input("Rows: "))
    c = int(input("Columns: "))
    final = []
    for i in range(matrices):
        temp = []
        print(f"Matrix {i+1}")
        for j in range(r):
            row = list(map(float, input(f"Row {j+1}: ").split()))
            if len(row) != c:
                raise err.MatrixInputInconsistencyError
            if i == 0:
                final.append(row)
            else:
                temp.append(row)
        if isinstance(final[0], list):
            final = flatten(final)
        if i != 0:
            final = operation(final, flatten(temp), r, c)
    final = reshape(final, r, c)
    printMatrix(final)
def matadd(command):
    matrixOperation(command, de.matrixAdd)

def matsub(command):
    matrixOperation(command, de.matrixSubtract)
################# Standard Data ###################

def statData(command, func, name):
    if len(command) == 1:
        raise err.InvalidInstructionTypeError
    data = list(map(float, command[1:]))
    print(f"{name}:", func(data))

def meanData(command): statData(command, de.mean, "Mean")
def medianData(command): statData(command, de.median, "Median")
def modeData(command): statData(command, de.mode, "Mode")
def varData(command): statData(command, de.var, "Variance")
def stdData(command): statData(command, de.std_dev, "Std Dev")
def minimumData(command): statData(command, de.min, "Minimum")
def maximumData(command): statData(command, de.max, "Maximum")
def rangeData(command): statData(command, de.range, "Range")

def statDataMore(command, func, name):
    if len(command) < 3:
        raise err.InvalidInstructionTypeError
    val = float(command[1])
    data = list(map(float, command[2:]))
    print(f"{name}:", func(data, val))
def zscoreData(command): statDataMore(command, de.zscore, "Zscore")
def percentileData(command): statDataMore(command, de.percentile, "Percentile")
################# IDENTIFICATION ##################

def identify(command):
    if command[0] == "exit":
        sys.exit()
    if command[0] not in COMMANDS:
        raise err.InvalidInstructionTypeError
    return COMMANDS[command[0]]

###################### SORTING ##############
def sortData(command, sorter):
    if len(command) < 3:
        raise err.InvalidInstructionTypeError
    if command[1] == "int":
        data = list(map(int, command[2:]))
    else:
        data = list(map(float, command[2:]))
    data = sorter(data)
    print("Sorted:", *data)
    
def quickSort(command): sortData(command, de.quickSort)
def bubbleSort(command): sortData(command, de.bubbleSort)
def insertionSort(command): sortData(command, de.insertionSort)

########### FILE HANDLING #####################
import sys
def load(command):
    fileName = input("Enter the file path: ")
    print("Enter commands:")
    while True:
        command1 = input("\t>>>>  ")
        command1 = process(command1)
        func = identifyFileCommand(command1)
        func(fileName, command1)
def identifyFileCommand(command):
    if command[0] in ["exit", "file.close"]:
        sys.exit()
    if command[0] not in FILE_COMMANDS:
        raise err.InvalidInstructionTypeError
    whole, label = FILE_COMMANDS[command[0]]
    if (command[0] in ["zscore", "percentile"]):
        return whole if len(command)==2 else label
    return whole if len(command) == 1 else label

def labelStat(file, command):
    stat = command[0]
    special = False
    try:
        num =float(command[1])
        special = True
        label = "".join(command[2:]).capitalize()
    except:
        pass
    if not special:
        values = FILE_STATS[stat](file)
        label = "".join(command[1:]).capitalize()
    else:
        values = FILE_STATS[stat](file, num)
    labels = de.getLabels(file)
    
    if label in labels:
        i = labels.index(label)
        print(f"{stat}: {values[i]:.2f}")
FILE_STATS = {
    "mean": de.meanWhole,
    "median": de.medianWhole,
    "mode": de.modeWhole,
    "var": de.varWhole,
    "std_dev": de.std_devWhole,
    "min": de.miniWhole,
    "max": de.maxiWhole,
    "range": de.rangeWhole,
    "zscore": de.zscoreWhole,
    "percentile": de.percentileWhole
}
def wholeStat(file, command):
    stat = command[0]
    special = False
    try:
        num =float(command[1])
        special = True
    except:
        pass
    if not special:
        values = FILE_STATS[stat](file)
    else:
        values = FILE_STATS[stat](file, num)
    labels = de.getLabels(file)
    for l, v in zip(labels, values):
        print(f"{l}: {v:.2f}")
FILE_COMMANDS = {
    "mean": (wholeStat, labelStat),
    "median": (wholeStat, labelStat),
    "mode": (wholeStat, labelStat),
    "var": (wholeStat, labelStat),
    "std_dev": (wholeStat, labelStat),
    "min" : (wholeStat, labelStat),
    "max" : (wholeStat, labelStat),
    "range" : (wholeStat, labelStat),
    "zscore": (wholeStat, labelStat),
    "percentile": (wholeStat, labelStat),
}

COMMANDS = {
    "matmul": matmul,
    "matadd": matadd,
    "matsub": matsub,
    "mean": meanData,
    "median": medianData,
    "mode": modeData,
    "var": varData,
    "std_dev": stdData,
    "load": load,
    "quicksort": quickSort,
    "bubblesort": bubbleSort,
    "insertionsort": insertionSort,
    "min": minimumData,
    "max": maximumData,
    "range": rangeData,
    "percentile": percentileData,
    "zscore": zscoreData,
}