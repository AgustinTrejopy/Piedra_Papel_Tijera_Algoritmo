import random

# Back-End
items = ['piedra', 'papel', 'tijera']
juego = random.randint(0, 2)
bot = items[juego]

# Elecciones
print("""Opciones: 
piedra
papel
tijera
---------------------------------------
""")
vos = input("Que opcion elegis? ")
print("tu eleccion fue: ", vos)
print("La eleccion del bot fue: ", bot)

# Logica
if vos == bot:
    print("Empate\n\n")

elif vos == 'tijera':
    if bot == 'piedra':
        print("Perdiste : (\n\n")
    elif bot == 'papel':
        print("Ganaste!!!\n\n")

elif vos == 'papel':
    if bot == 'tijera':
        print("perdiste : (\n\n")
    elif bot == 'piedra':
        print("Ganaste!!!\n\n")

elif vos == 'piedra':
    if bot == 'papel':
        print("Perdiste : (\n\n")
    elif bot == 'tijera':
        print("Ganaste!!!\n\n")