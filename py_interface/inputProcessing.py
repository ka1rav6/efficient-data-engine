import data_engine as de
import errorHandling as err
def process(command):
    command = command.strip().split()
    for i in range(len(command)):
        command[i] = command[i].strip().lower()
def matmul(command):
    matrices = int(command[2])
    final =[]
    r = int(input(f"Enter number of rows of the matrices: "))
    c = int(input(f"Enter number of coloums of the matrices: "))
    for i in range(matrices):
        temp = []
        for j in range(r):
            while True:
                try:
                    tempRow = list(map(int, input(f"Enter row {i}").strip().split()))
                    break
                except:
                    print("Please enter valid input")
            if len(tempRow) != c:
                raise err.MatrixInputInconsistencyError("Cannot Have different column lengths")
            temp.append(tempRow)
        de.matrixMultiply(final, temp)

def is_Normal(command):
    return command == "load"
def identify(command):
    if (command[0]== 'matmul'):
        return matmul

