#Programa per calcular el major numero
num1 = 18
num2 = 14
num3 = 12

if (num1 >= num2) and (num1 >= num3):
   mayor = num1
elif (num2 >= num1) and (num2 >= num3):
   mayor = num2
else:
   mayor = num3

print("El mayor numero entre " + str(num1) + ", " + str(num2) + " y " + str(num3) + " es " + str(mayor))