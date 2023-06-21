foods= []

def show_foods():
    for food in foods:
        print(f"Comida {food}")
    
def add_food(food):
    foods.append(food)
    
def del_food(food):
    try:
        foods.remove(food)
    except Exception:
        print("No se encuentra en la lista.")
    
text_menu ='''
Elige una opcion:
    1- Agree Food
    2- Delete Food
    3- Show Food 
    4- Exit
'''

while True:
    choice_user = int(input(text_menu))
    if choice_user==1:
        food=input("Write a food")
        add_food(food)
        
    elif choice_user==2:
        food=input("Write a food")
        del_food(food)
        
    elif choice_user==3:
        show_foods()
        
    elif choice_user==4:
        break
    else:
        print("Escribe bien.")