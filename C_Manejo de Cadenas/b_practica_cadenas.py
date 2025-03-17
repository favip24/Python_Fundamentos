print("Generador de Email")
print()

# datos del usuario
nombre_usuario = "Favio Palermo"
nombre_empresa = "Kolector"
dominio = ".com.ar"

# adaptación con métodos
usuario_sin_espacios = nombre_usuario.replace(" ", ".")
usuario_normalizado = usuario_sin_espacios.lower()
empresa_normalizada = nombre_empresa.lower()
email_generado = usuario_normalizado + "@" + empresa_normalizada + dominio

# impresión del email
print(email_generado)
