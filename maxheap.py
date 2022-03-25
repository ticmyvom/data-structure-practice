# learning source: https://www.programiz.com/dsa/heap-sort#heap and https://www.programiz.com/dsa/heap-data-structure

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def heapifyForMax(heapArray, i):
    n = len(heapArray)
    largest = i
    leftChildIndex = 2*i + 1
    rightChildIndex = 2*i + 2
    
    # if left and right children's indices are valid and either of them > largest
    if (leftChildIndex < n and heapArray[leftChildIndex] > heapArray[largest]):
        largest = leftChildIndex
    if rightChildIndex < n:
        if heapArray[rightChildIndex] > heapArray[largest]:
            largest = rightChildIndex
    
    # do the swap and heapify recursively on i until it's at its proper place
    if largest != i:
        swap (heapArray, largest, i)
        print("     swap ", largest, i)
        # after the swap, old arr[i] will be at index largest
        heapifyForMax(heapArray, largest)
    
    return heapArray
    

def buildMaxHeap(array):
    heapArray = array
    n = len(heapArray)
    
    indexOfFirstNonLeaf = n / 2 - 1
    for i in range(indexOfFirstNonLeaf, -1, -1):
        print(i, "------")
        heapArray = heapifyForMax(heapArray, i)
    
    return heapArray

arr1 = list()
str = "24178"
for char in str: arr1.append(int(char))

arr1.append(10)

str = "9356"
for char in str: arr1.append(int(char))
print(arr1)

print(buildMaxHeap(arr1))

