#Dades demanades
DNI = input("Escriu el teu DNI sense lletra: ")
preuarticle = float(input("Escriu el preu de l'article comprat: "))
descompte = float(input("Escriu el tant per cent de descompte: "))
IVA = float(input("Escriu el tant per cent d'IVA: "))

#Cálcul de la lletra DNI
lletraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"[int(DNI) % 23]
NIF = DNI + lletraDNI

#Cálcul del preu final
preudescompte = preuarticle - (preuarticle * descompte / 100)
preuIVA = preudescompte + (preudescompte * IVA / 100)

#Resultat pantalla
print("El teu NIF és:", NIF)
print("El preu final és:", preuIVA, "€")

# Tasca realitzada per Shaila Martínez - 2nC SMX