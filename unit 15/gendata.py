from random import randint,choice
from string import lowercase
from time import ctime
from math import pow
import re

doms = ("com","edu","net","org","gov")

for i in range(randint(5,10)):
    dtint = randint(0,pow(2,31)-2)
    timestr = ctime(dtint)

    shorter = randint(4,7)
    em = ""
    for j in range(shorter):
        em += choice(lowercase)

    longer = randint(shorter,12)
    dn = ""
    for j in range(longer):
        dn += choice(lowercase)

    str = '%s::%s@%s.%s::%d-%d-%d' % \
          (timestr,em,dn,choice(doms),dtint,shorter,longer)
    #print re.match(r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)',str).group()
    print re.match(r'^(\w{3})',str).group()