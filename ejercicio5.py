#5
a=float(input("digite el coeficiente a:"))
b=float(input("digite el coeficiente b:"))
c=float(input("digite el coeficiente c:"))
operacion=((-b)+(b**2-4*a*c)**0.5)/(2*a)
operacion1=((-b)-(b**2-4*a*c)**0.5)/(2*a)
print(f"la primera solucion de la ecuacion {operacion} y la segunda {operacion1}")