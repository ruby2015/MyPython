class NumStr(object):
    def __init__(self,num=0,str=""):
        self.__num = num
        self.__string = str

    def __str__(self):
        return "[%d::%s]" % (self.__num,self.__string)

    __repr__ = __str__

    def __add__(self, other):
        if isinstance(other,NumStr):
            return self.__class__(self.__num+other.__num,self.__string+other.__string)
        else:
            raise TypeError,\
        "Illegal argument type for built-in operation"

    def __mul__(self, num):
        if isinstance(num,int):
            return self.__class__(self.__num*num,self.__string*num)
        else:
            raise TypeError,\
        "Illegal argument type for built-in operation"

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __norm_cval(self,cmpres):
        return cmp(cmpres,0)

    def __cmp__(self, other):
        return self.__norm_cval(cmp(self.__num,other.__num))+\
            self.__norm_cval(cmp(self.__string,other.__string))


a = NumStr(3,'foo')
b = NumStr(3,'goo')
c = NumStr(2,'foo')
d = NumStr()
e = NumStr(str='boo')
f = NumStr(1)
print a
print a<b
print b<c
print a==a
print b*2
print b+e
print cmp(a,b)
print bool(d)



