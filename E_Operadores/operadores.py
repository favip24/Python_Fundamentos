# Operadores Aritméticos
# Cálculos Matemáticos
print("Operadores Aritméticos")
print()

suma = 5 + 5  # Suma
resta = 10 - 5  # Resta
multiplicacion = 5 * 5  # Multiplicación
division = 25 / 5  # División
division_entera = 25 // 5  # División Entera
modulo = 25 % 5  # Módulo
exponente = 5 ** 5  # Exponente

resultado = f"Suma de dos operadores: {suma}\n" \
            f"Resta de dos operadores: {resta}\n" \
            f"Multiplicación de dos operadores: {multiplicacion}\n" \
            f"División de dos operadores: {division}\n" \
            f"División de tipo entero de dos operadores: {division_entera}\n" \
            f"Regresa el residuo de la división: {modulo}\n" \
            f"Eleva el primer operador a la potencia del segundo: {exponente}\n" \

print(resultado)
print()

# Operadores Asignación
# Asignar un valor a una variable
# Ya estuvimos trabajando con esto, ahora lo formalizamos
print("Operadores Asignación")
print()

# SINTAXIS: variable = valor
numero = 20
texto = "Buenos días"

# Asignación Múltiple
# Asignar valores a multiples variables en una sola línea de código
# SINTAXIS: variable1, variable2 = valor1, valor2
nmb, apd, edd, alt = "Favio", "Palermo", 25, 1.81

# Asginación Encadenada
# Asignar el mismo a valor a múltiples variables
# SINTAXIS: variable2 = variable2 = valor
contador1 = contador2 = contador3 = 0.0

mensaje = f"Variable con Valor Numérico: {numero}\n" \
          f"Variable con Valor Texto: {texto}\n" \
          f"Variables con Asignación Múltiple: {nmb} {apd}, {edd}, {alt}\n" \
          f"Variable con Asginación Encadenada: {contador1}, {contador2}, {contador3}\n" \

print(mensaje)
print()

# Operadores Asignación Compuestos
# Combinan una operación aritmética con una asignación, haciendo operaciones más conscisas
# +=, -=, *=, /=
print("Operadores de Asignación Compuestos")
print()

sueldo_total = 1000000
sueldo = 1000000
impuestos = 500000
comida = 200000

# SINTAXIS: variable OPERADOR= valor
sueldo -= impuestos
sueldo -= comida

mensaje2 = f"He cobrado mi sueldo, en total ${sueldo_total} de pesos argentinos.\n" \
            "Fui a pagar los impuestos y comprar comida.\n" \
           f"los cual era ${impuestos} y ${comida} de pesos.\n" \
           f"Ahora me quedan para ahorrar ${sueldo}\n" \

print(mensaje2)
