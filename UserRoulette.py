import random

# Lista original de usuarios
usuarios = [
    "HaggardCoder - Eduardo",
    "YuUs01 - Youssef",
    "Lowri-ui - Laura",
    "KUERVO - Angel",
    "ItsKein - Juan",
    "JaimeRuiz06 - Jaime",
    "naroa0699 - Naroa",
    "Montez - JorgeMontez",
    "Nezeon7 - Rubén",
    "Alexandra024 - Sara",
    "Ces216 - César",
    "DanielHe22 - Daniel",
    "AlexWhut - Alex",
    "DGuelar - David",
    "Eugenia-2024 - Eugenia",
    "Karls3fni - Manu"
]

# Para guardar los ya mostrados
usuarios_mostrados = []

print("Pulsa 'R' y ENTER para generar un usuario aleatorio (sin repetir). Escribe 'Q' para salir.")

while True:
    opcion = input(">> ").strip().upper()

    if opcion == "Q":
        print("Programa finalizado.")
        break
    elif opcion == "R":
        # Verificar si ya se mostraron todos
        if len(usuarios_mostrados) == len(usuarios):
            print("Ya se han mostrado todos los usuarios.")
            break

        # Seleccionar un usuario que no se haya mostrado
        while True:
            usuario = random.choice(usuarios)
            if usuario not in usuarios_mostrados:
                usuarios_mostrados.append(usuario)
                print("Usuario aleatorio generado:", usuario)
                break
    else:
        print("Opción no válida. Usa 'R' para repetir o 'Q' para salir.")
