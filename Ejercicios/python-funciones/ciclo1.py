codigo_seguridad = "ZONA1234"
codigo_ingresado = input("Ingrese el código de seguridad: ")

if codigo_ingresado == codigo_seguridad and len(codigo_ingresado) >= 8:
    print("Acceso a la zona restringida permitido")
else:
    print("Código incorrecto o demasiado corto. Acceso denegado.")
