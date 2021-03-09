
persona = str(input("Por favor, ingresa tu nombre:\n>>"))
empleado = int(input("Por favor,ingresa el numero de empleados.\n>>"))
llegados = str(input("Por favor, ingresa el numero de llegados\n>>"))
llegados = llegados.split(" ")
llegados.append(persona) 
llegados = sorted(llegados)
lista = []
con,con2 = 0,0
while con < len(llegados):
    lista.append([])
    for z in range(empleado):
        if len(llegados) > con:
            lista[con2].append(llegados[con])
            con +=1
        else:
            break        
    con2 += 1
for x in range(len(lista)):
    if persona in lista[x]:
        print((x+1)*20)