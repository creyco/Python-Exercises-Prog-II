# f.
# Un portal web requiere un formulario de alta de usuario donde se ingrese,
# mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python,
# una función contrasena_valida(contrasena) que devuelva True en caso de
# superar las siguientes validaciones sobre la contraseña proporcionada por el
# usuario:
# i. Longitud entre 6 y 20 caracteres.
# ii. Debe contener al menos un número.
# iii. Debe contener al menos dos mayúsculas.
# iv. Debe contener al menos un carácter especial.
# v. No puede contener espacios.
# USO comprehension

def contrasena_valida(contrasena):
    if 6 < len(contrasena) < 20:
        if any([c.isdigit() for c in contrasena]):
            if any([c.islower() for c in contrasena]):
                if any([c.isupper() for c in contrasena]):
                    if any([True if c in  "[$&+,:;=?@#|<>.^*()%!-]" else False for c in contrasena]):
                       print("Contraseña Valida")     
                       return True
                    else:
                        print("La contraseña debe tener algun CARACTER ESPECIAl")
                else:
                    print("La contraseña debe tener alguna mayuscula")
            else:        
                print("La contraseña debe tener alguna minuscula")
        else:
                print("La contraseña debe tener algun digito")
    else:
            print("La contraseña debe tener entre 6 y 20 caracteres")
    return False

#pwd = input("Ingrese su Contraseña: ")
pwd="Mi2Contraseña*"

if contrasena_valida(pwd):
    print(pwd)

# Otra opcion
def contrasena_valida2(contrasena):
    if len(contrasena) < 6 or len(contrasena) > 20:
        print("La contraseña debe tener entre 6 y 20 caracteres")
    elif not any([c.isdigit() for c in contrasena]):
        print("La contraseña debe tener algun digito")
    elif not any([c.islower() for c in contrasena]):
        print("La contraseña debe tener alguna minuscula")
    elif not any([c.isupper() for c in contrasena]):
        print("La contraseña debe tener alguna mayuscula")
    elif not any([True if c in "[$&+,:;=?@#|<>.^*()%!-]" else False for c in contrasena]):
        print("La contraseña debe tener algun CARACTER ESPECIAl")
    else:    
        print("Contraseña Valida")     
        return True              
    return False


#pwd = input("Ingrese su Contraseña Ver1: ")
pwd = "Tu$Contraseña"
if contrasena_valida2(pwd):
    print(pwd)
