import random
print ("Juguemos Cachipún")
sabores = ["piedra", "papel" ,"tijera"]
while True: 
   jugador = input("Elige, piedra, papel o tijera: ").lower()
   if jugador not in sabores :
    print (f"No entiendo qué es {jugador}...")
   else:
     break
computadora = random.choice(sabores)
print (f"La computadora elige {computadora}")

if (jugador == "piedra" and computadora == "tijera") or (jugador == "tijera" and computadora == "papel") or (jugador == "papel" and computadora == "piedra"):
  ganador = "Jugador"
elif  jugador == computadora :
    ganador = "Empate"
else :
   ganador = "Computadora"

if ganador == "Jugador" :
  print ("Ganaste. WENA QLO")
elif ganador == "Empate" :
  print ("¡Empate!")
else :
  print ("Perdiste. ¿Mejor de Tres?")