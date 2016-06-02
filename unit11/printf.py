def printf(pattern,*args):
    print pattern%args

pattern = 'a=%s,b=%s'
printf(pattern,3,4)