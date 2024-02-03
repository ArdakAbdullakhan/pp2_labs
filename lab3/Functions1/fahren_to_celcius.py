def fahrengeit_to_celcius(F):
    C = (5 / 9) * (F - 32)
    return C

F = float(input())
print(fahrengeit_to_celcius(F))