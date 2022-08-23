print ("Ingrese un numero, se detendra cuando el numero ingresado sea negativo")
num=int(input())
S=int
while num>0:
    S=0
    for i in range(1,num+1):
        if num % i == 0:
            S=S+i
    print("La suma de los divisores del numero es: ",S)
    print("Introduce un numero, y para terminar uno negativo:")
    num=int(input("num: "))