# shanesully
# Bubble Sort numbers in-place

import sys

def display_commandline_usage_info():
    print("\nUsage:")
    print("\n\t$ python {} $NUMBERS ...\n".format(sys.argv[0]))

def bubble_sort(numbers):

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    
    return numbers

def main():

    if len(sys.argv) <= 1:
        display_commandline_usage_info()
        exit()

    numbers = [int(arg) for arg in sys.argv[1:]]

    print(bubble_sort(numbers))

if __name__ == '__main__':
    main()

