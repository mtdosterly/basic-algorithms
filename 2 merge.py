def merge(array,p,q,r):

    import sys

    n1 = q - p + 1
    n2 = r - q
    left = right = []

    for i in range (0,n1):
        left.append(array[p+i-1])

    for j in range(0,n2):
        right.append(array[q + j])

    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i = j = 1

    for k in range(p,r):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j +=1

    return array
