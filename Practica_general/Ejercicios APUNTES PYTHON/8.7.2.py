x = [1,3,7,6,4,9,14,5]
def ordenar(lis2):
	lista_organizada = []
	for x in range(len(lis2)):
		index = lis2.pop(lis2.index(min(lis2)))
		lista_organizada.append(index)
		
	
	print(lista_organizada)
	
ordenar(x)
	