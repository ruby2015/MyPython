j,k = 1,2
output = "j==%d and k==%d"

def proc1():
    j,k = 3,4
    print output%(j,k)
    k = 5

def proc2():
    j = 6
    proc1()
    print output%(j,k)

k = 7
proc1()
print output%(j,k)

j = 8
proc2()
print output%(j,k)