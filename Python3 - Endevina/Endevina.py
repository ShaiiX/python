import random

# Indiquem el número random i intents desde 0
numero = random.randint(1, 100)
attempts = 0

while attempts < 5:
    # Preguntem a l'usuari i sumem 1 intent
    usuari = int(input("Quin número he pensat? "))
    attempts += 1

    # Si encerta el número surt del bucle
    if usuari == numero:
        print(f"Has encertat en {attempts} intents.")

    # Si el número és més petit que el que l'usuari ha dit
    elif usuari > numero:
        print("És més petit")

    # Si el número és més gran que el que l'usuari ha dit
    else:
        print("És més gran")
    
    # Si arriba a 5 intents indica quina era la resposta correcta
    if attempts == 5:
        print("No l'has encertat, el número era " + str(numero))

# Tasca realitzada per Shaila Martínez - 2nC SMX