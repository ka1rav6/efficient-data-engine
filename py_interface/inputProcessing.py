import sys
import os
import platform
from pathlib import Path
import data_engine as de               # type: ignore
import errorHandling as err

def clearScreen():
    """Clear the terminal screen in a cross-platform way."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

############ BASIC PROCESSING ##############
def process(command):
    try:
        # FIX 3: split commas across ALL tokens, not just the last one
        tokens = command.strip().split()
        result = []
        for token in tokens:
            result.extend(token.split(","))
        command = [t.strip().lower() for t in result if t.strip()]
    except (ValueError, TypeError):    # FIX 6: specific exception instead of bare except
        raise err.InvalidFormat(f"{command} is not a valid format")
    return command

################# MATRIX ####################
def flatten(mat):
    return [elem for row in mat for elem in row]

def reshapeSquare(flat, n):
    return [flat[i*n:(i+1)*n] for i in range(n)]
def reshape(flat, r, c):
    return [flat[i*c:(i+1)*c] for i in range(r)]
def matmul(command):
    if len(command) < 3:
        raise err.InvalidInstructionTypeError("'matmul' requires a datatype and number of matrices")
    matrices = int(command[2])
    if matrices < 2:
        raise err.LowMatrixCountError("Cannot have number of matrices to be less than 2")
    final = []
    r = int(input("Enter rows/columns of the square matrix: "))
    for i in range(matrices):
        temp = []
        print(f"Enter rows for matrix {i+1}:")
        for j in range(r):
            while True:
                try:
                    tempRow = list(map(int, input(f"Enter row {j+1}: ").strip().split()))
                    break
                except (ValueError, TypeError):    # FIX 6: specific exception
                    print("Please enter valid input")
            if len(tempRow) != r:
                raise err.MatrixInputInconsistencyError("Cannot have different column lengths")
            tempRow = list(map(float, tempRow))
            if i != 0:
                temp.append(tempRow)
            else:
                final.append(tempRow)
        if isinstance(final[0], list):
            final = flatten(final)
        if i != 0:
            final = de.matrixMultiply(final, flatten(temp), r)
    final = reshapeSquare(final, r)    # FIX 1: call reshapeSquare() so the 3-arg reshape() isn't called with 2 args
    outputMatrix(command, final)
def outputMatrix(command, final):
    if command[1] == "int":
        for i in range(len(final)):
            final[i] = list(map(int, final[i]))
        printMatrix(final)
    else:
        printMatrix(final)

def printMatrix(matrix):
    for row in matrix:
        print(*(f"{v:.2f}" for v in row))
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
    try:
        data = list(map(float, command[1:]))
    except (ValueError, TypeError):    # FIX 6: specific exception
        raise err.InvalidInstructionTypeError
    print(f"{name}:", func(data))

## wrappers
def meanData(command):      statData(command, de.mean,    "Mean")
def medianData(command):    statData(command, de.median,  "Median")
def modeData(command):      statData(command, de.mode,    "Mode")
def varData(command):       statData(command, de.var,     "Variance")
def stdData(command):       statData(command, de.std_dev, "Std Dev")
def minimumData(command):   statData(command, de.min,     "Minimum")
def maximumData(command):   statData(command, de.max,     "Maximum")
def rangeData(command):     statData(command, de.range,   "Range")

def statDataMore(command, func, name):
    if len(command) < 3:
        raise err.InvalidInstructionTypeError
    val = float(command[1])
    data = list(map(float, command[2:]))
    print(f"{name}:", func(data, val))

def zscoreData(command):    statDataMore(command, de.zscore,     "Zscore")
def percentileData(command): statDataMore(command, de.percentile, "Percentile")

################# IDENTIFICATION ##################
def identify(command):
    if command[0] == "exit":
        sys.exit()                     # FIX 2: sys is now imported at the top, so this is always safe
    if command[0] not in COMMANDS:
        raise err.InvalidInstructionTypeError
    return COMMANDS[command[0]]

###################### SORTING ##############
def sortData(command, sorter):
    if len(command) < 3 or command[1] not in ["int", "float"]:
        raise err.InvalidInstructionTypeError
    data = list(map(float, command[2:]))
    data = sorter(data)
    if command[1] == "int":
        data = list(map(int, data))
    print("Sorted:", *data)

## wrappers
def quickSort(command):      sortData(command, de.quickSort)
def bubbleSort(command):     sortData(command, de.bubbleSort)
def insertionSort(command):  sortData(command, de.insertionSort)

########### FILE HANDLING #####################
def loadFileProcess(command):
    # FIX 4: properly load the file, then enter the interactive file-mode loop
    if len(command) < 2:
        raise err.InvalidInstructionTypeError
    fileName = command[1]
    try:
        labels = de.getLabels(fileName)
    except Exception as e:
        print(f"Error loading file: {e}")
        return
    print(f"Loaded: {fileName}")
    print(f"Columns: {', '.join(labels)}")
    print("Entering file mode. Type 'file.close' to exit.\n")
    while True:
        try:
            raw = input("file> ").strip()
            if not raw:
                continue
            cmd = process(raw)
            if cmd[0] in ["exit", "file.close"]:
                print("Closing file.")
                break
            func = identifyFileCommand(cmd)
            func(fileName, cmd)
        except err.InvalidInstructionTypeError:
            print("Invalid command or arguments. Type 'file.close' to exit.")
        except err.LabelDoesNotExist:
            print("That label does not exist in the file.")
        except Exception as e:
            print(f"Error: {e}")

def identifyFileCommand(command):
    if command[0] in ["exit", "file.close"]:
        sys.exit()
    elif command[0] not in FILE_COMMANDS:
        raise err.InvalidInstructionTypeError
    else:
        whole, label = FILE_COMMANDS[command[0]]
        if command[0] in ["zscore", "percentile"]:
            return whole if len(command) == 2 else label
        return whole if len(command) == 1 else label

def labelStat(file, command):
    stat = command[0]
    special = False
    try:
        num = float(command[1])
        special = True
        label = "".join(command[2:]).capitalize()
    except (ValueError, IndexError):   # FIX 6: specific exception
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
    else:
        raise err.LabelDoesNotExist

def wholeDisplay(fileName, command):
    val = de.fileHandle(fileName)
    labels = de.getLabels(fileName)
    width = 12
    for label in labels:
        print(f"{label:<{width}}", end="")
    print()
    rows = len(val[0])
    cols = len(labels)
    for j in range(rows):
        for i in range(cols):
            print(f"{val[i][j]:<{width}}", end="")
        print()

def labelDisplay(fileName, command):
    val = de.fileHandle(fileName)
    labels = de.getLabels(fileName)
    labels = [label.capitalize() for label in labels]
    label = command[1].capitalize()
    if label not in labels:
        print("Label not found.")
        return
    idx = labels.index(label)
    width = 12
    print(f"{label:<{width}}")
    for v in val[idx]:
        print(f"{v:<{width}}")

FILE_STATS = {
    "mean":       de.meanWhole,
    "median":     de.medianWhole,
    "mode":       de.modeWhole,
    "var":        de.varWhole,
    "std_dev":    de.std_devWhole,
    "min":        de.miniWhole,
    "max":        de.maxiWhole,
    "range":      de.rangeWhole,
    "zscore":     de.zscoreWhole,
    "percentile": de.percentileWhole,
}

def wholeStat(file, command):
    stat = command[0]
    special = False
    try:
        num = float(command[1])
        special = True
    except (ValueError, IndexError):   # FIX 6: specific exception
        pass
    if not special:
        values = FILE_STATS[stat](file)
    else:
        values = FILE_STATS[stat](file, num)
    labels = de.getLabels(file)
    for label, v in zip(labels, values):   # FIX 5: renamed l -> label
        print(f"{label}: {v:.2f}")

FILE_COMMANDS = {
    "mean":       (wholeStat, labelStat),
    "median":     (wholeStat, labelStat),
    "mode":       (wholeStat, labelStat),
    "var":        (wholeStat, labelStat),
    "std_dev":    (wholeStat, labelStat),
    "min":        (wholeStat, labelStat),
    "max":        (wholeStat, labelStat),
    "range":      (wholeStat, labelStat),
    "zscore":     (wholeStat, labelStat),
    "percentile": (wholeStat, labelStat),
    "display":    (wholeDisplay, labelDisplay),
}

COMMANDS = {
    "matmul":        matmul,
    "matadd":        matadd,
    "matsub":        matsub,
    "mean":          meanData,
    "median":        medianData,
    "mode":          modeData,
    "var":           varData,
    "std_dev":       stdData,
    "load":          loadFileProcess,
    "quicksort":     quickSort,
    "bubblesort":    bubbleSort,
    "insertionsort": insertionSort,
    "min":           minimumData,
    "max":           maximumData,
    "range":         rangeData,
    "percentile":    percentileData,
    "zscore":        zscoreData,
}