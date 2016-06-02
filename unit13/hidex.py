class HideX(object):
    def __init__(self,x):
        self.x = x

        @property
        def x():
            def fget(self):
                return ~self.__x

            def fset(self,x):
                assert isinstance(x,int),'"x" must be an integer!'
                self.__x = ~x

            return locals()

inst = HideX(10)
print inst.x
inst.x = 30
print inst.x