from re import *
num_tlf = compile(r'\d\d\d\d\d\d\d\d\d\d')
mo = num_tlf.search('Mi numero de celular es 1173645036')
if mo:
    print(f'Numero de telefono: {mo.group()}')
else:
    print('Numero no encontrado.')