from time import ctime

print '***Welcome to MetaClass'
print '\tMetaClass declaration first.'

class MetaClass(type):
    def __init__(cls,name,bases,attrd):
        super(MetaClass,cls).__init__(name,bases,attrd)
        print '***Created class %r at: %s' %(name,ctime())

print '\tClass "Foo" declaration next.'

class Foo(object):
    __metaclass__ = MetaClass
    def __init__(self):
        print '***Instantiated class %r at: %s' %(self.__class__.__name__,ctime())

print '\tClass "Foo" instantiation next'

f = Foo()
print '\tDone'