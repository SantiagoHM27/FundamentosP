my_string="Hola, soy un string"
print(type(my_string))

print(my_string.upper())
print(my_string.upper())
print(my_string.cower())
print(my_string.title())

print(len(my_string))

#indexing
my_string="Mis compañeros se pasan de vrg con Juan"
print(my_string[12])
my_string[4]="A"
for letter in my_string:
    print(f"la letra{letter}")

print(my_string[-1])
print(my_string[-2])

#slicing
print(my_string[:])
print(my_string[0:3])
print(my_string[3:])
print(my_string[3:7])
print(my_string[:7])
print(my_string[::-1])