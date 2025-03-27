# Sistema de Empleados
# Se Creara un Programa para solicitar la información del personal

# Nombre - Str
# Edad - Convertir a Int
# Sueldo - Convertir a Float
# Discapacidad - Str #
print("Sistema de Empleados")
print("Por favor ingrese los siguientes datos para registrarse:")
print()

# Colocamos los datos en Consola
nombre = input("Nombre: ")
apellido = input("Apellido: ")
nombre_completo = nombre + apellido
edad = int(input("Edad: "))
sueldo = float(input("Sueldo: "))
discapacidad = input("Discapacidad: ")
print()

# Imprimimos en Consola
print("Confirmación de Datos: ")
print(f"Nombre Completo: {nombre_completo}")
print(f"Edad: {edad} Años")
print(f"Por lo que el proximo año tendrá {edad + 1}.")
print(f"Sueldo: ${sueldo}")
print(f"Tiene Discapacidad? {discapacidad}")
