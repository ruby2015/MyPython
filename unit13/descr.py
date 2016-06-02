import os
import pickle

class FileDecsr(object):
    saved = []

    def __init__(self,name=None):
        self.name = name

    def __get__(self, obj,typ=None):
        if self.name not in FileDecsr.saved:
            raise AttributeError,\
        '%r used before assignment' % self.name

        try:
            f = open(self.name,'r')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError,IOError,EOFError,AttributeError,ImportError,IndexError),e:
            raise AttributeError,\
        'could not read %r: %s' % self.name

    def __set__(self, obj, val):
        f = open(self.name,'w')
        try:
            try:
                pickle.dump(val,f)
                FileDecsr.saved.append(self.name)
            except (TypeError,pickle.PicklingError),e:
                raise AttributeError,\
            'could not pickle %r' % self.name
        finally:
            f.close()

    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDecsr.saved.remove(self.name)
        except (OSError,ValueError),e:
            pass

class MyFileVarClass(object):
    foo = FileDecsr('foo')
    bar = FileDecsr('bar')

fvc = MyFileVarClass()
#print fvc.foo
fvc.foo = 42
fvc.bar = 'leanna'
print fvc.foo,fvc.bar
del fvc.foo
#print fvc.foo,fvc.bar
fvc.foo = __builtins__