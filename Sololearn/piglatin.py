datos = "Hola mundo"

def pig(input):
    input = list(input)
    palabra = input.pop(0)
    input = "".join(input)+palabra+"ay"
    return input.lower()  
datos = datos.split(" ")
res = list(map(pig,datos))
print(" ".join)