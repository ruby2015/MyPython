class P(object):
    'class P'
    def __init__(self):
        print 'created an instance of',self.__class__.__name__

    def foo(self):
        print 'Hi,i am P-foo'

class C(P):
    def foo(self):
        super(C,self).foo()
        #P.foo(self)
        print 'Hi,i am C-foo'

class D(C):
    pass

d = D()
print isinstance(d,P)

#c = C()
#c.foo()
class RoundFloat(float):
    def __new__(cls, val):
        #return super(RoundFloat,cls).__new__(cls,round(val,2))
        return float.__new__(cls,round(val,2))


#print RoundFloat(3.1414)

class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict,self).keys())

d = SortedKeyDict((('zheng-cai',67),('hui-jun',68),('xin-yi',2)))
#print 'By iterator: '.ljust(12),[i for i in d]
#print 'By keys:'.ljust(12),d.keys()
