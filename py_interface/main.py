import data_engine as de
import inputProcessing as ip
# nums = [5, 2, 8, 1, 3]

# print(de.insertionSort(nums))

while True:
    command = input()
    ip.process(command)
    if ip.is_Normal(command):
        pass

    else: #FILE MODE
        file_name = input("Enter file name: ")

        while True:
            sub_command = input()