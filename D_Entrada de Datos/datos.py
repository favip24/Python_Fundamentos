# Conversión de Tipos de Datos
# Conocida como 'Casting'
# Es una técnica para manipular datos que no están en el tipo requerido
# Pueden hacerse desde y hacia distintos tipos

# De Cadena a Entero
# SINTAXIS: entero_cadena = int(cadena_entero)
entero_cadena = "10"
entero_entero = int(entero_cadena)

print("Conversión de Cadenas")
print()
print("Cadena a Entero")
print("Número como cadena: ", entero_cadena)
print("Cadena como entero convertido: ", entero_entero)
print()

# De Cadena a Flotante
# SINTAXIS: flotante_cadena = float(cadena_flotante)
flotante_cadena = "3.5"
flotante_flotante = float(flotante_cadena)

print("Cadena a Flotante")
print("Flotante como cadena: ", flotante_cadena)
print("Cadena como flotante convertido: ", flotante_flotante)
print()

# De Entero a Cadena
# SINTAXIS: entero_entero = int(entero_cadena)
entero_entero = 25
entero_cadena = str(entero_entero)

print("Entero a Cadena")
print("Número como entero: ", entero_entero)
print("Entero como cadena convertido: ", entero_cadena)
print()

# Convertir a Booleano
# False: Si el valor es 0, cadena vacía, o None
# True: Si el valor es distinto de 0, de cadena vacía, o de None
# SINTAXIS: cadena/numero = boolean(cadena/numero)
numero_entero = 0
numero_entero2 = 18
numero_booleano = bool(numero_entero)
numero_booleano2 = bool(numero_entero2)
cadena_vacia = ""
cadena_completa = "Verdadero"
cadena_falsa = bool(cadena_vacia)
cadena_verdadera = bool(cadena_completa)

print("Convertir a Booleano")
print("Número como 0: ", numero_entero)
print("Número como entero: ", numero_entero2)
print("Número como False: ", numero_booleano)
print("Número como True: ", numero_booleano2)
print("Cadena Vacía: ", cadena_vacia)
print("Cadena Completa: ", cadena_completa)
print("Cadena como False: ", cadena_falsa)
print("Cadena como True: ", cadena_verdadera)
print()

# Demostración
concatenacion = entero_cadena + flotante_cadena  # Números como cadenas
suma_numeros = entero_entero + flotante_flotante  # Números como números
print("Caso Demostrado")
print("Concatención de Cadenas: ", concatenacion)  # 253.5
print("Suma de Números: ", suma_numeros)  # 25 + 3.5 = 28.5
print()

# Entrada de Datos por Consola
# Se realiza usando la función input()
# Se pausa la ejcución del programa y espera que el usaurio introduzca datos
# Una vez se presiona enter se devuelve los datos ingresados
print("Entrada de Datos por Consola")
nombre = input("Ingrese su nombre: ")  # Se pausa la ejecución
print("Nombre: ", nombre)
edad = int(input("Ingrese su edad: "))  # Convertimos a entero con int()
print("Edad: ", edad)
