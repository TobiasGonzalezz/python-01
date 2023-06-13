welcome_message = "Bienvenido a mi calculadora \nPara salir solo escribe Salir \nLas operaciones son suma, resta, multi y div"
print(welcome_message)

result = ""

while True:
    if not result:
        result = input('Ingresa el primer numero: ')
        if result.lower() == "salir":
            break
        result = int(result)
    op = input("Ingresa el operador: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op == "suma":
        result += n2
    elif op == "resta":
        result -= n2
    elif op == "multi":
        result *= n2
    elif op == "div":
        result /= n2
    else:
        print("Eso no se puede hacer")
        break
    print(f"El resultado es {result}")


# Primer intento
# n1 = input("Ingresa numero: ")
# operator = input("Ingresa el operador: ")
# n2 = input("Ingresa siguiente numero: ")

# n1 = int(n1)
# n2 = int(n2)

# suma = n1 + n2
# resta = n1 - n2
# multi = n1 * n2
# div = n1 / n2

# while n1 or operator or n2 != "salir":
#     if operator == "suma":
#         print("resultado", suma)
#     elif operator == "resta":
#         print("resultado", resta)
#     elif operator == "multi":
#         print("resultado", multi)
#     elif operator == "div":
#         print("resultado", div)
#     if n1 or operator or n2 == "salir":
#         print("Calculadora Finalizada")
#         break
