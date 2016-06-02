from time import time,sleep

def timeit(func):
    def _time(*args,**kwargs):
        start = time()
        val = func(*args,**kwargs)
        delta = time()-start
        return delta,val
    return _time

@timeit
def test(sec):
    sleep(sec)


if __name__=="__main__":
    print test(1)






