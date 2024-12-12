import random

# Generar dos números randoms
num1 = random.randint(0, 100)
num2 = random.randint(0, 100)

# Generar operacions randoms
operacions = ["+", "-", "*", "/"]
operacio = random.choice(operacions)

# Càlcul resultat operació
# Suma
if operacio == "+":
    resultat = num1 + num2

# Resa
elif operacio == "-":
    resultat = num1 - num2

# Multiplicació
elif operacio == "*":
    resultat = num1 * num2

# Divisió
elif operacio == "/":
    resultat = num1 // num2     
        # Es posen // dues barres per indicar que ha de ser divisió entera

# Preguntar resposta de l'usuari
resposta = int(input(f"Quin és el resultat de {num1} {operacio} {num2}? "))

#Comprovació de la resposta
if resposta == resultat:
    print("Correcte")
else:
    print(f"Error: El resultat correcte era {resultat}.")

#Tasca realitzada per Shaila Martínez - 2nC SMX