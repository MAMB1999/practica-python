def fibonacci(n):
    #Caso Base.
    if n < 2:
        return n
    #F = F-1 + F-2 (Recursividad jejx)
    return fibonacci(n-1)+fibonacci(n-2)

txt = int(input("Ingrese numero:"))
#Rango del numero ingresado
for x in range(txt):
    print(fibonacci(x))