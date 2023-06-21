my_tuple=(1,"dos", 3.1, True)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
#error
#my_tuple[0]="Algo mas"


my_Set={"uno", "dos", "tres", "uno"}
print(type(my_Set))
print(my_Set)
my_Set.add(4)
print(my_Set)

a={1,2,3,4}
b={5,6,7,8}
print(a.union(b))
print(a.intersection(b))