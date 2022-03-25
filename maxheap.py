# learning source: 
# https://www.programiz.com/dsa/heap-sort#heap 
# https://www.programiz.com/dsa/heap-data-structure
# https://randerson112358.medium.com/lets-build-a-min-heap-4d863cac6521
# https://randerson112358.medium.com/min-heap-deletion-step-by-step-1e05ff9d3932

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
        # print("     swap ", largest, i)
        # after the swap, old arr[i] will be at arr[large]
        heapifyForMax(heapArray, largest)
    return heapArray
    

def buildMaxHeap(array):
    heapArray = array
    n = len(heapArray)
    
    indexOfFirstNonLeaf = n / 2 - 1
    for i in range(indexOfFirstNonLeaf, -1, -1):
        # print(i, "------")
        heapArray = heapifyForMax(heapArray, i)
    return heapArray


def siftUp(heapArray, index):
    parentOfIndex = (index - 1) / 2
    # print(" ///// 1 sift up ", index, parentOfIndex)
    if parentOfIndex >= 0 and heapArray[index] > heapArray[parentOfIndex]:
        swap(heapArray, index, parentOfIndex)
        # print("     swap ", parentOfIndex, index)
        heapArray = siftUp(heapArray, parentOfIndex)
    return heapArray


def maxHeapInsertion(heapArray, element):
    heapArray.append(element)
    heapArray = siftUp(heapArray, len(heapArray) - 1) # sift up starting @ the element we just inserted
    return heapArray
    

def maxHeapDeletion(heapArray, index):
    lastElement = len(heapArray) - 1
    if lastElement == index: heapArray.pop()
    else:
        swap(heapArray, lastElement, index)
        heapArray.pop()
        heapArray = heapifyForMax(heapArray, index) # sift down @ index until it found its place or becomes a leaf node
    return heapArray
    
    
arr1 = list()
str = "24178"
for char in str: arr1.append(int(char))

arr1.append(10)

str = "9356"
for char in str: arr1.append(int(char))
print(arr1)

heapArr1 = buildMaxHeap(arr1)
print(heapArr1)
print(maxHeapInsertion(heapArr1, 11))
print(maxHeapInsertion(heapArr1, 12))
print(maxHeapDeletion(heapArr1, 1))     # remove 10 from the array, which is @ index 1
print(maxHeapDeletion(heapArr1, 10))    # remove 1 from the array, which is @ index 10
print(maxHeapDeletion(heapArr1, 0))     # remove root node
