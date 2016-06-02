def convert(func,seq):
    'conv. sequence of numbers to same type'
    return [func(eachnum) for eachnum in seq]

seq = [123,45.67,-6.2e8,99999999999L]

print convert(int,seq)
print convert(float,seq)
print convert(long,seq)