#ciclos
x=1
num=7
while x<=10:
    print(f"{num}*{x}={num*x}")
    x+=1
else:
    print("termina el ciclo")
    
#Ciclo for
#permite correr 

my_String="Hola a todos"
for letter in my_String:
    print(letter, end=', ')
print()

my_list=["uno", "dos", "tres", "cuatro"]
for item in my_list:
    print(item, end=', ')
print()

#Fuction range()
#ramge()
for i in range(10):
    print(i, end=', ')
print()
for i in range(10, 20):
    print(i, end=', ')
print()
for i in range(10, 100, 10):
    print(i, end=', ')
print()
#