print("Bienvenido a la calculadora de python")
print("")
print("NOTA: ingresar un numero distinto a los del menu causara el ciere del programa")
print("")
op = 1

while (op >0 and op <6):
    print("1) SUMAR")
    print("2) RESTAR")
    print("3) MULTIPLICAR")
    print("4) DIVIDIR")
    print("5) ELEVAR")
    print("6) SALIR")

    op = int(input("Selecione Opcion: \n"))

    if (op == 1):
        x = float(input("Ingrese el primer numero: \n"))
        y = float(input("Ingrese el segundo numero: \n"))
        print("La Suma es: ", x + y)
        print("")


    elif (op == 2):
        x = float(input("Ingrese el primer numero: \n"))
        y = float(input("Ingrese el segundo numero: \n"))
        print("La Resta es:", x - y)
        print("")


    elif (op == 3):
        x = float(input("Ingrese el primer numero: \n"))
        y = float(input("Ingrese el segundo numero: \n"))
        print("La Multiplicacion es:", x * y)
        print("")


    elif (op == 4):
        x = float(input("Ingrese Numero: \n"))
        y = float(input("Ingrese Divisor: \n"))
        try:
            print("La Division es:", x/y)
            print("")

        except ZeroDivisionError:
            print("No se Permite la Division Entre 0")

    elif (op == 5):
        x = float(input("Ingrese el numero: \n"))
        y = float(input("Ingrese potencia: \n"))
        print("El resultado es: " , round(pow(x,y)))

    elif (op == 6):
        break
