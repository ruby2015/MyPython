#!/usr/bin/env python
dash = '\n'+'_'*50

exec_dic = {
    'f':"""
for %s in %s:
    print %s
    """,
    'n':"""
%s = %d
while %s<%d:
    print %s
    %s = %s + %d
    """,
    's':"""
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s = %s + 1
    """
}

def main():
    ltype = raw_input('Please enter the loop type(For/While)')[0].lower()
    dtype = raw_input('Please enter the data type(Sequence/Number)')[0].lower()

    if dtype == 'n':
        start = input('Please enter the start number: ')
        end = input('Please enter the end number: ')
        step = input('Please enter the step: ')
        sequence = str(range(start,end,step))
    elif dtype == 's':
        sequence = '"'+raw_input("Please enter the sequence: ")+'"'

    var = raw_input('Please enter the iterative variable name: ')

    if ltype == 'f':
        exec_str = exec_dic['f'] % (var,sequence,var)
    elif ltype == 'w':
        if dtype == 'n':
            exec_str = exec_dic['n'] % (var,start,var,end,var,var,var,step)
        elif dtype == 's':
            svar = raw_input("Please enter the sequence name: ")
            exec_str = exec_dic['s'] % (var,svar,sequence,var,svar,svar,var,var,var)

    print dash
    print "Your customed generated code: "+dash
    print exec_str + dash
    print "Test execution of your code"+dash
    exec exec_str
    print dash


if __name__ == '__main__':
    main()