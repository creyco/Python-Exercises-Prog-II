import re

# i. Longitud entre 6 y 20 caracteres.
# ii. Debe contener al menos un número.
# iii. Debe contener al menos dos mayúsculas.
# iv. Debe contener al menos un carácter especial.
# v. No puede contener espacios.

pattern = "^(?=.{6,20}$)(?=(?:.*?[A-Z]){2})(?=.*?[a-z])(?=(?:.*?[0-9]))(?=(?:.*[!@#$%^&*()\-_=+{};:,<.>])).*$"

lista = ["mi$ContraseN12","Mi5pass", "MI5#pss", "Lo+Grande", "Lo>Chic0"]

#password = raw_input("Ingres Password: ")

for password in lista:
    result = re.findall(pattern, password)     

    print("\x1b[1;33mContraseña: ", password,end=" ")
    print("\x1b[0;m")

    if (result):
        print("Valid password")
    else:
        print("Password not valid")

