def fromNto0(N):

    while N>=0:
        yield N
        N-=1

gener = fromNto0(int(input()))
for num in gener:
    print(num, end=' ')
        