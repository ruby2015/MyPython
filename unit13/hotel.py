class HotelRoomCalc(object):
    'Hotel room rate calculator'
    def __init__(self,rt,sales=0.085,rm=0.1):
        '''HotelRoomCalc default arguments:
                sales tax == 8.5% and room tax == 10%'''
        self.saleTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self,days=1):
        'Calculate total;default to daily rate'
        daily = round((self.roomRate*(1+self.saleTax+self.roomTax)),2)
        return daily*days

sfo = HotelRoomCalc(189,0.086,0.058)
print sfo.calcTotal()