def heapsort(array):

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

    def build_max_heap(array):

        i = len(array)//2

        while i >= 0:
            max_heapify(array,i,len(array)-1)
            i -= 1

    size = len(array)-1

    build_max_heap(array)

    for i in range(size,-1,-1):
        array[0],array[i] = array[i],array[0]
        size -= 1
        max_heapify(array,0,size)

    return array
