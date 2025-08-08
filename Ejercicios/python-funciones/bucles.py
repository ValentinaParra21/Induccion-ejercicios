nombres = input("Ingresa los nombres de quien compro de la rifa: ")
contador = 0

for letra in nombres:
    if letra == "a" or letra == "A":
        contador += 1

print(f"La letra 'r' aparece {contador} veces en los nombres.")
