# This is a sample Python script.
from QuickSort import quickSort


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

list = [5, 1, 2, 6, 8, 4, 7]

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sortedList = quickSort(list, 0, (len(list) - 1))
    print(sortedList)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
