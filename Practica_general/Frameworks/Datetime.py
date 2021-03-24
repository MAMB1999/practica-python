from datetime import date,datetime
print(datetime.now())  #Imprime la fecha completa
print(datetime.today()) #Imprime la fecha completa
print(date.today()) #Imprime la fecha sin las horas 
print(date(1876,5,7)) #Asigna e imprime la fecha asignada
print(date.fromtimestamp(1526244370)) # Asigna una marca de tiempo que tiene como referencia el 1\1\1970

fecha_hoy = date.today()
print("Hoy ",fecha_hoy.day,"\nMes: ",fecha_hoy.month,"\nAnno:",fecha_hoy.year)

