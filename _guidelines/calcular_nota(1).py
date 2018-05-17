#Programa para saber la nota

nota = int(input("Introduce tu nota: "))

if nota < 5:
  print("Insuficiente: esfuerzate mas")
elif nota < 6:
  print("Suficiente")
elif nota < 7:
  print("Bien")
elif nota < 9:
  print("Notable")  
else:
  print("Sobresaliente: eres un/a crack")

