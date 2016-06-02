from operator import add,sub,mul,div
from random import randint,choice

ops = {'+':add,'-':sub,'*':mul,'/':div}
MAXTRIES = 2

def doprob():
    nums =[randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('/')
    if op in '+-*':
        ans = ops[op](*nums)
    else:
        nums = [float(i) for i in nums]
        ans = round(ops[op](*nums),6)
    pr = '%d %s %d='%(nums[0],op,nums[1])
    oops = 0
    while True:
        try:
            if float(raw_input(pr))==float(ans):
                print 'correct'
                break
            elif oops==MAXTRIES:
                print 'answer\n%s%d'%(pr,ans)
                break
            else:
                print 'incorrect...try again'
                oops += 1
        except (KeyboardInterrupt,EOFError,ValueError):
            print 'invalid input...try again'

def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again?[y]').lower()
            if opt and opt[0]=='n':
                break
        except (EOFError,KeyboardInterrupt):
            break

if __name__=='__main__':
    main()