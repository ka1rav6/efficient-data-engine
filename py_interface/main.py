import data_engine as de
import inputProcessing as ip
import sys
# nums = [5, 2, 8, 1, 3]

# print(de.insertionSort(nums))

while True:
    command = input()
    command = ip.process(command)
    if command == "exit":
        sys.exit(0)
    print(command[0])
    if not ip.isLoad(command):
        func= ip.identify(command)
        func(command)

    # else: #FILE MODE
    #     file_name = input("Enter file name: ")

    #     while True:
    #         sub_command = input()