def even_nums(n):
    i = 0
    while i <=n:
        if(i%2 == 0):
            yield i
        i+=1

even = even_nums(int(input()))
for x in even:
    print(x, end = ' ')
