import random

# Lista de usuarios
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

def generar_usuario_aleatorio():
    return random.choice(usuarios)

# Generar y mostrar un usuario aleatorio
usuario_aleatorio = generar_usuario_aleatorio()
print("Usuario aleatorio generado:", usuario_aleatorio)