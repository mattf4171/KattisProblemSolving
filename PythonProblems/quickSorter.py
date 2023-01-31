"""
Matthew Fernandez

"""

class solution:

    def swap(self, a, b):
        temp = a
        b = a 
        a = temp
        return a,b

    def partition(self, array, low, high):
        
        pivot = array[high]
        i = low - 1
        for j in range(low, high,1):
            if array[j] <= pivot:
                i += 1
                (array[i], array[j]) = (array[j], array[i])

        (array[i + 1], array[high]) = (array[high], array[i + 1])

        return i + 1

    def quickSort(self, array, low, high):
        # print(array, low, high)
        if low < high :
            pivot_location = self.partition(array, low, high)
            self.quickSort(array, low, pivot_location - 1)
            self.quickSort(array, pivot_location + 1, high)


if __name__ == "__main__":
    
    array = input()
    new_array = []
    for i in array:
        new_array.append(i)
    low = 0
    high = len(new_array) - 1
    method = solution()
    method.quickSort( [new_array][0], low, high)
    print(new_array)

"""
Input: 

21437698


Output:

"""