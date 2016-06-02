def safe_float(object):
    try:
        retval = float(object)
    except (ValueError,TypeError), e:
        retval = str(e)
    return retval

#try:
#   assert 0==1,'One does not equal zero silly'
#except AssertionError, e:
#   print '%s:%s'%(e.__class__.__name__,e)
def assertnew(expr,args=None):
    if __debug__ and not expr:
        raise AssertionError,args

try:
    assertnew(0==1,'one does not equal zero silly')
except AssertionError,e:
    print '%s:%s'%(e.__class__.__name__,e)
