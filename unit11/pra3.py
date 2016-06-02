def max2(num1,num2):
    return num1 if num1>num2 else num2

def min2(num1,num2):
    return num1 if num1<num2 else num2

def my_max(*args):
    return reduce(max2,args)

def my_min(*args):
    return reduce(min2,args)

str = "abcdef"
nums = [1,2,3,4,5]
print my_min(*nums)
print my_max(1,2,3,4,5)

