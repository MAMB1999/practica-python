def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

txt = int(input("Ingrese numero:"))
for x in range(txt):
    print(fibonacci(x))