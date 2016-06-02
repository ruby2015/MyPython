def average(*numbers):
    return reduce(lambda x,y:float(x+y),numbers)/len(numbers)

print average(1,2,3,4,5,6,7)