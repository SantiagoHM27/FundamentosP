#Eleccion de maquina
import random

num_rand = random.randint(1,3)
if num_rand ==1:
    choice_maq='Piedra'
elif num_rand ==2:
    choice_maq='Papel'
else:
    choice_maq='Tijera'
    
#Eleccion de usuario

choice_text='''
Escribe una opcion:
    Piedra 
    Papel
    Tigera
'''
Choice_user = input(choice_text)
#Imprime seleccion
print("Usuario Elige: ", Choice_user)
print("Maquina Elige: ", choice_maq)

#Define ganador
if Choice_user == choice_maq:
    print("Es un empate")
else:
    if Choice_user == 'Piedra' and choice_maq == 'Papel':
        print("Gana Maquina.")
    elif Choice_user == 'Piedra' and choice_maq == 'Tijera':
        print("Gana Usuario.")
    elif Choice_user =='Papel' and choice_maq == 'Piedra':
        print("Gana Usuario.")
    elif Choice_user =='Papel' and choice_maq == 'Tijera':
        print("Gana MMaquina.")
    elif Choice_user == 'Tijera' and choice_maq == 'Piedra':
        print("Gana Maquina.")
    else:
        print("Escribe bien.")