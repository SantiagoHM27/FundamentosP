#Funciones
#Def name_fuction():
# code


#Funcion sin parametros
#Funcion sin retorno

def saluda():
    print("Hola prros")
    
saluda()

#parametros sin retornos

def duplica(number):
    print(number*2)

duplica(23)

def suma(num1, num2):
    print(num1+num2)

suma(12,15)

#parametros opcionales
def lista_drinks(d1="Beer", d2="water"):
    print(d1)
    print(d2)

lista_drinks("Tequila")
lista_drinks()
lista_drinks("Tequila", "Juice")

#Funciones con retorno
#return

def get_list():
    return [1,2,3]
list_gotten = get_list()
print(list_gotten)

def resta(va1,va2):
    return va1-va2

result = resta(13,2)
print(result)

def duplica_list(list):
    new_list = []
    for item in list:
        new_list.append(item*2)
    return new_list

my_list=[1,2,3,4,5]
print(my_list)
new_list=duplica_list(my_list)
print(new_list)