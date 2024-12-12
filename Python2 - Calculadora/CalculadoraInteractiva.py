while True:
    # Demanar el primer número
    num1 = float(input("Introdueix el primer número: "))

    # Demanar el segon número
    num2 = float(input("Introdueix el segon número: "))

    # Preguntar quina operació es vol fer
    operacio = input("Quina operació vols fer? (+, -, *, /, %): ")

    # Càlcul operació
    # Suma
    if operacio == "+":
        resultat = num1 + num2
        # Surt
        break

    # Resta
    elif operacio == "-":
        resultat = num1 - num2
        break

    # Multiplicació
    elif operacio == "*":
        resultat = num1 * num2
        break

    # Divisió
    elif operacio == "/":
        if num2 != 0:
            resultat = num1 / num2
            break
        else:
            print("Error: no es pot dividir entre zero")
            continue  # Permet tornar a demanar els números

    # Mòdul
    elif operacio == "%":
        if num2 != 0:
            resultat = num1 % num2
            break
        else:
            print("Error: no es pot dividir entre zero")
            continue  # Permet tornar a demanar els números
    else:
        print("Error: operació no vàlida")
        continue  # Permet tornar a demanar els números

# Mostrar el resultat
print("El resultat és:", resultat)

# Tasca realitzada per Shaila Martínez - 2nC SMX