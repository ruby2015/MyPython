class AddrBookEntry(object):
    'address book entry class'
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print 'Created instance for: ',self.name

    def updatePhone(self,newph):
        self.phone = newph
        print 'Updated phone for: ',self.name


var = AddrBookEntry('ruby','111')
var.updatePhone('333')
print var.phone