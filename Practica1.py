a=input("Introduce un número: ")
while not a.isnumeric():
    a=input("Error! No es un número! Introduce un número: ")
n1=float(a)
b=input("Introduce otro número: ")
while not b.isnumeric():
    b=input("Error! No es un número! Introduce otro número: ")
n2=float(b)

resultado=(n1+n2)/2

print("La media aritmética de ",n1," y ",n2, " es", resultado)