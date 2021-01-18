def build_max_heap(array):

    def max_heapify(array,index):

        left = 2*(index) + 1
        right = 2*(index) + 2

        if left <= (len(array)-1) and array[left] > array[index]:
            largest = left
        else:
            largest = index

        if right <= (len(array)-1) and array[right] > array[largest]:
            largest = right

        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            max_heapify(array, largest)

    i = len(array)//2

    while i >= 0:
        max_heapify(array, i)
        i -= 1
    return array
