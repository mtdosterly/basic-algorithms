def fibnaive(n):
    """worst way to do it"""
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibnaive(n-1) + fibnaive(n-2)

def fibdyn(n):
    """better, but more time consuming to append to the list than just work within a list of predetermined size"""
    if n < 0:
        return "Invalid input"
    elif n <= 1:
        return n
    else:
        fibs = [0,1]
        for num in range (2,n+1):
            fibs.append(fibs[num-2] + fibs[num-1])
        return fibs[n]

def fib(len):
    """optimal"""
    lst = [0]*len
    lst[1] = 1
    for x in range(2,len):
        lst[x] = lst[x-1] + lst[x-2]
    return lst[len-1]
