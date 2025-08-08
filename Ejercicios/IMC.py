
nombre = input("nombre: ")
edad = int(input("edad: "))
altura = float(input("altura en metros: "))
peso = float(input("peso en kilogramos: "))


imc = peso / (altura ** 2)


if imc < 18.5:
    categoria = "Bajo"
elif 18.5 <= imc <= 24.9:
    categoria = "Normal"
elif 25.0 <= imc <= 29.9:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"



print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura:.2f} m")
print(f"Peso: {peso:.1f} kg")
print(f"IMC: {imc:.2f}")
print(f"Categoría según la OMS: {categoria}")
