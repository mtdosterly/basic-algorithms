def merge_sort(array,first,last):

    import sys

    if len(array) > 1:
        middle = (first + last)//2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left,0,len(left))
        merge_sort(right,0,len(right))

        left.append(sys.maxsize)
        right.append(sys.maxsize)

        x = y = 0

        for z in range(first,last):
            if left[x] <= right[y]:
                array[z] = left[x]
                x += 1
            else:
                array[z] = right[y]
                y += 1

    return array
