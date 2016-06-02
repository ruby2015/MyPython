from time import time

def timeit(func):
    def _time(*args,**kwargs):
        start = time()
        val = func(*args,**kwargs)
        delta = time()-start
        return delta,val
    return _time


def mult(x,y):
    return x*y

@timeit
def factorial1(num):
    return reduce(mult,range(1,num+1))

@timeit
def factorial2(num):
    return reduce(lambda x,y:x*y,range(1,num+1))


def factorial3(num):
    if num==1:
        return 1
    else:
        return num*factorial3(num-1)

@timeit
def factorial(num):
    return factorial3(num)

if __name__=="__main__":
    print factorial1(100)
    print factorial2(100)
    print factorial(100)
