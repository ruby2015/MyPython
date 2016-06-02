def dollarize(val):
    try:
        val = float(val)
    except ValueError,e:
        raise TypeError,'val must be a float'
    else:
        s = '$' if val>0 else '-$'
        val = abs(val)
        l = []
        while val:
            l.append(str(val%1000))
            val = int(val/1000)
        l.reverse()
        return s+','.join(l)

class MoneyFmt(object):

    def __init__(self,val,opt=True):
        try:
            self.__money = float(val)
        except ValueError,e:
            raise TypeError,'val must be a float'
        self.__opt = opt

    def update(self,val):
        try:
            self.__money = float(val)
        except ValueError,e:
            raise TypeError,'val must be a float'

    def __nonzero__(self):
        return bool(self.__money)

    def __repr__(self):
        return "%.2f"%self.__money

    def __str__(self):
        if self.__money>=0:
            s = '$'
        elif self.__opt:
            s = '-$'
        else:
            s = '<->$'
        val = abs(self.__money)
        l = []
        while val:
            l.append(str(val%1000))
            val = int(val/1000)
        if l:
            l[0] = "%.2f" % float(l[0])
            l.reverse()
            return s+','.join(l)
        else:
            return s+"%.2f" % val

a = MoneyFmt('12345565765.8901',False)
print a
a.update('-2314343')
print a
a.update(0)
print a
print bool(a)
