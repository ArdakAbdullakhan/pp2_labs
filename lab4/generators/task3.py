def divided(n):
    i = 0
    while i <=n:
        if(i%12 == 0):
            yield i
        i+=1

by_three_and_for = divided(int(input()))
for x in by_three_and_for:
    print(x, end = ' ')
