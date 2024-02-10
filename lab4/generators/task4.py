def squares(N):
    i = 1
    while i < N:
        yield i*i
        i+=1
gener = squares(int(input()))
for x in gener:
    print(x, end =' ')