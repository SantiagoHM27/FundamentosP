#if y else
age = int(input("Cual es tu edad? "))
if age >= 10:
    print("Eres mayor de edad.")
else:
    print("NO eres mayor de edad")
    
age = int(input("Cual es la edad de tu hermana? "))
if age <= 10:
    print("Eres mayor de edad.")
elif age <= 29:
    age1 = input("Que estudia? ")
    print(f"Es menor pero estudia {age1}")