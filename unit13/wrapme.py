class WrapMe(object):
    def __init__(self,object):
        self.__data = object

    def get(self):
        return self.__data

    def __repr__(self):
        #return '%r'%self.__data
        return repr(self.__data)

    def __str__(self):
        return str(self.__data)

    def __getattr__(self, attr):
        return getattr(self.__data,attr)


wrappedComplex = WrapMe(3.5+4.2j)
print repr(wrappedComplex)
print wrappedComplex.real
print wrappedComplex.imag
print wrappedComplex.get()
print wrappedComplex.conjugate()