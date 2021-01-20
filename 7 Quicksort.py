def quicksort(array,left,right):

    def partition(array,left,right):

        pivot = array[right]
        i = left - 1

        for num in range(left,right):
            if array[num] <= pivot:
                i += 1
                array[i],array[num] = array[num],array[i]
        array[i+1],array[right] = array[right],array[i+1]
        return i + 1

    if left < right:
        pivot = partition(array,left,right)
        quicksort(array,left,pivot-1)
        quicksort(array,pivot+1,right)

    return array
