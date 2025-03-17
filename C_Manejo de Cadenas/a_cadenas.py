# Manejo de Cadenas.
nombre = "Favio"
edad = 25
cadena1 = "¡Hola y Bienvenidos!"
cadena1 = "¡Adiós, Vuelva Pronto!"
cadena2 = 'Cómo lo ayudo?'
cadena3 = """
Los Macros Nutrientes son:
- Carbohidratos
- Grasas
- Proteínas"""  # Cadena de Multipleslineas.
print(cadena1)
print(cadena1)
print(cadena2)
print(cadena3)
print()

# Índices de Cadenas.
primer_caracter = cadena1[0]
ultimo_caracter = cadena3[10]
print(primer_caracter)
print(ultimo_caracter)
print()

# Inmutabilidad de una Cadena.
saludo = "Buenos días"
saludo2 = saludo  # Pasamos la referencia para no perder el objeto.
saludo = "Buenas noches"
print(saludo)
print(saludo2)
print()

# Caracteres Especiales.
print("Cómo \nandas?")  # \n: Salto de línea.
print("\t Python es God")  # \t: Tab inicial.
print("Desire\" Cuper")  # "\: Permite "" dentro de una Cadena.
print("\\")  # "\": Incluye '\' como caracter especial.
print()

# Concatenación de Cadenas.
hola = "Hola"
mundo = "Mundo!"
print(hola + " " + mundo)  # Operador '+'
despedida1 = "Che"
despedida2 = "nos vemos"
despedida3 = "mañana."
despedida4 = "".join([despedida1, " ", despedida2, " ", despedida3])  # Join
print(despedida4)
print()

# Formateo de Cadenas.
# f-string

formateo_cadenas = f"Hola, me llamo {nombre} y tengo {edad} años."
print(formateo_cadenas)
print()

# Método format.
formateo_cadenas = "Hola me llamo {} y tengo {} años.".format(nombre, edad)
print(formateo_cadenas)
print()

# Métodos de Cadenas
mayusculas = formateo_cadenas.upper()  # Convierte a Mayúsculas.
minusculas = formateo_cadenas.lower()  # Convierte a Minúsculas.
sin_espacios = formateo_cadenas.strip()  # Elimina espacios al principio y fin.
longitud_cadena = len(formateo_cadenas)  # Devuelve en números el largo.
print("Todo en mayúsculas:", mayusculas)
print("Todo en minúsculas:", minusculas)
print(sin_espacios)
print("Caracteres totales de la cadena:", longitud_cadena)
print()

# Subcadenas
# Sintaxis: subcadena = cadena[inicio:fin]
subcadena_saludos = saludo[0:6]  # Obtenemos solo 'Buenos'
subcadena_saludos2 = saludo[7:13]
print(subcadena_saludos)
print(subcadena_saludos2)
print(subcadena_saludos + " " + subcadena_saludos2)
print()

# Buscar subcadenas con find()
# Sintaxis: posicion = cadena.find("cadena")
buscar_subcadena = saludo.find("noches")
buscar_subcadena2 = saludo.find("días")
print(buscar_subcadena)  # Imprime el índice del primer caracter
print(buscar_subcadena2)  # Cuando no se encuentra se imprime -1
print()

# Reemplazar subcadenas
# Sintaxis: nueva_cadena = cadena.replace("noches", "tardes")
nuevo_saludo = saludo.replace("noches", "tardes")
nueva_despedida = saludo2.replace("Buenos días", "Adiós, un abrazo!")
print(nuevo_saludo)
print(nueva_despedida)
print()

# Extraer Subcadenas por separadores con el Método Split
# Divide en una lista, por eso va entre []
# Sintaxis: lista = cadena.split(',')
cadena_sp = "Patricio Fontanet, 40, Argentina"
cadena_sp2 = "Patricio Rogelio Santos Fontantet"
lista = cadena_sp.split(",")
lista2 = cadena_sp2.split()
print(lista)  # Separa elementos por coma
print(lista2)  # Por default, separa cada elemento por espacio en blanco
print()

# Multiplicador de Cadenas
veces = 4
resultado = hola * veces
print(resultado)
print()
