def safe_input(str):
    try:
        var = raw_input(str)
    except (EOFError,KeyboardInterrupt):
        var = None
    return var

print safe_input('Please enter string: ')