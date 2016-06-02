def reverse_show_str(str):
    if str:
        print str[len(str)-1],
        reverse_show_str(str[:len(str)-1])


reverse_show_str('abc')
print

def cross_show_str(str):
    if str:
        print str[0],
        cross_show_str(str[1:])

cross_show_str('abc')
