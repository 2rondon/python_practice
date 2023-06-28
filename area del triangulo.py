#Ejercicio 1 area del Triangulo

def calcularArea(a,b):
    area = (a * b)/2
    return area

print("Ingresar altura")
a = float(input())
print("Ingresar Base")
b = float(input())

print("El Area es" + str(calcularArea(a,b)))
