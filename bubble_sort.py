# shanesully
# Bubble Sort numbers in-place

import sys

def bubble_sort(numbers):

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    
    return numbers

def main():
    numbers = [int(x) for x in sys.argv[1:]]

    print bubble_sort(numbers)

if __name__ == '__main__':
    main()

