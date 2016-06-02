class CapOpen(object):
    def __init__(self,fn,mode='r',buff=-1):
        self.f = open(fn,mode,buff)

    def __repr__(self):
        return repr(self.f)

    def __str__(self):
        return str(self.f)

    def write(self,line):
        self.f.write(line.upper())

    def __getattr__(self, item):
        return getattr(self.f,item)

    def get(self):
        return self.f

f = CapOpen('test','w')
f.write('faye is good\n')
f.write('at delegating\n')
f.close()
f = CapOpen('test')
for eachline in f.get():
    print eachline,