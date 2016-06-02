def foo():
    global is_this_global
    is_this_global = 'def'
    this_is_local = 'abc'

    print this_is_local,is_this_global



is_this_global = 'xyz'
foo()
print is_this_global