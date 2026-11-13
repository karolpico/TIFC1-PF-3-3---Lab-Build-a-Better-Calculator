def addmultiplenumbers(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def multiplymultiplenumbers(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def isiteven(num):
    return num % 2 == 0


def isitaninteger(num):
    return num == int(num)


def main():
    print("Calculadora")
    print("1. Sumar varios números")
    print("2. Multiplicar varios números")
    print("3. ¿Es par?")
    print("4. ¿Es entero?")
    opcion = input("Elige una opción (1-4): ")

    if opcion in ("1", "2"):
        numeros = [float(x) for x in input("Escribe los números separados por espacios: ").split()]
        if opcion == "1":
            print("Resultado:", addmultiplenumbers(numeros))
        else:
            print("Resultado:", multiplymultiplenumbers(numeros))
    elif opcion in ("3", "4"):
        num = float(input("Escribe un número: "))
        if opcion == "3":
            print(isiteven(num))
        else:
            print(isitaninteger(num))
    else:
        print("Opción no válida")


if __name__ == "__main__":
    main()