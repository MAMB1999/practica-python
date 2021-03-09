
persona = "Zebediaj"
empleado = 5
llegados = "Bob jim becky Pat"
llegados = llegados.split(" ")
llegados.append(persona)
llegados = sorted(llegados)
lista = []
contador = 0
for z in range(empleado):
    lista.append([])
    for x in range(empleado):
        if contador >= len(llegados):
           continue
        else: 
            lista[z].append(llegados[contador])
            contador += 1

for w in range(len(lista)):
    for x in range(len(lista[w])):
        if lista[w][x] == persona:
            print(lista[w].index(persona)*20)