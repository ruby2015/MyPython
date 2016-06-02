def testit(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True,retval)
    except Exception,diag:
        result = (False,diag)
    return result

def test():
    funcs = [int,long,float]
    vals = (1234,12.34,'1234','12.34')
    for func in funcs:
        print '_'*20
        for val in vals:
            retval = testit(func,val)
            if retval[0]:
                print '%s(%r)='%(func.__name__,val),retval[1]
            else:
                print '%s(%r)=Failed:'%(func.__name__,val),retval[1]

if __name__=='__main__':
    test()
