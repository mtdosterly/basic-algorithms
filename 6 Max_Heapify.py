def build_max_heap(array):

    def max_heapify(array,index,size):

        left = 2*(index) + 1
        right = 2*(index) + 2

        if left <= size and array[left] > array[index]:
            largest = left
        else:
            largest = index

        if right <= size and array[right] > array[largest]:
            largest = right

        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            max_heapify(array,largest,size)

    i = len(array)//2

    while i >= 0:
        max_heapify(array,i,len(array)-1)
        i -= 1
    return array
