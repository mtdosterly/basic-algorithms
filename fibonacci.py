def fibnaive(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return step(n-1) + step(n-2)

def fibdyn(n):
    if n < 0:
        return "Invalid input"
    elif n <= 1:
        return n
    else:
        fibs = [0,1]
        for num in range (2,n+1):
            fibs.append(fibs[num-2] + fibs[num-1])
        return fibs[n]
