def busqueda(cadena,listas):
	tupla = []
	if cadena.isdigit():
		x = 1
	else:
		x = 0
	for z in range(len(listas)):
		if cadena in listas[z][x]:
			tupla.append(listas[z])
	for w in tupla:
			print(w)
			
base = [("Maria carolina ",127),("Moises Maria",126),("Mario Jose",234),("Edwind Moises",126)]
busqueda("Maria",base)
			