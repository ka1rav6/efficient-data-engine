import data_engine as de # type: ignore   ## to ignore the warning error 
import inputProcessing as ip
import sys

import os
import platform

def clearScreen():
    """Clear the terminal screen in a cross-platform way."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
def displayCommands():
    NormalCommandDict = {
        "load": "Enter file mode and load a CSV file",
        "exit": "To close the engine",
        "mean data": "Calculate the mean of the data",
        "median data": "Calculate the median of the data",
        "mode data": "Calculate the mode of the data",
        "var data": "Calculate the variance of the data",
        "std_dev data": "Calculate the standard deviation of the data",

        "zscore val data": "Calculate the z-score of a value relative to the data",
        "percentile val data": "Calculate the percentile of a value in the data",

        "min data": "Find the minimum value in the data",
        "max data": "Find the maximum value in the data",
        "range data": "Calculate the range of the data",

        "matmul datatype number_of_matrices": "Multiply multiple matrices of the given datatype",

        "quicksort datatype data": "Sort the data using Quick Sort",
        "insertionsort datatype data": "Sort the data using Insertion Sort",
        "bubblesort datatype data": "Sort the data using Bubble Sort",

        "clear OR cls": "Clear the screen",
        "help": "Display the list of available commands"
    }
    FileCommandDict = {
        "mean": "Calculate the mean for all labels in the loaded file",
        "mean label": "Calculate the mean of a specific label",

        "median": "Calculate the median for all labels in the loaded file",
        "median label": "Calculate the median of a specific label",

        "mode": "Calculate the mode for all labels in the loaded file",
        "mode label": "Calculate the mode of a specific label",

        "var": "Calculate the variance for all labels",
        "var label": "Calculate the variance of a specific label",

        "std_dev": "Calculate the standard deviation for all labels",
        "std_dev label": "Calculate the standard deviation of a specific label",

        "min": "Find the minimum for all labels",
        "min label": "Find the minimum of a specific label",

        "max": "Find the maximum for all labels",
        "max label": "Find the maximum of a specific label",

        "range": "Calculate the range for all labels",
        "range label": "Calculate the range of a specific label",

        "display": "Display the entire dataset",
        "display label": "Display a specific column",

        "file.close": "Close the file and exit"
    }
    print("In normal mode: ")
    for k,v in NormalCommandDict.items():
        print(f"{k}: {v}")
        print()
    print("In file mode:")
    for k,v in FileCommandDict.items():
        print(f"{k}: {v}")
        print()

        
clearScreen()

while True:
    command = input(">>>> ")
    command = ip.process(command)
    if command[0] == "exit":
        sys.exit(0)
    elif command[0] == "help":
        displayCommands()
        continue
    elif command[0] == "cls" or command[0] == "clear":
        clearScreen()
        continue
    func= ip.identify(command)
    func(command)
