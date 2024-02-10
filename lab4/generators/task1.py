def squares(N):
    i = 1
    while i <= N:
        yield i*i
        i+=1
        