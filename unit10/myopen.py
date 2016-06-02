def myopen(name,mode='r',buffering=-1):
    try:
        file = open(name,mode,buffering)
    except IOError:
        file = None
    return file

print myopen('a')
