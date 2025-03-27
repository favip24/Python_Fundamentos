print("Generador de Email")
print()

# datos del usuario
nombre_usuario = "Favio Palermo"
nombre_empresa = "Flexxus"
dominio = ".com.ar"

# adaptación con métodos
usuario_sin_espacios = nombre_usuario.replace(" ", ".")
usuario_normalizado = usuario_sin_espacios.lower()
empresa_normalizada = nombre_empresa.lower()
email_generado = usuario_normalizado + "@" + empresa_normalizada + dominio
mensaje_confirmacion = f"Muchas Gracias {nombre_usuario} por registrarte!"
mensaje_confirmacion2 = f"Tu nuevo mail será {email_generado}. Buena jornada!"

# impresión del email
print(mensaje_confirmacion)
print(mensaje_confirmacion2)
