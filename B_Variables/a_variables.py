# Variables
# Datos que pueden variar o cambiar
# Las Variables deben definirse y asignarles un valor (obligatorio)
# Sintaxis: nombreVariable = valor

# String/Cadenas de texto
# Se utilizan comillas simples, dobles o triples
nombre = "Mateo"
apellido = 'Palermo'
texto = """
        Datos:
            nombre: Favio
            apellido: Palermo
            edad: 25
            pais: Argentina"""

# Numero Entero = Int
edad = 19
# Numero con coma o de punto flotante = Float o Double
peso = 80.5
altura = 1.85
# Valor Booleano, se escriben la 'F' o 'T' con mayúsculas
es_casado = False
es_soltero = True
# Ausencia de valor
discapacidad = None

# Imprimimos las Variables en consola
print("Variables")
print("Mi nombre es", nombre)  # Python agrega un espacio al separar con coma
print("Tengo", edad, "Años")
print("Actualmente estoy pesando", peso, "Kg.")
print("Soy Casado?", es_casado)
print("Soy Soltero?", es_soltero)
print("Tengo alguna discapacidad?", discapacidad)
print(texto)
print()

# Modificar los Valores de las Variables
edad = 21  # Misma Sintaxis con distinto valor
peso = 91.5  # Se sobrescriben los valores perdiendo el anterior

# Valores Modificados
print("Modificamos Variables")
print(edad)
print(peso)
print()

# Python es dinámico, puede almacenar cualquier dato en cualquier variable
# Aún así no es una buena práctica esta
altura = "Un Metro Ochenta"
print(altura)
print()

# Constantes
# Es un tipo de variable la cual no puede/debe ser cambiada
# Sintaxis: NOMBRE_VARIABLE = valor
PI = 3.14159
NOMBRE_BASE_DATOS = "clientes_db"
print("CONSTANTES")
print(PI)
print(NOMBRE_BASE_DATOS)
print()
