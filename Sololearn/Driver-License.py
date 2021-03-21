
class Driver_license():
    def __init__(self,persona,empleado,llegados):
        self.persona = persona
        self.empleado = empleado
        self.llegados = llegados
        self.llegados = self.llegados.split(",")
        self.llegados.append(self.persona) 
        self.llegados = sorted(self.llegados)
        self.lista = []
    def __str__(self):
        frase = """Driver license 1.1\n\n
            El programa tomara un numero de datos como:
            \nTu nombre.\n
            Numero de empleados.\n
            Numero de llegados.\n
            Y calculara el tiempo que te tomara\n
            en sacar tu licencia de conducir por orden alfabetico."""
        return frase
    def iterar_listas(self):
        con,con2 = 0,0
        while con < len(self.llegados):
            self.lista.append([])
            for z in range(self.empleado):
                if len(self.llegados) > con:
                    self.lista[con2].append(self.llegados[con])
                    con +=1
                    break 
            print(self.lista)
            con2 += 1
    def resultado_bucle(self):
        self.iterar_listas()
        for x in range(len(self.lista)):
            if self.persona in self.lista[x]:
                print((x+1)*20)

A = Driver_license(persona="",empleado = "",llegados = "")
print(A)
end = ""
    while not end == "Finalizar" :
        try:
            persona = "Ing"
