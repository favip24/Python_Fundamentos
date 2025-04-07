# Le pedí a ChatGPT que me creara ejercicios para practicar
# Programar se aprende programando!

# Ejercicio 1: Datos Personales
# Crea un programa que pida al usuario su nombre, edad y ciudad
print('Ejercicio 1: Datos Personales:')
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")

mensaje_completo = f'Bienvenido {nombre}, gracias por registrarse!'
mensaje_completo2 = f'Usted tiene {edad}, \npor lo que el próximo año tendrá {edad + 1}!'
mensaje_completo3 = f'Usted actualmente vive en {ciudad}!'

print(mensaje_completo)
print(mensaje_completo2)
print(mensaje_completo3)

# Ejercicio 2: Cálculo del área de un rectángulo
# Solicita al usuario el ancho y el alto de un rectángulo y calcula su área
print("Calcular el área de un rectángulo")
print("Fórmula: Área = ancho * alto")

ancho = float(input("Ingrese el ancho del rectángulo: "))
alto = float(input("Ingrese el alto del rectángulo: "))
area = ancho * alto

print(f"El área del rectángulo es: {area}")

# Ejercicio 3: Conversión de temperatura
# Pide al usuario una temperatura en grados Celsius y conviértela a Fahrenheit usando la fórmula
print("Conversión de Temperatura")
print("Fórmula: Fahrenheit = (Celsius * 9/5) + 32")

temperatura_celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"{temperatura_celsius}°C equivalen a {fahrenheit}°F")

# Ejercicio 4: Cálculo del salario semanal
# Solicitar al usuario: Hs Trabajadas, Usd por Hs
print("Cálculo de Sueldo Semanal")
print("Fórmula: Sueldo Semanal = Hs Trabajadas * Usd x Hs")

horas_trabajadas = int(input("Ingrese las horas trabajadas: "))  # Por día
pago_hora = float(input("Ingrese el pago por hora: "))
sueldo_semanal = (horas_trabajadas * 5) * pago_hora  # *5 días a la semana

print("El sueldo semanal es ${} Usd" .format(sueldo_semanal))
