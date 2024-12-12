plats = []
preus = []

# Preguntar els plats i els preus de cadascun
while len(plats) < 8:
    plat = input("Introdueix el nom d'un plat o escriu $ per acabar: ")
    if plat == "$":
        break
    preu = float(input("Escriu el preu del plat: "))
    if preu <= 0:
        break

    # Elements a les llistes
    plats.append(plat)
    preus.append(preu)

# Mostrar el menú amb estructura i per números
print("Menú")
print("----------")
for i, plat in enumerate(plats, start=1):
    print(f"{i} - {plat} ..... {preus[i - 1]}€")
print("----------")
print("0 - Pagar")

# Ordenar el que es vol dinar
cost_total = 0
escollir = -1  # Inicia amb un valor diferent de 0 per entrar al bucle
while escollir != 0:  # Bucle que es repeteix mentre no es posi 0
    print("Què volen dinar?")
    escollir = int(input("Introdueix l'opció (0 per pagar): "))

    if 0 <= escollir <= len(plats):  # Si escull una opció vàlida o pagar
        if escollir == 0:
            break  # Si es tria pagar, surt del bucle
        cost_total += preus[escollir - 1]
        
    else:
        print("Opció incorrecta, prova de nou.")

# Mostrar el preu final total
print(f"Total cost: {cost_total}€")