from spy_game import spy_game
from heads_and_legs import solve
n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(spy_game(numbers))

inp = input()
x, y = map(int, inp.split())
solve(x, y)