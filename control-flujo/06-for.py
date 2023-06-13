buscar = 10
# for numero in range(5):
#     print(numero, numero * 'hola mundo')
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado:", buscar)
        break
else:
    print("no encontre el numero buscado")

for char in "Ultimate Phyton":
    print(char)
