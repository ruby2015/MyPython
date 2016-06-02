from time import ctime,sleep

def tsfunc(func):
    def wrappedFunc():
        print '%s %s'%(ctime(),func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    print 'mark'

foo()
sleep(4)

for i in range(5):
    sleep(1)
    foo()