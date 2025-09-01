#1
numero=int(input("digite un numero entero:"))
valor=numero
for i in range (numero, numero+101):
    numero=numero+i

print(f"la suma de los siguientes 100 numeros del {valor} es {numero}")
