edad = int(input("¿Cuál es tu edad? "))

if edad >= 13:
    tiene_consola = input("¿Tienes consola para jugar? (s/n): ").lower()
    if tiene_consola == "s":
        print("Puedes jugar el torneo ")
    else:
        print("Tienes la edad, pero necesitas una consola para participar.")
else:
    print(" debes tener al menos 13 años para participar en el torneo.")
