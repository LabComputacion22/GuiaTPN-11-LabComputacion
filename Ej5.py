email = input("Ingrese su correo electronico: ")
email_nuevo = str

email_nuevo = email[:email.find("@")] + "@ceu.es"

print(email_nuevo)
