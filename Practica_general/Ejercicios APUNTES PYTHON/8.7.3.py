

def busqueda(cadena,listas):
	tupla = []
	if cadena.isdigit():
		for x in range(len(listas)):
			if cadena == listas[x][1]:
				tupla.append(listas[x])
	else:
		for c in range(len(listas)):
			if cadena in listas[c][0]:
				tupla.append(listas[c])
	for z in tupla:
		print(z)
base = [("Maria carolina ",127),("Moises Maria",126),("Mario Jose",234),("Edwind Moises",126)]
busqueda("126",base)