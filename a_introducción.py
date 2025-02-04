# Primer programa de "Hola Mundo" con Python.
print("Hola Mundo")
print("Saludos")
print()  # Print vacío para mejor legibilidad.

# Presentación.
print("Hola, soy Favio Palermo")
print("Tengo 25 años")
print("Soy de Córdoba, Argentina.")
print()

# Variables.
# Sintaxis: nombreVariable = valor
# Las Variables deben definirse y asignarles un valor (obligatorio).
nombre = "Mateo"  # Cadena de Texto, pueden inicializarce con comillas "" o ''.
edad = 19  # Dato de tip Entero tipo Int.
peso = 80.5  # Dato de punto flotante, Double o Float.
pais = "Argentina"
es_casado = False  # Tipo Boolean, se escriben la 'F' o 'T' con mayúsculas.
carrera = None  # Ausencia de valor.

# Imprimimos las Variables en consola.
print("Mi nombre es", nombre)  # Python agrega un espacio al separar con coma.
print("Tengo", edad, "Años")
print("Actualmente estoy pesando", peso, "Kg.")
print("Vivo en", pais)
print("Soy Casado?", es_casado)
print("Qué Estudia?", carrera)
print()

# Modificar los Valores de las Variables.
edad = 21  # Misma Sintaxis con distinto valor.
peso = 91.5  # Se sobrescriben los valores perdiendo el anterior.

# Valores Modificados.
print(edad)
print(peso)
print()

# Python es dinámico, puede almacenar cualquier dato en cualquier variable.
altura = "Un Metro Ochenta"
print(altura)
print()

# Constantes.
# Sintaxis: NOMBRE_VARIABLE = valor
PI = 3.14159
NOMBRE_BASE_DATOS = "clientes_db"
print(PI)
print(NOMBRE_BASE_DATOS)
print()

# Manejo de Cadenas.
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
# Las últimas variables eran n=Mateo y e=21
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
