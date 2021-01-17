def merge_sort(array):

    import sys

    if len(array) > 1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        left.append(sys.maxsize)
        right.append(sys.maxsize)

        x = y = 0

        for z in range(0,len(array)):
            if left[x] <= right[y]:
                array[z] = left[x]
                x += 1
            else:
                array[z] = right[y]
                y += 1

    return array
