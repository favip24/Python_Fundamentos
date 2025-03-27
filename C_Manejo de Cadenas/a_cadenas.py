# Manejo de Cadenas
# Se utilizan para almacenar secuencia de caracteres
# Se encierran entre comillas
cadena1 = "¡Hola y Bienvenidos!"
cadena1 = "¡Adiós, Vuelva Pronto!"
cadena2 = 'Cómo lo ayudo?'
cadena3 = """
Los Macros Nutrientes son:
- Carbohidratos
- Grasas
- Proteínas"""  # Cadena de Multipleslineas.
print("Cadenas")
print(cadena1)
print(cadena1)
print(cadena2)
print(cadena3)
print()

# Índices de Cadenas
# Los caracteres están indexados de manera secuencial
# Podemos acceder a cada caracter que deseemos
primer_caracter = cadena1[0]
ultimo_caracter = cadena3[10]
print("Indices de Cadeas")
print(primer_caracter)
print(ultimo_caracter)
print()

# Inmutabilidad de una Cadena
# Una vez creada una cadena, no podemos modificarla
# Si así quisieramos, deberíamos crear una nueva y pasarle la referencia
saludo = "Buenos días"
saludo2 = saludo  # Pasamos la referencia para no perder el objeto.
saludo = "Buenas noches"
print("Inmutabilidad de Cadenas")
print(saludo)
print(saludo2)
print()

# Caracteres Especiales
print("Cómo \nandas?")  # \n: Salto de línea.
print("\t Python es God")  # \t: Tab inicial.
print("Desire\" Cuper")  # "\: Permite "" dentro de una Cadena.
print("\\")  # "\": Incluye '\' como caracter especial.
print()

# Concatenación de Cadenas
# Combinar dos o más cadenas para formar una nueva
# Usando el operador '+'
# Usando la función "".join
hola = "Hola"
mundo = "Mundo!"
print("Concatenación de Cadenas")
print(hola + " " + mundo)  # Operador '+'
despedida1 = "Che"
despedida2 = "nos vemos"
despedida3 = "mañana."
despedida4 = "".join([despedida1, " ", despedida2, " ", despedida3])  # Join
print(despedida4)
print()

# Formateo de Cadenas
# f-string
nombre = "Favio"
edad = 25
formateo_cadenas = f"Hola, me llamo {nombre} y tengo {edad} años."
print("Formateo de Cadenas")
print("f-string: " + formateo_cadenas)
print()

# Método format
formateo_cadenas = "Hola me llamo {} y tengo {} años.".format(nombre, edad)
print("Método 'format': " + formateo_cadenas)
print()

# Métodos de Cadenas
mayusculas = formateo_cadenas.upper()  # Convierte a Mayúsculas.
minusculas = formateo_cadenas.lower()  # Convierte a Minúsculas.
sin_espacios = formateo_cadenas.strip()  # Elimina espacios al principio y fin.
longitud_cadena = len(formateo_cadenas)  # Devuelve en números el largo.
print("Métodos de Cadenas")
print("Todo en mayúsculas:", mayusculas)
print("Todo en minúsculas:", minusculas)
print("Sin Espacios Al Princio y Fin: ", sin_espacios)
print("Caracteres totales de la cadena:", longitud_cadena)
print()

# Subcadenas
# Es una parte de una cadena principal
# Podemos buscarlas, reemplazarla, etc

# Extracción de Subcadena con Slicing
# Indica el índice del incio y final (sin incluirlo)
# SINTAXIS = subcadena[inicio:fin]
subcadena_saludos = saludo[0:6]  # Obtenemos solo 'Buenos'
subcadena_saludos2 = saludo[7:13]
print("Subcadenas: Extracción")
print(subcadena_saludos)
print(subcadena_saludos2)
print(subcadena_saludos + " " + subcadena_saludos2)
print()

# Buscar Subcadenas con find()
# Devuelve el primer índice de la subcadena
# Si no encuentra nada devuelve '-1'
# SINTAXIS: subcadena = subcadena.find("cadena")
buscar_subcadena = saludo.find("noches")
buscar_subcadena2 = saludo.find("días")
buscar_subcadena3 = saludo.find("tardes")
print("Subcadenas: Búsqueda")
print(buscar_subcadena)  # Imprime el índice del primer caracter
print(buscar_subcadena2)  # Cuando no se encuentra se imprime -1
print()

# Reemplazar subcadenas con replace
# Reemplaza una subcadena por otra, dentro de una principal
# SINTAXIS: subcadena = subcadena.replace("noches", "tardes")
nuevo_saludo = saludo.replace("noches", "tardes")
nueva_despedida = saludo2.replace("Buenos días", "Adiós, un abrazo!")
print("Subcadenas: Reemplazar")
print(nuevo_saludo)
print(nueva_despedida)
print()

# Extraer Subcadenas por separadores con Método Split
# Divide la cadena en una lista, por eso va entre []
# Si no encuentra una coma, el separador por default es un espacio en blanco
# Sintaxis: lista = cadena.split(',')
cadena_sp = "Patricio Fontanet, 40 años, Argentina"
cadena_sp2 = "Patricio Rogelio Santos Fontantet"
lista = cadena_sp.split(",")
lista2 = cadena_sp2.split()
print("Subcadena: Extracción SPLIT")
print(lista)  # Separa elementos por coma
print(lista2)  # Por default, separa cada elemento por espacio en blanco
print()

# Multiplicador de Cadenas
# Define cuantas veces se repite una cadena
veces = 4
resultado = hola * veces
print("Multiplicación de Cadenas")
print(resultado)
print()
