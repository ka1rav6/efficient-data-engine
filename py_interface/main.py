import data_engine as de
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
clearScreen()

while True:
    command = input(">>>> ")
    command = ip.process(command)
    if command[0] == "exit":
        sys.exit(0)
    elif command[0] == "cls" or command[0] == "clear":
        clearScreen()
        continue
    func= ip.identify(command)
    func(command)
