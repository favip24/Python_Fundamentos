# Generar Valores Aleatorio
# La función randint() nos permite generar números aleatorios
# Es parte del módulo 'random'

# Siempre primero hay que importar el módulo antes de usar la función
# SINTAXIS: número = randint(a, d)
from random import randint
numeros = randint(1, 10)  # Generar un núnmero al azar entre 1 y 10
print(f"Número aleatorio entre 1 y 10: {numeros}")
print()

# Sistema de ID Único
# Crear un Generador de ID para cada individuo
print("Generador Único de ID")
print("Por favor, ingrese los siguientes datos:")

# Ingreso de Datos en la Consola
nombre = input("Nombre: ")
apellido = input("Apellido: ")
año_nacimiento = input("Año de Nacimiento: ")
numero_aleatorio = randint(1000, 10000)  # Generamos el número al azar de 4 dígitos
print()

# Extraemos las subcadenas
nombre_id = nombre.lower()[0:2]
apellido_id = apellido.lower()[0:2]
año_nacimiento_id = año_nacimiento[2:4]

# Imprimimos el mensaje con el formateo de cadenas
# Agregamos saltos de líneas para mejor legibilidad
mensaje_final = f"¡Hola {nombre}! Muchas gracias por completar los datos\n" \
                "Tu nuevo Identificador Único (ID) creado por el sistema es:\n" \
                f"{nombre_id}{apellido_id}{año_nacimiento_id}{numero_aleatorio}\n" \
                "¡Muchas gracias!¡Hasta Pronto!"

print(mensaje_final)
print()

# Sistema de Correo Electrónico
# Crear un Generador de Correo Electrónicos para cada usuario
print("Generador Único de Correo Electrónicos")
print("Por favor, ingrese los siguientes datos:")

nombre2 = input("Nombre: ")
apellido2 = input("Apellido: ")
numero_aleatorio2 = randint(0, 99)
empresa = input("Nombre de la Empresa: ")
dominio = ".com.ar"
print()

nombre_mail = nombre2.lower()
apellido_mail = apellido2.lower()
empresa_mail = empresa.lower()

mensaje_final2 = f"¡Hola {nombre2}! Muchas gracias por registrar sus datos!\n" \
                 "Tu nuevo correo elctrónico creado por el sistema es:\n" \
                 f"{nombre_mail}{apellido_mail}{numero_aleatorio2}@{empresa_mail}{dominio}\n" \
                 "¡Muchas gracias!¡Que tengas muy buena jornada!"

print(mensaje_final2)
print()
