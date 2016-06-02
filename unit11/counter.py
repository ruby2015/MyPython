def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

count = counter(5)
print count.next()
print count.next()
print count.send(10)
print count.next()