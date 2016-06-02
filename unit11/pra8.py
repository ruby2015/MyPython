def isLeap(year):
    return (year%4 == 0 and (year%100 != 0 or year%400 == 0))

print filter(isLeap,range(2000,2020))
print [i for i in range(2000,2020) if isLeap(i)]