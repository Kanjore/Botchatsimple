
import json
#abrir el Json
with open('conversacion.json', 'r') as file:
    conversacion = json.load(file)
#se imprime la informacion
print("<======================================>")
print("Pon agg para agregar una nueva palabra")
print("Pon exit para salir")
print("<======================================>")
#comienza el bucle y la conversación
while True:
    user_input = input("Tú: ").lower()
    if user_input in conversacion:
        respuesta = conversacion[user_input]
        print("Bot:", respuesta)
    elif user_input == "exit":
        break
    elif user_input == "agg":
        agg_new = input("System: agrega la nueva clave: ").lower()        
        new_qs = input("System: agrega el nuevo valor: ")
        conversacion[agg_new] = new_qs
        with open('conversacion.json', 'w') as file:
            json.dump(conversacion, file)
            print("System: se a guardado con exito")
    else:
          print("System: Lo siento, no entiendo lo que quieres decir")