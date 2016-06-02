#def bar():
#    return ['abc',[4-2j,'python'],"Guido"]
    #return 'abc',[4-2j,'python'],"Guido"

def foo():
    'foo() -- properly created doc string'
    def bar():
        print 'bar() is called'
    print 'foo() is called'
    bar()

def tupleVarArgs(arg1,arg2='default B',*theRest):
    print 'formal arg1:',arg1
    print 'formal arg2:',arg2
    for eachXtrArg in theRest:
        print 'another arg:',eachXtrArg


#tupleVarArgs('abc',123,'xyz',456.789)
#vals = (1234,12.34,'1234','12.34')

x = 10
def test():
    y = 5
    bar = lambda :x+y
    print bar()
    y =8
    print bar()

def simpleGen():
    yield 1
    yield '2--punch'

from operator import div
