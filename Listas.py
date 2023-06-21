my_list = [0, 1, "dos", 3.14, True]
print(type(my_list))

my_list.append("New item")
my_list.remove(1)
print(my_list.pop())
print(my_list.reverse())

print(my_list[3])
my_list[0]="Cambia valor"
print(my_list)

other_list=[3,2,4,1,5,3,6]
print(other_list.reverse())
print(other_list)
print(other_list.sort())
print(other_list)

#slicing
print(other_list[:3])
print(other_list[3:])