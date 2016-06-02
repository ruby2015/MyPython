import cmath,math
def safe_sqrt(num):
    try:
        result = math.sqrt(num)
    except TypeError:
        result = None
    except ValueError:
        result = cmath.sqrt(num)
    return result

print safe_sqrt(-5)