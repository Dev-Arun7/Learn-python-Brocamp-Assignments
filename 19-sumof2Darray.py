import numpy as np

class ArrayAdder:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.array1 = np.zeros((rows, cols), dtype=int)
        self.array2 = np.zeros((rows, cols), dtype=int)
        self.result_array = np.zeros((rows, cols), dtype=int)

    def getArray(self):
        print("Enter the values of array1 : ")
        for i in range(self.rows):
             for j in range(self.cols):
                value=int(input())
                self.array1[i][j]=value
        print("Enter the values of array2 : ")
        for i in range(self.rows):
             for j in range(self.cols):
                value=int(input())
                self.array2[i][j]=value

    def addArray(self):
        self.result_array = self.array1 + self.array2

    def displayArray(self, array):
        print("Array values:")
        print(array)

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    array_adder = ArrayAdder(rows, cols)

    array_adder.getArray()
    array_adder.addArray()

    print("Array 1:")
    array_adder.displayArray(array_adder.array1)

    print("Array 2:")
    array_adder.displayArray(array_adder.array2)

    print("Result Array:")
    array_adder.displayArray(array_adder.result_array)


if __name__ == "__main__":
    main()
