class RoundFloatManual(object):
    def __init__(self,val):
        assert isinstance(val,float),'Value must be a float!'
        self.value = round(val,2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__


f = RoundFloatManual(3.425343)
print f
print repr(f)