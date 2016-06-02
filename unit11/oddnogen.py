from random import randint

#def odd(num):
#    return num%2

#allnums = []
#for i in range(9):
#    allnums.append(randint(1,99))
#print filter(odd,allnums)
#print filter(lambda n:n%2,allnums)
#print [n for n in allnums if n%2]
#print [n for n in [randint(1,99) for i in range(9)] if n%2]
print reduce(lambda x,y:x*y,range(1,6)) #5!
