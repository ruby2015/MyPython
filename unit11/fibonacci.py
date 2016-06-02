def getFibonacci(num):
    if num==1 or num==2:
        return 1
    else:
        return getFibonacci(num-1)+getFibonacci(num-2)


print getFibonacci(6)

