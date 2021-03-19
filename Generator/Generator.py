def topten():
    n=1
    while n<6:
        sq=n*n
        yield sq
        n += 1


values=topten()
for i in values:
    print(i)